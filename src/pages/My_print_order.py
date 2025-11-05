# My_print_order.py
"""
打印订单页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MyPrintOrderPage(BasePage):
    # 页面元素定位器
    ORDER_LIST = (AppiumBy.ID, "order_list_id")
    ORDER_ITEM = (AppiumBy.ID, "order_item_id")
    PRINT_BUTTON = (AppiumBy.ID, "print_button_id")
    ORDER_STATUS = (AppiumBy.ID, "order_status_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_order_list(self):
        """获取订单列表"""
        return self.find_elements(self.ORDER_LIST)

    def click_print_order(self, order_index=0):
        """点击打印订单"""
        orders = self.find_elements(self.ORDER_ITEM)
        if order_index < len(orders):
            orders[order_index].click()

    def get_order_status(self):
        """获取订单状态"""
        return self.get_text(self.ORDER_STATUS)

    def click_print(self):
        """点击打印按钮"""
        self.click_element(self.PRINT_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_order_displayed(self):
        """检查订单是否显示"""
        return self.wait_for_element_visible(self.ORDER_LIST)
