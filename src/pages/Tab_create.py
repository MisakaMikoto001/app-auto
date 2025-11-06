# Tab_create.py
"""
创建标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabCreatePage(BasePage):
    # 页面元素定位器
    CREATE_TITLE = (AppiumBy.ID, "create_title_id")
    CREATE_INPUT = (AppiumBy.ID, "create_input_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_create_content(self, content):
        """输入创建内容"""
        self.input_text(self.CREATE_INPUT, content)

    def click_confirm(self):
        """点击确认按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def click_cancel(self):
        """点击取消按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def create_item(self, content):
        """创建项目完整流程"""
        self.input_create_content(content)
        self.click_confirm()

    def is_create_page_displayed(self):
        """检查创建页面是否显示"""
        return self.wait_for_element_visible(self.CREATE_TITLE)
