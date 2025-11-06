import os
import subprocess
import shutil
import argparse
import sys
import signal
import time
print(f"Python 路径: {sys.executable}")
print(f"PATH 环境变量: {os.environ.get('PATH')}")



def main():
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
    allure_report_dir = os.path.join(project_root, "outputs", "allure-report")
    test_cases_dir = os.path.join(project_root, "test_cases")

    # 清理旧报告
    shutil.rmtree(reports_dir, ignore_errors=True)
    os.makedirs(reports_dir, exist_ok=True)

    print("当前工作目录:", os.getcwd())
    print("test_cases 目录内容:")
    if os.path.exists(test_cases_dir):
        print(os.listdir(test_cases_dir))
    else:
        print("test_cases 目录不存在")

    # 运行测试（即使测试失败也继续执行）
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
        subprocess.run([
            "allure", "generate",
            reports_dir,
            "-o", allure_report_dir,
            "--clean"
        ], check=True, shell=True)  # 添加 shell=True 参数
        print(f"静态HTML报告已生成至 {allure_report_dir}")
    except FileNotFoundError:
        print("提示: 未安装 allure 命令行工具，跳过静态报告生成")

    # 打开网页版测试报告
    try:
        subprocess.run(["allure", "open", allure_report_dir], check=True, shell=True)  # 添加 shell=True 参数
        print("已打开网页版测试报告")
    except FileNotFoundError:
        print("提示: 未安装 allure 命令行工具，无法自动打开报告")
        print(f"你可以手动打开 {allure_report_dir}/index.html 查看报告")

    def signal_handler(sig, frame):
        print("\n正在停止服务器...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()
