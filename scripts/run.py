# scripts/run.py
import os
import subprocess
import shutil
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--device", default="pixel_5")
    ap.add_argument("--apk", default="apk/android/app-demo-debug.apk")
    args = ap.parse_args()

    os.environ["DEVICE_NAME"] = args.device
    os.environ["APP_PATH"] = os.path.abspath(args.apk)

    # 清理旧报告
    shutil.rmtree("outputs/reports", ignore_errors=True)
    os.makedirs("outputs/reports", exist_ok=True)

    # 运行测试（取消注释以启用）
    # subprocess.run([
    #     "pytest", "test_cases",
    #     "--alluredir=outputs/reports",
    #     "--clean-alluredir"
    # ], check=True)

    # 本地打开报告（可选）
    try:
        subprocess.run(["allure", "serve", "outputs/reports"], check=True)
    except FileNotFoundError:
        print("提示: 未安装 allure 命令行工具，跳过报告服务启动")
        print("报告文件已生成在 outputs/reports 目录中")

if __name__ == "__main__":
    main()
