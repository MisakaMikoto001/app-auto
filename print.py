import os

project_root = os.path.dirname(os.path.abspath(__file__))

screenshot_dir = os.path.join(project_root, "outputs", "screenshots")


print(f"环境变量:{ os.environ.copy()} ")
print(f"截图目录:{ screenshot_dir} ")



