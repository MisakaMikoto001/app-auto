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

    def __init__(self, driver):
        super().__init__(driver)

    def get_user_name(self):
        """获取用户名"""
        return self.get_text(self.USER_NAME)

    def click_settings(self):
        """点击设置按钮"""
        self.click_element(self.SETTINGS_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_mine_page_displayed(self):
        """检查我的页面是否显示"""
        return self.wait_for_element_visible(self.MINE_TITLE)
