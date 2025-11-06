"""
YAML 文件读取工具类
"""

import yaml
import os


class YamlReader:
    def __init__(self, yaml_path):
        """
        初始化 YamlReader

        Args:
            yaml_path (str): YAML 文件路径
        """
        if not os.path.exists(yaml_path):
            raise FileNotFoundError(f"YAML 文件不存在: {yaml_path}")
        self.yaml_path = yaml_path
        self._data = None

    def read(self, file_path=None):
        """
        读取 YAML 文件内容

        Args:
            file_path (str, optional): YAML 文件路径，如果不提供则使用初始化时的路径

        Returns:
            dict: YAML 文件解析后的数据
        """
        # 确定要读取的文件路径
        path = file_path if file_path is not None else self.yaml_path

        # 如果是初始化路径且已有缓存数据，则直接返回缓存
        if file_path is None and self._data is not None:
            return self._data

        # 读取并解析 YAML 文件
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # 如果是初始化路径，缓存数据
        if file_path is None:
            self._data = data

        return data

    def get(self, key, default=None):
        """
        获取 YAML 数据中的指定键值

        Args:
            key (str): 键名
            default: 默认值

        Returns:
            任意类型: 键对应的值
        """
        data = self.read()
        return data.get(key, default) if isinstance(data, dict) else default

    @staticmethod
    def load_yaml(yaml_path):
        """
        静态方法直接加载 YAML 文件

        Args:
            yaml_path (str): YAML 文件路径

        Returns:
            dict: 解析后的 YAML 数据
        """

        # 如果是相对路径，则基于项目根目录
        if not os.path.isabs(yaml_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            yaml_path = os.path.join(project_root, yaml_path)

        with open(yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
