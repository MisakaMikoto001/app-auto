# My_member_top_up.py
"""
会员充值页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MyMemberTopUpPage(BasePage):
    # 页面元素定位器
    RECHARGE_AMOUNT_INPUT = (AppiumBy.ID, "recharge_amount_input_id")
    RECHARGE_BUTTON = (AppiumBy.ID, "recharge_button_id")
    BALANCE_TEXT = (AppiumBy.ID, "balance_text_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")
    PAYMENT_METHOD_SELECTOR = (AppiumBy.ID, "payment_method_selector_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_recharge_amount(self, amount):
        """输入充值金额"""
        self.input_text(self.RECHARGE_AMOUNT_INPUT, amount)

    def click_recharge(self):
        """点击充值按钮"""
        self.click_element(self.RECHARGE_BUTTON)

    def get_balance(self):
        """获取当前余额"""
        return self.get_text(self.BALANCE_TEXT)

    def select_payment_method(self, method):
        """选择支付方式"""
        # 这里可以根据具体实现进行调整
        self.click_element(self.PAYMENT_METHOD_SELECTOR)
        # 选择具体的支付方式逻辑

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def recharge_balance(self, amount):
        """充值余额完整流程"""
        self.input_recharge_amount(amount)
        self.click_recharge()
