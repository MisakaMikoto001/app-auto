# Tab_ablility.py
"""
能力标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabAbilityPage(BasePage):
    # 页面元素定位器
    ABILITY_TITLE = (AppiumBy.ID, "ability_title_id")
    ABILITY_LIST = (AppiumBy.ID, "ability_list_id")
    ABILITY_ITEM = (AppiumBy.ID, "ability_item_id")
    ADD_ABILITY_BUTTON = (AppiumBy.ID, "add_ability_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_ability_title(self):
        """获取能力标签页面标题"""
        return self.get_text(self.ABILITY_TITLE)

    def get_ability_list(self):
        """获取能力标签列表"""
        return self.find_elements(self.ABILITY_LIST)

    def click_ability(self, ability_index=0):
        """点击指定能力标签"""
        abilities = self.find_elements(self.ABILITY_ITEM)
        if ability_index < len(abilities):
            abilities[ability_index].click()

    def click_add_ability(self):
        """点击添加能力标签按钮"""
        self.click_element(self.ADD_ABILITY_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_ability_page_displayed(self):
        """检查能力标签页面是否显示"""
        return self.wait_for_element_visible(self.ABILITY_TITLE)
