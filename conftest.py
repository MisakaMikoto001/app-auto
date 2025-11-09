import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import time
from src.common.yaml_reader import YamlReader
import sys
import subprocess
import logging.handlers
from typing import Optional

project_root = os.path.dirname(os.path.abspath(__file__))

# 创建日志目录
logs_dir = os.path.join(project_root, "outputs", "logs")
os.makedirs(logs_dir, exist_ok=True)

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.handlers.RotatingFileHandler(
            os.path.join(logs_dir, "app_auto.log"),
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
    ]
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def driver():
    """提供 Appium WebDriver 实例"""
    # 从环境变量获取配置
    device_name = os.environ.get("DEVICE_NAME", "pixel_5")
    app_path = os.environ.get("APP_PATH", "apk/android/app-demo-debug.apk")

    # 加载设备配置
    try:
        config_data = YamlReader.load_yaml("config/devices.yaml")

        if device_name not in config_data:
            available_devices = list(config_data.keys())
            raise KeyError(f"设备 '{device_name}' 未在 config/devices.yaml 中定义。可用设备: {available_devices}")

        device_config = config_data[device_name]

    except FileNotFoundError:
        raise FileNotFoundError("配置文件 config/devices.yaml 不存在")

    # 更新应用路径
    if "app" in device_config or "appPackage" not in device_config:
        device_config["app"] = os.path.abspath(app_path)

    # 使用 UiAutomator2Options
    options = UiAutomator2Options()

    # 设置基本选项
    for key, value in device_config.items():
        try:
            if hasattr(options, key):
                setattr(options, key, value)
            else:
                options.set_capability(key, value)
        except Exception as e:
            print(f"警告: 无法设置选项 {key}: {e}")

    # 尝试连接 Appium 服务器
    max_retries = 3
    for attempt in range(max_retries):
        try:
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723',
                options=options
            )
            yield driver
            driver.quit()
            return
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"连接尝试 {attempt + 1} 失败: {e}")
                time.sleep(2)
            else:
                raise e


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """pytest钩子函数，用于生成测试报告"""
    outcome = yield
    try:
        rep = outcome.get_result()
        # 使用更安全的方式设置属性，避免覆盖已有属性
        attr_name = "rep_" + rep.when
        if not hasattr(item, attr_name):
            setattr(item, attr_name, rep)
    except Exception as e:
        # 记录异常但不中断测试执行
        print(f"pytest_runtest_makereport 钩子函数异常: {e}")



@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """测试失败时自动截图保存"""
    yield
    # 检查测试是否失败
    if request.node.rep_call.failed:
        # 确保截图目录存在
        screenshot_dir = os.path.join(project_root, "outputs", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        # 生成截图文件名（避免特殊字符）
        test_name = "".join(c for c in request.node.name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{test_name}_failure_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        screenshot_path = os.path.abspath(screenshot_path)

        # 保存截图
        try:
            driver.get_screenshot_as_file(screenshot_path)

            if sys.platform.startswith('win'):
                os.system(f"dir > nul")  # Windows刷新

            time.sleep(1)  # 等待文件写入

            # 检查文件
            if os.path.exists(screenshot_path):
                file_size = os.path.getsize(screenshot_path)
                print(f"截图已保存成功: {screenshot_path}, 大小: {file_size} 字节")
            else:
                print(f"截图文件未找到: {screenshot_path}")
                # 列出目录内容
                files = os.listdir(screenshot_dir) if os.path.exists(screenshot_dir) else []
                print(f"目录中的文件: {files}")

        except Exception as e:
            print(f"保存截图时发生异常: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()


def check_allure_installed() -> bool:
    """
    检查 allure 命令是否可用

    Returns:
        bool: allure 是否可用
    """
    try:
        # 使用完整的环境变量
        env = os.environ.copy()

        # 检查 allure 是否在 PATH 中
        if os.name == 'nt':  # Windows
            result = subprocess.run(
                ["where", "allure"],
                check=True,
                capture_output=True,
                text=True,
                shell=True,
                env=env
            )
        else:  # Unix/Linux/Mac
            result = subprocess.run(
                ["which", "allure"],
                check=True,
                capture_output=True,
                text=True,
                env=env
            )

        logger.debug(f"找到 allure 路径: {result.stdout.strip()}")

        # 检查版本
        version_result = subprocess.run(
            ["allure", "--version"],
            check=True,
            capture_output=True,
            text=True,
            env=env
        )
        logger.info(f"Allure 版本: {version_result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logger.warning(f"Allure 命令未安装或不可用: {e}")
        return False


def run_tests(test_cases_dir: str, reports_dir: str) -> int:
    """
    运行测试用例

    Args:
        test_cases_dir (str): 测试用例目录
        reports_dir (str): 报告输出目录

    Returns:
        int: 测试返回码
    """
    logger.info("开始运行测试...")

    cmd = [
        sys.executable, "-m", "pytest",
        test_cases_dir,
        f"--alluredir={reports_dir}",
        "--clean-alluredir"
    ]

    logger.debug(f"执行命令: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True)
        logger.info("所有测试执行成功")
        return result.returncode
    except subprocess.CalledProcessError as e:
        logger.error(f"测试执行失败，返回码: {e.returncode}")
        return e.returncode

def generate_allure_report(reports_dir: str, allure_report_dir: str) -> bool:
    """
    生成 Allure 静态报告
    """
    logger.info("正在生成静态HTML报告...")

    try:
        result = subprocess.run([
            "allure", "generate", reports_dir, "-o", allure_report_dir, "--clean"
        ], check=True, env=os.environ.copy(), shell=True)

        logger.info(f"静态HTML报告已生成至 {allure_report_dir}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"报告生成失败: {e}")
        return False
    except FileNotFoundError as e:
        logger.error(f"Allure 命令未找到: {e}")
        return False


def start_allure_server(allure_report_dir: str) -> Optional[subprocess.Popen]:
    """
    启动 Allure 报告服务器
    """
    logger.info("正在启动Allure报告服务器...")
    logger.info(f"报告地址: file://{os.path.join(os.path.abspath(allure_report_dir), 'index.html')}")

    try:
        # 添加环境变量
        env = os.environ.copy()
        process = subprocess.Popen(
            ["allure", "open", allure_report_dir],
            env=env,
            shell=True
        )

        # 等待10秒后自动停止
        time.sleep(10)
        if process.poll() is None:  # 检查进程是否仍在运行
            process.terminate()
            try:
                process.wait(timeout=5)
                logger.info("Allure 服务器已自动停止")
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
                logger.warning("Allure 服务器强制终止")

        return process
    except FileNotFoundError as e:
        logger.error(f"Allure 命令未找到: {e}")
        return None
    except Exception as e:
        logger.error(f"启动服务器时出错: {e}")
        return None
