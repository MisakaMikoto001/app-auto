# Pop_up_login.py
"""
弹窗登录页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpLoginPage(BasePage):
    # 页面元素定位器
    CLOSE_BUTTON = (AppiumBy.ID, "btnClose")
    USER_TEL = (AppiumBy.ID, "et_phone")
    USER_CODE = (AppiumBy.ID, "et_verify_code")
    LOGIN_BUTTON = (AppiumBy.ID, "btnlogin")
    WECHAT_LOGIN_BUTTON = (AppiumBy.ID, "btnlogin")
    TEL_LOGIN_BUTTON = (AppiumBy.ID, "//*[@text='手机登录']")
    AGREEMENT_CHECK = (AppiumBy.XPATH, "//*[@text='我已阅读并同意']")
    POPUP_TITLE = (AppiumBy.ID, "popup_title_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        """输入用户手机号"""
        self.input_text(self.USER_TEL, username)

    def input_password(self, password):
        """输入验证码"""
        self.input_text(self.USER_CODE, password)

    def click_login(self):
        """点击登录按钮"""
        self.click_element(self.LOGIN_BUTTON)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_popup_displayed(self):
        """检查弹窗是否显示"""
        return self.wait_for_element_visible(self.POPUP_TITLE)

    def login(self, username, password):
        """完整的登录流程"""
        self.input_username(username)
        self.input_password(password)
        self.click_login()
