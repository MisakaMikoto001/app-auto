"""
所有页面对象的基类，封装滑动、等待、截图
"""

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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

    def wait_for_element_visible(self, locator, timeout=10):
        """等待元素可见"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def take_screenshot(self, filename):
        """截图"""
        self.driver.save_screenshot(filename)

    def get_text(self, locator, timeout=10):
        """获取元素文本"""
        element = self.find_element(locator, timeout)
        return element.text
