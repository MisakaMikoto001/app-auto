# Pop_up_generated_successfully.py
"""
弹窗生成成功页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpGeneratedSuccessfullyPage(BasePage):
    # 页面元素定位器
    SUCCESS_TITLE = (AppiumBy.ID, "success_title_id")
    SUCCESS_MESSAGE = (AppiumBy.ID, "success_message_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_success_title(self):
        """获取成功弹窗标题"""
        return self.get_text(self.SUCCESS_TITLE)

    def get_success_message(self):
        """获取成功弹窗消息内容"""
        return self.get_text(self.SUCCESS_MESSAGE)

    def click_confirm(self):
        """点击确认按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_success_popup_displayed(self):
        """检查生成成功弹窗是否显示"""
        return self.wait_for_element_visible(self.SUCCESS_TITLE)
