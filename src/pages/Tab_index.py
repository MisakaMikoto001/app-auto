# Tab_index.py
"""
首页标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabIndexPage(BasePage):
    # 页面元素定位器
    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_index(self):
        """切换到首页标签"""
        self.click_element(self.TAB_INDEX)
