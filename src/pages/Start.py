# Start.py
"""
启动页面对象类
"""

from src.base_page import BasePage
from src.pages.Policy import PrivacyPolicyPage
from appium.webdriver.common.appiumby import AppiumBy


class StartPage(BasePage):
    # 页面元素定位器
    LOGO_IMAGE = (AppiumBy.ID, "iv_logo")
    TITLE = (AppiumBy.ID, "tv_title")
    CONTENT = (AppiumBy.ID, "tv_content")
    AGREE_BUTTON = (AppiumBy.ID, "tv_agree")
    REJECT_BUTTON = (AppiumBy.ID, "tv_reject")
    PRIVACY_POLICY = (AppiumBy.XPATH, "//*[@text='隐私政策']")
    USER_AGREEMENT = (AppiumBy.XPATH, "//*[@text='用户协议']")

    def __init__(self, driver):
        super().__init__(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)

    def wait_for_start_page(self, timeout=30):  # 增加超时时间
        """等待启动页加载完成"""
        return self.wait_for_element_visible(self.AGREE_BUTTON, timeout)

    def is_agree_button_displayed(self):
        """检查同意按钮是否显示"""
        return self.wait_for_element_visible(self.AGREE_BUTTON)

    def click_agree(self):
        """点击同意进入APP"""
        self.click_element(self.AGREE_BUTTON)

    def is_reject_button_displayed(self):
        """检查不同意按钮是否显示"""
        return self.wait_for_element_visible(self.REJECT_BUTTON)

    def click_reject(self):
        """点击不同意退出APP"""
        self.click_element(self.REJECT_BUTTON)

    def is_logo_displayed(self):
        """检查Logo是否显示"""
        return self.wait_for_element_visible(self.LOGO_IMAGE)

    def is_title_displayed(self):
        """检查标题是否显示"""
        return self.wait_for_element_visible(self.TITLE)

    def is_content_displayed(self):
        """检查内容是否显示"""
        return self.wait_for_element_visible(self.CONTENT)

    def click_privacy_policy(self, locator, expected_texts, timeout=10):
        """点击隐私政策，并断言元素包含指定文本"""
        self.click_element(locator, timeout)
        assert self.assert_element_contains_texts(locator, expected_texts), \
            f"元素 {locator} 不包含预期文本: {expected_texts}"

    def click_user_agreement(self, locator, expected_texts, timeout=10):
        """点击用户协议，并断言元素包含指定文本"""
        self.click_element(locator, timeout)
        assert self.assert_element_contains_texts(locator, expected_texts), \
            f"元素 {locator} 不包含预期文本: {expected_texts}"

class StartPageBusiness(StartPage):
    """启动页面业务逻辑类"""
    def __init__(self, driver):
        super().__init__(driver)  
        
    def start_page_get_in(self, retry_count = 0):
        if retry_count >= 3:
            print("已达到最大重试次数，启动页仍未显示")
            return

        self.wait_for_start_page()
        
        if self.is_agree_button_displayed():
            self.click_agree()
        else:
            print("启动页未显示，正在清理缓存、重启APP。。。")
            self.clear_app_cache()
            self.close_app()
            self.launch_app()
            self.start_page_get_in(retry_count+1)

    def start_page_get_out(self, retry_count = 0):
        if retry_count >= 3:
            print("已达到最大重试次数，启动页仍未显示")
            return

        self.wait_for_start_page()

        if self.is_reject_button_displayed():
            self.click_reject()
        else:
            print("启动页未显示，正在清理缓存、重启APP。。。")
            self.clear_app_cache()
            self.close_app()
            self.launch_app()
            self.start_page_get_out(retry_count+1)

    def start_page_check_policy(self, retry_count = 0):
        if retry_count >= 3:
            print("已达到最大重试次数，启动页仍未显示")
            return

        self.wait_for_start_page()

        if self.is_content_displayed():
            self.click_user_agreement(self.USER_AGREEMENT, ["用户协议"])
            if (self.privacy_policy_page.is_content_displayed()
                    and self.privacy_policy_page.is_title_displayed()
                    and self.privacy_policy_page.get_title_text()=="用户协议"
                ):
                print("用户协议存在")
            else:
                print("用户协议不存在")
            self.go_back()
            self.click_privacy_policy(self.PRIVACY_POLICY, ["隐私政策"])
            if (self.privacy_policy_page.is_content_displayed()
                    and self.privacy_policy_page.is_title_displayed()
                    and self.privacy_policy_page.get_title_text()=="隐私政策"
            ):
                print("隐私政策存在")
            else:
                print("隐私政策不存在")

            self.close_app()
        else:
            print("启动页未显示，正在清理缓存、重启APP。。。")
            self.clear_app_cache()
            self.close_app()
            self.launch_app()
            self.start_page_check_policy(retry_count+1)