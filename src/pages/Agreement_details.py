# Agreement_details.py
"""
协议详情页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class AgreementDetailsPage(BasePage):
    # 页面元素定位器
    AGREEMENT_TITLE = (AppiumBy.ID, "agreement_title_id")
    AGREEMENT_CONTENT = (AppiumBy.ID, "agreement_content_id")
    ACCEPT_BUTTON = (AppiumBy.ID, "accept_button_id")
    DECLINE_BUTTON = (AppiumBy.ID, "decline_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_agreement_title(self):
        """获取协议标题"""
        return self.get_text(self.AGREEMENT_TITLE)

    def get_agreement_content(self):
        """获取协议内容"""
        return self.get_text(self.AGREEMENT_CONTENT)

    def click_accept(self):
        """点击同意按钮"""
        self.click_element(self.ACCEPT_BUTTON)

    def click_decline(self):
        """点击拒绝按钮"""
        self.click_element(self.DECLINE_BUTTON)

    def close_agreement(self):
        """关闭协议页面"""
        self.click_element(self.CLOSE_BUTTON)

    def is_agreement_displayed(self):
        """检查协议页面是否显示"""
        return self.wait_for_element_visible(self.AGREEMENT_TITLE)
