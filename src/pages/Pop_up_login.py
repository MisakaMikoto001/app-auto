# Pop_up_login.py
"""
弹窗登录页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpLoginPage(BasePage):
    # 页面元素定位器
    POPUP_TITLE = (AppiumBy.ID, "tv_title")
    CLOSE_BUTTON = (AppiumBy.ID, "btnClose")
    WECHAT_LOGIN_BUTTON = (AppiumBy.ID, "btnWechat")
    TEL_LOGIN_BUTTON = (AppiumBy.ID, "//*[@text='手机登录']")
    USER_TEL = (AppiumBy.ID, "et_phone")
    USER_CODE = (AppiumBy.ID, "et_verify_code")
    LOGIN_BUTTON = (AppiumBy.ID, "btnLogin")
    CHECK_BOX = (AppiumBy.ID, "ivCheck")
    AGREEMENT_CHECK = (AppiumBy.XPATH, "//*[@text='我已阅读并同意']")
    PRIVACY_POLICY = (AppiumBy.XPATH, "//*[@text='《隐私政策》']")
    USER_AGREEMENT = (AppiumBy.XPATH, "//*[@text='《用户协议》']")
    CONFIRM_POPUP_REJECT = (AppiumBy.ID, "btnReject")
    CONFIRM_POPUP_AGREE = (AppiumBy.ID, "btnAgree")


    def __init__(self, driver):
        super().__init__(driver)

    def is_popup_title_displayed(self):
        """检查弹窗标题是否显示"""
        return self.is_element_displayed(self.POPUP_TITLE)

    def is_popup_displayed(self):
        """检查弹窗是否显示"""
        return self.wait_for_element_visible(self.POPUP_TITLE)

    def is_popup_tel_displayed(self):
        """检查手机登录是否显示"""
        return self.is_element_displayed(self.USER_CODE)

    def is_popup_closed(self):
        """检查弹窗是否关闭"""
        return not self.is_popup_displayed()

    def is_confirm_popup_displayed(self):
        """检查弹窗是否显示"""
        return self.wait_for_element_visible(self.CONFIRM_POPUP_AGREE)

    def input_user_tel(self, tel):
        """输入用户手机号"""
        self.input_text(self.USER_TEL, tel)

    def input_user_code(self, code):
        """输入验证码"""
        self.input_text(self.USER_CODE, code)

    def click_login_wechat(self):
        """点击微信登录"""
        self.click_element(self.WECHAT_LOGIN_BUTTON)

    def click_login_tel(self):
        """点击手机登录"""
        self.click_element(self.TEL_LOGIN_BUTTON)

    def click_login(self):
        """点击登录按钮"""
        self.click_element(self.LOGIN_BUTTON)

    def click_check_box(self):
        """点击勾选框"""
        self.click_element(self.CHECK_BOX)

    def click_privacy_policy(self):
        """点击隐私政策"""
        self.click_element(self.PRIVACY_POLICY)

    def click_user_agreement(self):
        """点击用户协议"""
        self.click_element(self.USER_AGREEMENT)

    def click_confirm_popup_agree(self):
        """点击确认弹窗-同意"""
        self.click_element(self.CONFIRM_POPUP_AGREE)

    def click_confirm_popup_reject(self):
        """点击确认弹窗-拒绝"""
        self.click_element(self.CONFIRM_POPUP_REJECT)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

class PopUpLoginWeChatBusiness(PopUpLoginPage):
    """弹窗登录业务逻辑类"""
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_login_page = PopUpLoginPage(driver)

    def login_with_wechat(self):
        """微信登录流程"""
        if self.popup_login_page.is_popup_displayed():
            # 点击微信登录
            self.popup_login_page.click_login_wechat()
            print("已选择微信登录")
            return True
        else:
            print("登录弹窗未显示，无法进行微信登录")
            return False

class PopUpLoginTelBusiness(PopUpLoginPage):
    """弹窗登录业务逻辑类"""
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_login_page = PopUpLoginPage(driver)

    def login_with_phone(self, phone, code):
        """手机号登录流程"""
        if self.popup_login_page.is_popup_displayed():
            # 点击手机号登录
            self.popup_login_page.click_login_tel()

            # 输入手机号
            if self.popup_login_page.is_popup_tel_displayed():
                self.popup_login_page.input_user_tel(phone)

                # 输入验证码
                self.popup_login_page.input_user_code(code)

                # 勾选协议
                self.popup_login_page.click_check_box()

            # 点击登录按钮
            self.popup_login_page.click_login()

            print(f"已使用手机号 {phone} 登录")
            return True
        else:
            print("登录弹窗未显示，无法进行手机号登录")
            return False

