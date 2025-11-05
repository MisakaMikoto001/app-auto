# Set_cancellation_notice.py
"""
注销通知设置页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SetCancellationNoticePage(BasePage):
    # 页面元素定位器
    NOTICE_TITLE = (AppiumBy.ID, "notice_title_id")
    NOTICE_CONTENT = (AppiumBy.ID, "notice_content_id")
    AGREE_CHECKBOX = (AppiumBy.ID, "agree_checkbox_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_notice_title(self):
        """获取注销通知标题"""
        return self.get_text(self.NOTICE_TITLE)

    def get_notice_content(self):
        """获取注销通知内容"""
        return self.get_text(self.NOTICE_CONTENT)

    def click_agree_checkbox(self):
        """点击同意复选框"""
        self.click_element(self.AGREE_CHECKBOX)

    def click_confirm(self):
        """点击确认按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_notice_page_displayed(self):
        """检查注销通知页面是否显示"""
        return self.wait_for_element_visible(self.NOTICE_TITLE)
