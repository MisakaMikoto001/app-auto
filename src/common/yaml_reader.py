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

    def read(self):
        """
        读取 YAML 文件内容

        Returns:
            dict: YAML 文件解析后的数据
        """
        if self._data is None:
            with open(self.yaml_path, 'r', encoding='utf-8') as f:
                self._data = yaml.safe_load(f)
        return self._data

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
        with open(yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
