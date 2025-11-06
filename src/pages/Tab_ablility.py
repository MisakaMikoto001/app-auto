# Tab_ablility.py
"""
能力标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabAbilityPage(BasePage):
    # 页面元素定位器
    CAROUSEL_CHART = (AppiumBy.ID, "vip_main")
    ABILITY_BUY = (AppiumBy.ID, "iv_buy")
    ABILITY_COVER = (AppiumBy.ID, "iv_cover")
    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")

    def __init__(self, driver):
        super().__init__(driver)

