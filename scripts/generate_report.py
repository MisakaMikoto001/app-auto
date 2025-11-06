# scripts/generate_report.py
import subprocess
import os


def generate_test_report():
    # 运行测试并生成allure结果
    subprocess.run(["pytest", "--alluredir=./outputs/reports"])

    # 生成HTML报告
    report_output_dir = "./outputs/allure-report"
    os.makedirs(report_output_dir, exist_ok=True)
    subprocess.run(["allure", "generate", "./outputs/reports", "-o", report_output_dir, "--clean"])

    print(f"测试报告已生成至: {report_output_dir}")


if __name__ == "__main__":
    generate_test_report()
