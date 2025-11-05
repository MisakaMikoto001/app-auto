# Wallet_withdrawal_details.py
"""
钱包提现详情页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class WalletWithdrawalDetailsPage(BasePage):
    # 页面元素定位器
    WITHDRAWAL_DETAILS_TITLE = (AppiumBy.ID, "withdrawal_details_title_id")
    WITHDRAWAL_AMOUNT = (AppiumBy.ID, "withdrawal_amount_id")
    WITHDRAWAL_STATUS = (AppiumBy.ID, "withdrawal_status_id")
    WITHDRAWAL_TIME = (AppiumBy.ID, "withdrawal_time_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_withdrawal_amount(self):
        """获取提现金额"""
        return self.get_text(self.WITHDRAWAL_AMOUNT)

    def get_withdrawal_status(self):
        """获取提现状态"""
        return self.get_text(self.WITHDRAWAL_STATUS)

    def get_withdrawal_time(self):
        """获取提现时间"""
        return self.get_text(self.WITHDRAWAL_TIME)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_withdrawal_details_page_displayed(self):
        """检查提现详情页面是否显示"""
        return self.wait_for_element_visible(self.WITHDRAWAL_DETAILS_TITLE)
