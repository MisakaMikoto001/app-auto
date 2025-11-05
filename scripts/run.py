#!/usr/bin/env python3
import os, subprocess, shutil, argparse, datetime
from src.common.yaml_reader import YamlReader

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

    # pytest + allure
    subprocess.run([
        "pytest", "test_cases",
        "--alluredir=outputs/reports",
        "--device", args.device,
        "--clean-alluredir"
    ], check=True)

    # 本地打开报告
    subprocess.run(["allure", "serve", "outputs/reports"])

if __name__ == "__main__":
    main()