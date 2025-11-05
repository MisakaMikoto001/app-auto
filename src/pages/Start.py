# Start.py
"""
启动页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class StartPage(BasePage):
    # 页面元素定位器
    TITLE = (AppiumBy.ID, "tv_title")
    DESCRIPTION = (AppiumBy.ID, "tv_content")
    AGREE_BUTTON = (AppiumBy.ID, "start_button_id")
    REJECT_BUTTON = (AppiumBy.ID, "skip_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def click_start(self):
        """点击开始按钮"""
        self.click_element(self.START_BUTTON)

    def click_skip(self):
        """点击跳过按钮"""
        self.click_element(self.SKIP_BUTTON)

    def is_logo_displayed(self):
        """检查Logo是否显示"""
        return self.wait_for_element_visible(self.LOGO_IMAGE)

    def wait_for_start_page(self, timeout=10):
        """等待启动页加载完成"""
        return self.wait_for_element_visible(self.START_BUTTON, timeout)

