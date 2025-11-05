"""
所有页面对象的基类，封装滑动、等待、截图
"""

from src.common.yaml_reader import YamlReader
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.yaml_reader = None  # 延迟初始化

    def get_yaml_reader(self, yaml_path):
        """获取 YamlReader 实例"""
        if self.yaml_reader is None:
            self.yaml_reader = YamlReader(yaml_path)
        return self.yaml_reader

    def read_config(self, file_path):
        """读取 YAML 配置文件"""
        return self.yaml_reader.read(file_path)

    def get_config_value(self, file_path, key):
        """获取配置文件中的特定值"""
        config = self.read_config(file_path)
        return config.get(key)

    def find_element(self, locator, timeout=10):
        """查找元素"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        """查找多个元素"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def get_text(self, locator, timeout=10):
        """获取元素文本"""
        element = self.find_element(locator, timeout)
        return element.text

    def click_element(self, locator, timeout=10):
        """点击元素"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text, timeout=10):
        """输入文本"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def swipe_up(self, duration=1000):
        """向上滑动"""
        size = self.driver.get_window_size()
        x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(x, start_y, x, end_y, duration)

    def swipe_down(self, duration=1000):
        """向下滑动"""
        size = self.driver.get_window_size()
        x = size['width'] // 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(x, start_y, x, end_y, duration)

    def go_back(self, times=1):
        """返回上一步/多步
        Args:
            times (int): 返回的步数，默认为1
        """
        for _ in range(times):
            self.driver.back()

    def wait_for_element_visible(self, locator, timeout=10):
        """等待元素可见"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def assert_element_present(self, locator, timeout=10, message="Element is not present"):
        """断言元素存在"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            raise AssertionError(message)

    def assert_element_not_present(self, locator, timeout=10, message="Element is still present"):
        """断言元素不存在"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            raise AssertionError(message)
        except TimeoutException:
            return True

    def assert_element_visible(self, locator, timeout=10, message="Element is not visible"):
        """断言元素可见"""
        try:
            self.wait_for_element_visible(locator, timeout)
            return True
        except TimeoutException:
            raise AssertionError(message)

    def assert_element_text(self, locator, expected_text, timeout=10, message=None):
        """断言元素文本等于预期值"""
        if message is None:
            message = f"Element text does not match. Expected: '{expected_text}'"
        element_text = self.get_text(locator, timeout)
        if element_text != expected_text:
            raise AssertionError(f"{message}. Actual: '{element_text}'")

    def assert_element_contains_texts(self, locator, expected_texts, timeout=10, message=None):
        """断言元素文本包含多个预期值"""
        if isinstance(expected_texts, str):
            expected_texts = [expected_texts]

        if message is None:
            message = f"Element text does not contain all expected texts: {expected_texts}"

        element_text = self.get_text(locator, timeout)
        missing_texts = []

        for text in expected_texts:
            if text not in element_text:
                missing_texts.append(text)

        if missing_texts:
            raise AssertionError(f"{message}. Missing texts: {missing_texts}. Actual text: '{element_text}'")

    def take_screenshot(self, filename):
        """截图"""
        self.driver.save_screenshot(filename)

    def close_app(self):
        """关闭应用程序"""
        try:
            self.driver.terminate_app(self.driver.capabilities.get('appPackage'))
            return True
        except Exception as e:
            print(f"关闭应用程序失败: {e}")
            return False

    def launch_app(self):
        """启动应用程序"""
        try:
            package_name = self.driver.capabilities.get('appPackage')
            if not package_name:
                raise ValueError("无法获取应用包名")

            # 激活应用
            self.driver.activate_app(package_name)
            return True
        except Exception as e:
            print(f"启动应用程序失败: {e}")
            return False

    def clear_app_cache(self):
        """清除应用程序缓存"""
        try:
            # 获取当前应用的包名
            package_name = self.driver.capabilities.get('appPackage')
            if not package_name:
                raise ValueError("无法获取应用包名")

            # 使用 adb 命令清除应用缓存
            self.driver.execute_script('mobile: shell', {
                'command': 'pm',
                'args': ['clear', package_name]
            })
            return True
        except Exception as e:
            print(f"清除应用缓存失败: {e}")
            return False

    def is_app_closed(self, timeout=10, message="Application is still running"):
        """
        断言应用程序已关闭
        Args:
            timeout (int): 等待超时时间，默认为10秒
            message (str): 断言失败时的错误信息
        Returns:
            bool: 如果应用已关闭返回True
        Raises:
            AssertionError: 如果应用仍在运行
        """
        try:
            # 获取当前活动的 activity
            activity = self.driver.current_activity
            # 如果能成功获取且不为空，则说明应用仍在运行
            if activity:
                raise AssertionError(message)
            else:
                return True
        except Exception:
            # 出现异常通常表示应用已关闭
            return True

    def is_app_running(self, timeout=10):
        """
        检查应用程序是否仍在运行
        Args:
            timeout (int): 等待超时时间，默认为10秒
        Returns:
            bool: 如果应用正在运行返回True，否则返回False
        """
        try:
            # 尝试获取当前上下文，如果应用关闭会抛出异常
            current_context = self.driver.context
            return current_context is not None
        except Exception:
            return False
