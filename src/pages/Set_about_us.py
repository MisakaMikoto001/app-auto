# Set_about_us.py
"""
关于我们设置页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SetAboutUsPage(BasePage):
    # 页面元素定位器
    ABOUT_US_TITLE = (AppiumBy.ID, "about_us_title_id")
    VERSION_INFO = (AppiumBy.ID, "version_info_id")
    COMPANY_INFO = (AppiumBy.ID, "company_info_id")
    CONTACT_US = (AppiumBy.ID, "contact_us_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_about_us_title(self):
        """获取关于我们页面标题"""
        return self.get_text(self.ABOUT_US_TITLE)

    def get_version_info(self):
        """获取版本信息"""
        return self.get_text(self.VERSION_INFO)

    def get_company_info(self):
        """获取公司信息"""
        return self.get_text(self.COMPANY_INFO)

    def click_contact_us(self):
        """点击联系我们"""
        self.click_element(self.CONTACT_US)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_about_us_page_displayed(self):
        """检查关于我们页面是否显示"""
        return self.wait_for_element_visible(self.ABOUT_US_TITLE)
