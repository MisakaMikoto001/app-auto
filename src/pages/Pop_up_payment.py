# Pop_up_payment.py
"""
弹窗支付页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpPaymentPage(BasePage):
    # 页面元素定位器
    PAYMENT_TITLE = (AppiumBy.ID, "payment_title_id")
    PAYMENT_AMOUNT = (AppiumBy.ID, "payment_amount_id")
    WECHAT_PAY_BUTTON = (AppiumBy.ID, "wechat_pay_button_id")
    ALIPAY_BUTTON = (AppiumBy.ID, "alipay_button_id")
    BANK_CARD_BUTTON = (AppiumBy.ID, "bank_card_button_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_payment_title(self):
        """获取支付弹窗标题"""
        return self.get_text(self.PAYMENT_TITLE)

    def get_payment_amount(self):
        """获取支付金额"""
        return self.get_text(self.PAYMENT_AMOUNT)

    def click_wechat_pay(self):
        """点击微信支付"""
        self.click_element(self.WECHAT_PAY_BUTTON)

    def click_alipay(self):
        """点击支付宝支付"""
        self.click_element(self.ALIPAY_BUTTON)

    def click_bank_card(self):
        """点击银行卡支付"""
        self.click_element(self.BANK_CARD_BUTTON)

    def click_confirm(self):
        """点击确认支付按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def click_cancel(self):
        """点击取消支付按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        """关闭支付弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_payment_popup_displayed(self):
        """检查支付弹窗是否显示"""
        return self.wait_for_element_visible(self.PAYMENT_TITLE)
