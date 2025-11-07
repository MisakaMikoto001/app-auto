# Tab_invite.py
"""
邀请标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabInvitePage(BasePage):
    # 页面元素定位器
    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")

    def __init__(self, driver):
        super().__init__(driver)

    def click_tab_index(self):
        """点击首页标签"""
        self.click_element(self.TAB_INDEX)

    def click_tab_create(self):
        """点击创作标签"""
        self.click_element(self.TAB_CREATE)

    def click_tab_ability(self):
        """点击能力标签"""
        self.click_element(self.TAB_ABILITY)

    def click_tab_invitation(self):
        """点击邀请标签"""
        self.click_element(self.TAB_INVITATION)

    def click_tab_mine(self):
        """点击我的标签"""
        self.click_element(self.TAB_MINE)



