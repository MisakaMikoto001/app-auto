# Points_breakdown.py
"""
积分明细页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PointsBreakdownPage(BasePage):
    # 页面元素定位器
    POINTS_BALANCE = (AppiumBy.ID, "points_balance_id")
    POINTS_LIST = (AppiumBy.ID, "points_list_id")
    POINTS_ITEM = (AppiumBy.ID, "points_item_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_points_balance(self):
        """获取积分余额"""
        return self.get_text(self.POINTS_BALANCE)

    def get_points_list(self):
        """获取积分明细列表"""
        return self.find_elements(self.POINTS_LIST)

    def get_points_item(self, index=0):
        """获取指定积分项"""
        items = self.find_elements(self.POINTS_ITEM)
        if index < len(items):
            return items[index]
        return None

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_points_page_displayed(self):
        """检查积分页面是否显示"""
        return self.wait_for_element_visible(self.POINTS_BALANCE)
