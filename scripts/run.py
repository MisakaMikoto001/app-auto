# import os
# import time
# import subprocess
# import argparse
# import sys
# import signal
# from datetime import datetime
# from typing import Optional
# import logging.handlers
#
# # 创建日志目录
# project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# logs_dir = os.path.join(project_root, "outputs", "logs")
# os.makedirs(logs_dir, exist_ok=True)
#
# # 配置日志格式
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.StreamHandler(),
#         logging.handlers.RotatingFileHandler(
#             os.path.join(logs_dir, "app_auto.log"),
#             maxBytes=10*1024*1024,  # 10MB
#             backupCount=5
#         )
#     ]
# )
# logger = logging.getLogger(__name__)
#
# # 全局变量存储进程引用
# allure_process: Optional[subprocess.Popen] = None
#
#
# def signal_handler(sig, frame):
#     """信号处理器，用于关闭Allure服务器"""
#     global allure_process
#
#     logger.info("\n正在停止Allure服务器...")
#
#     if allure_process and isinstance(allure_process, subprocess.Popen):
#         try:
#             allure_process.terminate()
#             allure_process.wait(timeout=5)
#             logger.info("Allure 服务器已关闭")
#         except subprocess.TimeoutExpired:
#             logger.warning("服务器关闭超时，强制终止...")
#             allure_process.kill()
#             allure_process.wait()
#         except Exception as e:
#             logger.error(f"关闭 Allure 服务器时出错: {e}")
#         finally:
#             allure_process = None
#     else:
#         logger.info("Allure 服务器未运行或已关闭")
#
#     sys.exit(0)
#
# def check_allure_installed() -> bool:
#     """
#     检查 allure 命令是否可用
#
#     Returns:
#         bool: allure 是否可用
#     """
#     try:
#         # 使用完整的环境变量
#         env = os.environ.copy()
#
#         # 检查 allure 是否在 PATH 中
#         if os.name == 'nt':  # Windows
#             result = subprocess.run(
#                 ["where", "allure"],
#                 check=True,
#                 capture_output=True,
#                 text=True,
#                 shell=True,
#                 env=env
#             )
#         else:  # Unix/Linux/Mac
#             result = subprocess.run(
#                 ["which", "allure"],
#                 check=True,
#                 capture_output=True,
#                 text=True,
#                 env=env
#             )
#
#         logger.debug(f"找到 allure 路径: {result.stdout.strip()}")
#
#         # 检查版本
#         version_result = subprocess.run(
#             ["allure", "--version"],
#             check=True,
#             capture_output=True,
#             text=True,
#             env=env
#         )
#         logger.info(f"Allure 版本: {version_result.stdout.strip()}")
#         return True
#     except (subprocess.CalledProcessError, FileNotFoundError) as e:
#         logger.warning(f"Allure 命令未安装或不可用: {e}")
#         return False
#
# def run_tests(test_cases_dir: str, reports_dir: str) -> int:
#     """
#     运行测试用例
#
#     Args:
#         test_cases_dir (str): 测试用例目录
#         reports_dir (str): 报告输出目录
#
#     Returns:
#         int: 测试返回码
#     """
#     logger.info("开始运行测试...")
#
#     cmd = [
#         sys.executable, "-m", "pytest",
#         test_cases_dir,
#         f"--alluredir={reports_dir}",
#         "--clean-alluredir"
#     ]
#
#     logger.debug(f"执行命令: {' '.join(cmd)}")
#
#     try:
#         result = subprocess.run(cmd, check=True)
#         logger.info("所有测试执行成功")
#         return result.returncode
#     except subprocess.CalledProcessError as e:
#         logger.error(f"测试执行失败，返回码: {e.returncode}")
#         return e.returncode
#
# def generate_allure_report(reports_dir: str, allure_report_dir: str) -> bool:
#     """
#     生成 Allure 静态报告
#     """
#     logger.info("正在生成静态HTML报告...")
#
#     try:
#         result = subprocess.run([
#             "allure", "generate", reports_dir, "-o", allure_report_dir, "--clean"
#         ], check=True, env=os.environ.copy(), shell=True)
#
#         logger.info(f"静态HTML报告已生成至 {allure_report_dir}")
#         return True
#     except subprocess.CalledProcessError as e:
#         logger.error(f"报告生成失败: {e}")
#         return False
#     except FileNotFoundError as e:
#         logger.error(f"Allure 命令未找到: {e}")
#         return False
#
# def start_allure_server(allure_report_dir: str) -> Optional[subprocess.Popen]:
#     """
#     启动 Allure 报告服务器
#     """
#     logger.info("正在启动Allure报告服务器...")
#     logger.info(f"报告地址: file://{os.path.join(os.path.abspath(allure_report_dir), 'index.html')}")
#
#     try:
#         # 添加环境变量
#         env = os.environ.copy()
#         process = subprocess.Popen(
#             ["allure", "open", allure_report_dir],
#             env=env,
#             shell=True
#         )
#
#         # 等待10秒后自动停止
#         time.sleep(10)
#         if process.poll() is None:  # 检查进程是否仍在运行
#             process.terminate()
#             try:
#                 process.wait(timeout=5)
#                 logger.info("Allure 服务器已自动停止")
#             except subprocess.TimeoutExpired:
#                 process.kill()
#                 process.wait()
#                 logger.warning("Allure 服务器强制终止")
#
#         return process
#     except FileNotFoundError as e:
#         logger.error(f"Allure 命令未找到: {e}")
#         return None
#     except Exception as e:
#         logger.error(f"启动服务器时出错: {e}")
#         return None
#
#
# def main():
#     global allure_process
#
#     npm_global_path = os.path.expanduser("~/AppData/Roaming/npm")
#     if os.path.exists(npm_global_path) and npm_global_path not in os.environ.get("PATH", ""):
#         os.environ["PATH"] = f"{npm_global_path};{os.environ.get('PATH', '')}"
#
#
#     # 注册信号处理器
#     signal.signal(signal.SIGINT, signal_handler)
#     signal.signal(signal.SIGTERM, signal_handler)
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--device", default="pixel_5")
#     parser.add_argument("--apk", default="apk/android/app-demo-debug.apk")
#     parser.add_argument("--no-report", action="store_true",
#                         help="不生成报告")
#     parser.add_argument("--no-server", action="store_true",
#                         help="不启动报告服务器")
#
#     args = parser.parse_args()
#
#     os.environ["DEVICE_NAME"] = args.device
#     os.environ["APP_PATH"] = os.path.abspath(args.apk)
#
#     # 构建路径
#     reports_dir = os.path.join(project_root, "outputs", "reports")
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     allure_report_dir = os.path.join(project_root, "outputs", "allure-report", f"test_{timestamp}")
#     test_cases_dir = os.path.join(project_root, "test_cases")
#
#     # 创建必要的目录
#     os.makedirs(reports_dir, exist_ok=True)
#     os.makedirs(os.path.dirname(allure_report_dir), exist_ok=True)
#
#     # 运行测试
#     test_return_code =  run_tests(test_cases_dir, reports_dir)
#
#     # 检查allure
#     # if not check_allure_installed():
#     #     logger.info("跳过静态报告生成（Allure 未安装）")
#     #     sys.exit(test_return_code)
#
#     # 生成静态HTML报告
#     report_generated = False
#     if not args.no_report:
#         report_generated = generate_allure_report(reports_dir, allure_report_dir)
#
#     # 启动报告服务器
#     if report_generated and not args.no_server:
#         allure_process = start_allure_server(allure_report_dir)
#         if allure_process:
#             logger.info("按 Ctrl+C 停止服务器")
#             try:
#                 # 等待服务器进程结束
#                 allure_process.wait()
#             except KeyboardInterrupt:
#                 # 正常的中断处理
#                 signal_handler(signal.SIGINT, None)
#
#     sys.exit(test_return_code)
#
#
# if __name__ == "__main__":
#     main()


