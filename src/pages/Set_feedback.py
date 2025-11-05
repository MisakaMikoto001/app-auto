# Set_feedback.py
"""
反馈设置页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SetFeedbackPage(BasePage):
    # 页面元素定位器
    FEEDBACK_TITLE = (AppiumBy.ID, "feedback_title_id")
    FEEDBACK_INPUT = (AppiumBy.ID, "feedback_input_id")
    CONTACT_INPUT = (AppiumBy.ID, "contact_input_id")
    SUBMIT_BUTTON = (AppiumBy.ID, "submit_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_feedback_content(self, content):
        """输入反馈内容"""
        self.input_text(self.FEEDBACK_INPUT, content)

    def input_contact_info(self, contact):
        """输入联系方式"""
        self.input_text(self.CONTACT_INPUT, contact)

    def click_submit(self):
        """点击提交按钮"""
        self.click_element(self.SUBMIT_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def submit_feedback(self, content, contact=""):
        """提交反馈完整流程"""
        self.input_feedback_content(content)
        if contact:
            self.input_contact_info(contact)
        self.click_submit()

    def is_feedback_page_displayed(self):
        """检查反馈页面是否显示"""
        return self.wait_for_element_visible(self.FEEDBACK_TITLE)
