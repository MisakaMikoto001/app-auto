# Print_publicity.py
"""
打印宣传页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PrintPublicityPage(BasePage):
    # 页面元素定位器
    PUBLICITY_TITLE = (AppiumBy.ID, "publicity_title_id")
    PRINT_BUTTON = (AppiumBy.ID, "print_button_id")
    SHARE_BUTTON = (AppiumBy.ID, "share_button_id")
    DOWNLOAD_BUTTON = (AppiumBy.ID, "download_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_publicity_title(self):
        """获取宣传标题"""
        return self.get_text(self.PUBLICITY_TITLE)

    def click_print(self):
        """点击打印按钮"""
        self.click_element(self.PRINT_BUTTON)

    def click_share(self):
        """点击分享按钮"""
        self.click_element(self.SHARE_BUTTON)

    def click_download(self):
        """点击下载按钮"""
        self.click_element(self.DOWNLOAD_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_publicity_page_displayed(self):
        """检查宣传页面是否显示"""
        return self.wait_for_element_visible(self.PUBLICITY_TITLE)