import os
import time
import subprocess
import argparse
import sys
import signal
from datetime import datetime
from typing import Optional
import logging

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 从 conftest 导入所需函数
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from conftest import (
    logger,
    run_tests,
    generate_allure_report,
    start_allure_server,
    check_allure_installed
)

# 全局变量存储进程引用
allure_process: Optional[subprocess.Popen] = None


def signal_handler(sig, frame):
    """信号处理器，用于关闭Allure服务器"""
    global allure_process

    logger.info("\n正在停止Allure服务器...")

    if allure_process and isinstance(allure_process, subprocess.Popen):
        try:
            allure_process.terminate()
            allure_process.wait(timeout=5)
            logger.info("Allure 服务器已关闭")
        except subprocess.TimeoutExpired:
            logger.warning("服务器关闭超时，强制终止...")
            allure_process.kill()
            allure_process.wait()
        except Exception as e:
            logger.error(f"关闭 Allure 服务器时出错: {e}")
        finally:
            allure_process = None
    else:
        logger.info("Allure 服务器未运行或已关闭")

    sys.exit(0)


def main():
    global allure_process

    npm_global_path = os.path.expanduser("~/AppData/Roaming/npm")
    if os.path.exists(npm_global_path) and npm_global_path not in os.environ.get("PATH", ""):
        os.environ["PATH"] = f"{npm_global_path};{os.environ.get('PATH', '')}"

    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="pixel_5")
    parser.add_argument("--apk", default="apk/android/app-demo-debug.apk")
    parser.add_argument("--no-report", action="store_true",
                        help="不生成报告")
    parser.add_argument("--no-server", action="store_true",
                        help="不启动报告服务器")

    args = parser.parse_args()

    os.environ["DEVICE_NAME"] = args.device
    os.environ["APP_PATH"] = os.path.abspath(args.apk)

    # 构建路径
    reports_dir = os.path.join(project_root, "outputs", "reports")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    allure_report_dir = os.path.join(project_root, "outputs", "allure-report", f"test_{timestamp}")
    test_cases_dir = os.path.join(project_root, "test_cases")

    # 创建必要的目录
    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(os.path.dirname(allure_report_dir), exist_ok=True)

    # 运行测试
    test_return_code = run_tests(test_cases_dir, reports_dir)

    # 检查allure
    # if not check_allure_installed():
    #     logger.info("跳过静态报告生成（Allure 未安装）")
    #     sys.exit(test_return_code)

    # 生成静态HTML报告
    report_generated = False
    if not args.no_report:
        report_generated = generate_allure_report(reports_dir, allure_report_dir)

    # 启动报告服务器
    if report_generated and not args.no_server:
        allure_process = start_allure_server(allure_report_dir)
        if allure_process:
            logger.info("按 Ctrl+C 停止服务器")
            try:
                # 等待服务器进程结束
                allure_process.wait()
            except KeyboardInterrupt:
                # 正常的中断处理
                signal_handler(signal.SIGINT, None)

    sys.exit()


if __name__ == "__main__":
    main()
