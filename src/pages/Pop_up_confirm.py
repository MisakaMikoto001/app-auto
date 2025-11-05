# Pop_up_confirm.py
"""
弹窗确认页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpConfirmPage(BasePage):
    # 页面元素定位器
    CONFIRM_TITLE = (AppiumBy.ID, "confirm_title_id")
    CONFIRM_MESSAGE = (AppiumBy.ID, "confirm_message_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_confirm_title(self):
        """获取确认弹窗标题"""
        return self.get_text(self.CONFIRM_TITLE)

    def get_confirm_message(self):
        """获取确认弹窗消息内容"""
        return self.get_text(self.CONFIRM_MESSAGE)

    def click_confirm(self):
        """点击确认按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def click_cancel(self):
        """点击取消按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_confirm_popup_displayed(self):
        """检查确认弹窗是否显示"""
        return self.wait_for_element_visible(self.CONFIRM_TITLE)
