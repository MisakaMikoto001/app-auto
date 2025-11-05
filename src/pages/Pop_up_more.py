# Pop_up_more.py
"""
弹窗更多页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpMorePage(BasePage):
    # 页面元素定位器
    MORE_TITLE = (AppiumBy.ID, "more_title_id")
    OPTION_LIST = (AppiumBy.ID, "option_list_id")
    OPTION_ITEM = (AppiumBy.ID, "option_item_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_more_title(self):
        """获取更多弹窗标题"""
        return self.get_text(self.MORE_TITLE)

    def get_option_list(self):
        """获取选项列表"""
        return self.find_elements(self.OPTION_LIST)

    def click_option(self, option_index=0):
        """点击指定选项"""
        options = self.find_elements(self.OPTION_ITEM)
        if option_index < len(options):
            options[option_index].click()

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_more_popup_displayed(self):
        """检查更多弹窗是否显示"""
        return self.wait_for_element_visible(self.MORE_TITLE)
