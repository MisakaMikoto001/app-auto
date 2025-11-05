#!/usr/bin/env python3
"""
多设备并行测试执行脚本
支持同时在多个设备上运行测试用例
"""

import os
import subprocess
import shutil
import argparse
import yaml
from concurrent.futures import ThreadPoolExecutor
import sys


def load_device_config(config_path):
    """
    加载设备配置文件

    Args:
        config_path (str): 设备配置文件路径

    Returns:
        list: 设备配置列表
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config.get('devices', [])


def run_test_on_device(device_config, test_dir="test_cases", report_dir="outputs/reports"):
    """
    在指定设备上运行测试

    Args:
        device_config (dict): 设备配置信息
        test_dir (str): 测试用例目录
        report_dir (str): 报告输出目录
    """
    device_name = device_config.get('deviceName', 'unknown')
    udid = device_config.get('udid', '')

    # 创建设备专属报告目录
    device_report_dir = os.path.join(report_dir, f"device_{device_name}")
    os.makedirs(device_report_dir, exist_ok=True)

    # 设置环境变量
    env = os.environ.copy()
    env['DEVICE_NAME'] = device_name
    env['UDID'] = udid

    # 构建 pytest 命令
    cmd = [
        "pytest",
        test_dir,
        f"--alluredir={device_report_dir}",
        "--clean-alluredir"
    ]

    print(f"在设备 {device_name} 上启动测试...")

    try:
        # 执行测试
        result = subprocess.run(cmd, env=env, check=True,
                                capture_output=True, text=True)
        print(f"设备 {device_name} 测试完成")
        return device_name, "SUCCESS"
    except subprocess.CalledProcessError as e:
        print(f"设备 {device_name} 测试失败: {e}")
        return device_name, "FAILED"


def merge_allure_reports(report_dirs, merged_dir="outputs/merged_report"):
    """
    合并多个设备的 Allure 报告

    Args:
        report_dirs (list): 报告目录列表
        merged_dir (str): 合并后的报告目录
    """
    os.makedirs(merged_dir, exist_ok=True)

    # 使用 allure 命令合并报告
    cmd = ["allure", "generate"] + report_dirs + ["-o", merged_dir, "--clean"]
    try:
        subprocess.run(cmd, check=True)
        print(f"合并报告已生成到: {merged_dir}")
    except subprocess.CalledProcessError as e:
        print(f"合并报告失败: {e}")


def main():
    parser = argparse.ArgumentParser(description="并行执行多设备测试")
    parser.add_argument("--config", default="config/devices.yaml",
                        help="设备配置文件路径")
    parser.add_argument("--test-dir", default="test_cases",
                        help="测试用例目录")
    parser.add_argument("--report-dir", default="outputs/reports",
                        help="报告输出目录")
    parser.add_argument("--max-workers", type=int, default=3,
                        help="最大并行工作线程数")

    args = parser.parse_args()

    # 加载设备配置
    devices = load_device_config(args.config)
    if not devices:
        print("未找到设备配置")
        sys.exit(1)

    print(f"发现 {len(devices)} 个设备，开始并行测试...")

    # 清理旧报告
    shutil.rmtree(args.report_dir, ignore_errors=True)
    os.makedirs(args.report_dir, exist_ok=True)

    # 并行执行测试
    results = []
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = [
            executor.submit(run_test_on_device, device, args.test_dir, args.report_dir)
            for device in devices
        ]

        # 等待所有任务完成
        for future in futures:
            result = future.result()
            results.append(result)

    # 输出测试结果
    print("\n测试结果汇总:")
    for device_name, status in results:
        print(f"  {device_name}: {status}")

    # 收集所有报告目录
    report_dirs = [
        os.path.join(args.report_dir, d)
        for d in os.listdir(args.report_dir)
        if os.path.isdir(os.path.join(args.report_dir, d))
    ]

    # 合并报告
    if report_dirs:
        merge_allure_reports(report_dirs)

    # 启动合并报告服务
    try:
        subprocess.run(["allure", "serve", "outputs/merged_report"])
    except subprocess.CalledProcessError:
        print("无法启动 Allure 报告服务")


if __name__ == "__main__":
    main()
