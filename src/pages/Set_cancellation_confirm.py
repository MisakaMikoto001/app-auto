# Set_cancellation_confirm.py
"""
注销确认设置页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SetCancellationConfirmPage(BasePage):
    # 页面元素定位器
    CANCELLATION_TITLE = (AppiumBy.ID, "cancellation_title_id")
    CANCELLATION_MESSAGE = (AppiumBy.ID, "cancellation_message_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cancellation_title(self):
        """获取注销确认标题"""
        return self.get_text(self.CANCELLATION_TITLE)

    def get_cancellation_message(self):
        """获取注销确认消息"""
        return self.get_text(self.CANCELLATION_MESSAGE)

    def click_confirm(self):
        """点击确认注销按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def click_cancel(self):
        """点击取消注销按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_cancellation_page_displayed(self):
        """检查注销确认页面是否显示"""
        return self.wait_for_element_visible(self.CANCELLATION_TITLE)
