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
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import logging
from typing import List, Dict, Tuple

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_device_config(config_path: str) -> List[Dict]:
    """
    加载设备配置文件

    Args:
        config_path (str): 设备配置文件路径

    Returns:
        list: 设备配置列表
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config.get('devices', [])
    except FileNotFoundError:
        logger.error(f"配置文件未找到: {config_path}")
        return []
    except yaml.YAMLError as e:
        logger.error(f"配置文件解析错误: {e}")
        return []


def check_allure_installed() -> bool:
    """
    检查 allure 命令是否可用

    Returns:
        bool: allure 是否可用
    """
    try:
        subprocess.run(["allure", "--version"],
                      check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.warning("Allure 命令未安装或不可用")
        return False


def run_test_on_device(device_config: Dict, test_dir: str = "test_cases",
                      report_dir: str = "outputs/reports") -> Tuple[str, str]:
    """
    在指定设备上运行测试

    Args:
        device_config (dict): 设备配置信息
        test_dir (str): 测试用例目录
        report_dir (str): 报告输出目录

    Returns:
        tuple: (设备名, 执行状态)
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
        sys.executable, "-m", "pytest",
        test_dir,
        f"--alluredir={device_report_dir}",
        "--clean-alluredir"
    ]

    logger.info(f"在设备 {device_name} 上启动测试...")
    logger.debug(f"执行命令: {' '.join(cmd)}")

    try:
        # 执行测试
        result = subprocess.run(cmd, env=env, check=True,
                                capture_output=True, text=True, timeout=3600)
        logger.info(f"设备 {device_name} 测试完成")
        logger.debug(f"测试输出: {result.stdout}")
        return device_name, "SUCCESS"
    except subprocess.CalledProcessError as e:
        logger.error(f"设备 {device_name} 测试失败: {e}")
        logger.error(f"错误输出: {e.stderr}")
        return device_name, "FAILED"
    except subprocess.TimeoutExpired:
        logger.error(f"设备 {device_name} 测试超时")
        return device_name, "TIMEOUT"


def merge_allure_reports(report_dirs: List[str],
                        merged_dir: str = "outputs/merged_report") -> bool:
    """
    合并多个设备的 Allure 报告

    Args:
        report_dirs (list): 报告目录列表
        merged_dir (str): 合并后的报告目录

    Returns:
        bool: 合并是否成功
    """
    if not report_dirs:
        logger.warning("没有报告目录需要合并")
        return False

    os.makedirs(merged_dir, exist_ok=True)

    # 使用 allure 命令合并报告
    cmd = ["allure", "generate"] + report_dirs + ["-o", merged_dir, "--clean"]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logger.info(f"合并报告已生成到: {merged_dir}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"合并报告失败: {e}")
        logger.error(f"错误输出: {e.stderr}")
        return False
    except FileNotFoundError:
        logger.error("Allure 命令未找到，无法合并报告")
        return False


def serve_allure_report(report_dir: str) -> bool:
    """
    启动 Allure 报告服务

    Args:
        report_dir (str): 报告目录

    Returns:
        bool: 启动是否成功
    """
    try:
        logger.info(f"正在启动 Allure 报告服务: {report_dir}")
        subprocess.run(["allure", "serve", report_dir], check=True)
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"启动 Allure 报告服务失败: {e}")
        return False
    except FileNotFoundError:
        logger.error("Allure 命令未找到，无法启动报告服务")
        return False


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
    parser.add_argument("--no-merge", action="store_true",
                        help="不合并报告")
    parser.add_argument("--no-serve", action="store_true",
                        help="不启动报告服务")

    args = parser.parse_args()

    # 检查 allure 是否安装
    allure_installed = check_allure_installed()

    # 加载设备配置
    devices = load_device_config(args.config)
    if not devices:
        logger.error("未找到设备配置")
        sys.exit(1)

    logger.info(f"发现 {len(devices)} 个设备，开始并行测试...")

    # 清理旧报告
    shutil.rmtree(args.report_dir, ignore_errors=True)
    os.makedirs(args.report_dir, exist_ok=True)

    # 并行执行测试
    results = []
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        # 提交所有任务
        future_to_device = {
            executor.submit(run_test_on_device, device, args.test_dir, args.report_dir): device
            for device in devices
        }

        # 收集结果
        for future in as_completed(future_to_device):
            device = future_to_device[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                device_name = device.get('deviceName', 'unknown')
                logger.error(f"设备 {device_name} 执行异常: {e}")
                results.append((device_name, "ERROR"))

    # 输出测试结果
    logger.info("\n测试结果汇总:")
    success_count = 0
    for device_name, status in results:
        logger.info(f"  {device_name}: {status}")
        if status == "SUCCESS":
            success_count += 1

    logger.info(f"成功: {success_count}/{len(results)}")

    # 收集所有报告目录
    report_dirs = [
        os.path.join(args.report_dir, d)
        for d in os.listdir(args.report_dir)
        if os.path.isdir(os.path.join(args.report_dir, d))
    ]

    # 合并报告
    merged_success = False
    if report_dirs and not args.no_merge and allure_installed:
        merged_success = merge_allure_reports(report_dirs)

    # 启动合并报告服务
    if merged_success and not args.no_serve and allure_installed:
        serve_allure_report("outputs/merged_report")

    # 返回执行状态码
    if success_count != len(results):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
