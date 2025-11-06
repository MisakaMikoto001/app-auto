# Tab_invite.py
"""
邀请标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabInvitePage(BasePage):
    # 页面元素定位器
    INVITE_TITLE = (AppiumBy.ID, "invite_title_id")
    INVITE_CODE = (AppiumBy.ID, "invite_code_id")
    COPY_BUTTON = (AppiumBy.ID, "copy_button_id")
    SHARE_BUTTON = (AppiumBy.ID, "share_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")
    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")

    def __init__(self, driver):
        super().__init__(driver)

    def get_invite_title(self):
        """获取邀请页面标题"""
        return self.get_text(self.INVITE_TITLE)

