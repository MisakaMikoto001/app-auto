# Pop_up_login.py
"""
弹窗登录页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import re

class PopUpLoginPage(BasePage):
    # 页面元素定位器
    POPUP_TITLE = (AppiumBy.ID, "iv_title")
    CLOSE_BUTTON = (AppiumBy.ID, "btnClose")
    WECHAT_LOGIN_BUTTON = (AppiumBy.ID, "btnWechat")
    TEL_LOGIN_BUTTON = (AppiumBy.ID, "btnPhone")
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

    def click_check_box_1(self):
        """点击勾选框"""
        self.click_element(self.CHECK_BOX)

    def click_check_box_2(self):
        """点击勾选框"""
        self.click_element(self.AGREEMENT_CHECK)

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
    """弹窗微信登录业务逻辑类"""
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_login_page = PopUpLoginPage(driver)

    def login_with_wechat(self):
        """微信登录流程"""
        if self.popup_login_page.is_popup_displayed():
            # 点击微信登录
            self.popup_login_page.click_check_box_1()
            self.popup_login_page.click_login_wechat()
            print("已选择微信登录")
            return True
        else:
            print("登录弹窗未显示，无法进行微信登录")
            return False

class PopUpLoginTelBusiness(PopUpLoginPage):
    """弹窗手机登录业务逻辑类"""
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_login_page = PopUpLoginPage(driver)

    @staticmethod
    def validate_phone_format(phone):
        """验证手机号格式是否正确(11位中国手机号)"""
        pattern = r'^1[3-9]\d{9}$'
        return bool(re.match(pattern, phone))

    @staticmethod
    def validate_verification_code(code):
        """验证验证码格式是否正确(4位数字)"""
        pattern = r'^\d{4}$'
        return bool(re.match(pattern, code))
    #
    # def login_with_phone(self,phone, code):
    #     """手机号登录流程"""
    #     if self.popup_login_page.is_popup_displayed():
    #         # 点击手机号登录
    #         self.popup_login_page.click_login_tel()
    #
    #         # 输入手机号
    #         if self.popup_login_page.is_popup_tel_displayed():
    #             self.popup_login_page.input_user_tel(phone)
    #
    #             # 输入验证码
    #             self.popup_login_page.input_user_code(code)
    #
    #             # 勾选协议
    #             self.popup_login_page.click_check_box_2()
    #
    #             # 验证手机号、验证码、并登录
    #             if phone and self.validate_phone_format(phone):
    #                 if code and self.validate_verification_code(code):
    #                     self.popup_login_page.click_login()
    #                     print(f"已使用手机号 {phone} 验证码 {code}登录")
    #                     return True
    #                 else:
    #                     print(f"验证码格式错误 {code}")
    #                     return False
    #             else:
    #                 print(f"手机号格式错误 {phone}")
    #                 return False
    #         else:
    #             print("手机号登录弹窗未显示")
    #             return False
    #     else:
    #         print("登录弹窗未显示，无法进行手机号登录")
    #         return False
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
                self.popup_login_page.click_check_box_2()

                # 验证手机号、验证码、并登录
                if phone and self.validate_phone_format(phone):
                    if code and self.validate_verification_code(code):
                        self.popup_login_page.click_login()
                        print(f"已使用手机号 {phone} 验证码 {code}登录")
                        return True
                    else:
                        print(f"验证码格式错误 {code}")
                        # 验证码格式错误时应该显示相应吐司
                        self.assert_toast_visible("请输入正确的验证码")
                        return False
                else:
                    print(f"手机号格式错误 {phone}")
                    # 手机号格式错误时应该显示相应吐司
                    self.assert_toast_visible("请输入正确的手机号")
                    return False
            else:
                print("手机号登录弹窗未显示")
                return False
        else:
            print("登录弹窗未显示，无法进行手机号登录")
            return False

    def login_with_flash_test(self):
        """手机号登录流程"""
        if self.popup_login_page.is_popup_displayed():
            # 点击手机号登录
            self.popup_login_page.click_login_tel()

            # 点确认一键登录
            self.popup_login_page.click_confirm_popup_agree()
            return True
        else:
            print("登录弹窗未显示，无法进行一键登录")
            return False


