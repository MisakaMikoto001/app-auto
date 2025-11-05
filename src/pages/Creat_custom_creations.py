# Creat_custom_creations.py
"""
创建自定义创作页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CreatCustomCreationsPage(BasePage):
    # 页面元素定位器
    TITLE_INPUT = (AppiumBy.ID, "title_input_id")
    CONTENT_INPUT = (AppiumBy.ID, "content_input_id")
    CREATE_BUTTON = (AppiumBy.ID, "create_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_title(self, title):
        """输入标题"""
        self.input_text(self.TITLE_INPUT, title)

    def input_content(self, content):
        """输入内容"""
        self.input_text(self.CONTENT_INPUT, content)

    def click_create(self):
        """点击创建按钮"""
        self.click_element(self.CREATE_BUTTON)

    def click_cancel(self):
        """点击取消按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def create_custom_creation(self, title, content):
        """创建自定义创作完整流程"""
        self.input_title(title)
        self.input_content(content)
        self.click_create()
