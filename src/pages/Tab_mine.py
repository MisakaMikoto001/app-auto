# Tab_mine.py
"""
我的标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabMinePage(BasePage):
    # 页面元素定位器
    MINE_TITLE = (AppiumBy.ID, "mine_title_id")
    USER_AVATAR = (AppiumBy.ID, "user_avatar_id")
    USER_NAME = (AppiumBy.ID, "user_name_id")
    SETTINGS_BUTTON = (AppiumBy.ID, "settings_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")
    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")

    def __init__(self, driver):
        super().__init__(driver)

    def get_user_name(self):
        """获取用户名"""
        return self.get_text(self.USER_NAME)
