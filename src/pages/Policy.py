"""
隐私政策页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PrivacyPolicyPage(BasePage):
    """隐私政策页面"""

    # 页面元素定位器
    TITLE = (AppiumBy.ID, "toolbarTitle")  # 标题
    CONTENT = (AppiumBy.ID, "webview")  # 内容区域
    NO_DATA = (AppiumBy.ID, "no_data")

    def __init__(self, driver):
        super().__init__(driver)

    def is_title_displayed(self):
        """检查标题是否显示"""
        return self.is_element_displayed(self.TITLE)

    def get_title_text(self):
        """获取标题文本"""
        return self.get_text(self.TITLE)

    def is_content_displayed(self):
        """检查内容是否显示"""
        return self.is_element_displayed(self.CONTENT)

    def is_no_data_displayed(self):
        """检查无数据提示是否显示"""
        return self.is_element_displayed(self.NO_DATA)

    def get_content_text(self):
        """获取内容文本"""
        return self.get_text(self.CONTENT)



