# Start.py
"""
启动页面对象类
"""

from src.base_page import BasePage
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

    def wait_for_start_page(self, timeout=30):  # 增加超时时间
        """等待启动页加载完成"""
        return self.wait_for_element_visible(self.AGREE_BUTTON, timeout)

    def is_agree_button_displayed(self):
        """检查同意按钮是否显示"""
        return self.wait_for_element_visible(self.AGREE_BUTTON)

    def click_agree(self):
        """点击同意进入APP"""
        self.click_element(self.AGREE_BUTTON)

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

    def wait_for_start_page(self, timeout=10):
        """等待启动页加载完成"""
        return self.wait_for_element_visible(self.AGREE_BUTTON, timeout)

