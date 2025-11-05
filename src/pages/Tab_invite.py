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

    def __init__(self, driver):
        super().__init__(driver)

    def get_invite_title(self):
        """获取邀请页面标题"""
        return self.get_text(self.INVITE_TITLE)

    def get_invite_code(self):
        """获取邀请码"""
        return self.get_text(self.INVITE_CODE)

    def click_copy(self):
        """点击复制按钮"""
        self.click_element(self.COPY_BUTTON)

    def click_share(self):
        """点击分享按钮"""
        self.click_element(self.SHARE_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_invite_page_displayed(self):
        """检查邀请页面是否显示"""
        return self.wait_for_element_visible(self.INVITE_TITLE)
