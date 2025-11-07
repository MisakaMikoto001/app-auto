import os
import time
import subprocess
import argparse
import sys
import signal
from datetime import datetime
import keyboard
import threading

print(f"Python 路径: {sys.executable}")
print(f"PATH 环境变量: {os.environ.get('PATH')}")

# 全局变量存储进程引用
allure_process = None
# 添加线程同步锁
process_lock = threading.Lock()

def signal_handler(sig, frame):
    """信号处理器，用于关闭Allure服务器"""
    print("\n\n正在停止Allure服务器...")
    global allure_process

    # 只有当 allure_process 是一个有效的 Popen 对象时才进行终止操作
    if allure_process and isinstance(allure_process, subprocess.Popen):
        try:
            allure_process.terminate()
            allure_process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            allure_process.kill()
        except Exception as e:
            print(f"关闭 Allure 服务器时出错: {e}")
        finally:
            allure_process = None  # 清理引用
    else:
        print("Allure 服务器未运行或已关闭")

    sys.exit(0)


def main():
    global allure_process  # 声明使用全局变量

    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    ap = argparse.ArgumentParser()
    ap.add_argument("--device", default="pixel_5")
    ap.add_argument("--apk", default="apk/android/app-demo-debug.apk")
    args = ap.parse_args()

    os.environ["DEVICE_NAME"] = args.device
    os.environ["APP_PATH"] = os.path.abspath(args.apk)

    # 获取项目根目录路径
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 构建正确的路径
    reports_dir = os.path.join(project_root, "outputs", "reports")

    # 创建带时间戳的报告文件夹
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    allure_report_dir = os.path.join(project_root, "outputs", "allure-report", f"test_{timestamp}")

    test_cases_dir = os.path.join(project_root, "test_cases")

    # 运行测试
    test_result = subprocess.run([
        "pytest", test_cases_dir,
        f"--alluredir={reports_dir}",
        "--clean-alluredir"
    ])

    if test_result.returncode == 0:
        print("所有测试执行成功")
    else:
        print(f"测试执行完成，{test_result.returncode}个测试失败")

    # 生成静态HTML报告
    try:
        result = subprocess.run([
            "allure", "generate",
            reports_dir,
            "-o", allure_report_dir,
            "--clean"
        ], check=True, shell=True)

        print(f"静态HTML报告已生成至 {allure_report_dir}")
        time.sleep(1)
    except FileNotFoundError:
        print("提示: 未安装 allure 命令行工具，跳过静态报告生成")
    except subprocess.CalledProcessError as e:
        print(f"报告生成失败: {e}")

    # 打开网页版测试报告
    # try:
    #     print("正在启动Allure报告服务器...")
    #     with process_lock:
    #         allure_process = subprocess.Popen(["allure", "open", allure_report_dir], shell=True)
    #     print("服务器已启动")
    #     print("浏览器已打开报告页面")
    #     print("按 ESC 键停止服务器并退出程序")
    #
    #     # 检测键盘，按esc关闭程序
    #     def check_keyboard():
    #         try:
    #             while True:
    #                 with process_lock:
    #                     if allure_process is None or \
    #                             not hasattr(allure_process, 'poll') or \
    #                             allure_process.poll() is not None:
    #                         break
    #
    #                 if keyboard.is_pressed('esc'):
    #                     print("\n检测到 ESC 键，正在退出...")
    #                     signal_handler(signal.SIGINT, None)
    #                     break
    #                 time.sleep(0.1)  # 防止CPU占用过高
    #         except Exception:
    #             pass  # 忽略键盘检测中的异常
    #
    #     # 启动键盘检测线程
    #     keyboard_thread = threading.Thread(target=check_keyboard, daemon=True)
    #     keyboard_thread.start()
    #
    #     with process_lock:
    #         if allure_process:
    #             allure_process.wait()
    # except FileNotFoundError:
    #     print("提示: 未安装 allure 命令行工具，无法自动打开报告")
    #     print(f"你可以手动打开 {allure_report_dir}/index.html 查看报告")
    # except KeyboardInterrupt:
    #     signal_handler(signal.SIGINT, None)
    # except Exception as e:
    #     print(f"启动报告服务器时出错: {e}")

    # 打开网页版测试报告
    try:
        print("正在启动Allure报告服务器...")
        allure_process = subprocess.Popen(["allure", "open", allure_report_dir], shell=True)
        print(f"报告地址: {allure_report_dir}/index.html")
        time.sleep(10)
        signal_handler(signal.SIGINT, None)
    except Exception as e:
        print(f"启动服务器时出错: {e}")

if __name__ == "__main__":
    main()
