# My_wallet.py
"""
我的钱包页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MyWalletPage(BasePage):
    # 页面元素定位器
    WALLET_BALANCE = (AppiumBy.ID, "wallet_balance_id")
    RECHARGE_BUTTON = (AppiumBy.ID, "recharge_button_id")
    WITHDRAW_BUTTON = (AppiumBy.ID, "withdraw_button_id")
    TRANSACTION_RECORD = (AppiumBy.ID, "transaction_record_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_wallet_balance(self):
        """获取钱包余额"""
        return self.get_text(self.WALLET_BALANCE)

    def click_recharge(self):
        """点击充值按钮"""
        self.click_element(self.RECHARGE_BUTTON)

    def click_withdraw(self):
        """点击提现按钮"""
        self.click_element(self.WITHDRAW_BUTTON)

    def click_transaction_record(self):
        """点击交易记录"""
        self.click_element(self.TRANSACTION_RECORD)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_wallet_page_displayed(self):
        """检查钱包页面是否显示"""
        return self.wait_for_element_visible(self.WALLET_BALANCE)
