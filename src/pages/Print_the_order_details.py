# Print_the_order_details.py
"""
打印订单详情页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PrintTheOrderDetailsPage(BasePage):
    # 页面元素定位器
    ORDER_NUMBER = (AppiumBy.ID, "order_number_id")
    ORDER_STATUS = (AppiumBy.ID, "order_status_id")
    PRODUCT_INFO = (AppiumBy.ID, "product_info_id")
    PRINT_BUTTON = (AppiumBy.ID, "print_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_order_number(self):
        """获取订单号"""
        return self.get_text(self.ORDER_NUMBER)

    def get_order_status(self):
        """获取订单状态"""
        return self.get_text(self.ORDER_STATUS)

    def get_product_info(self):
        """获取产品信息"""
        return self.get_text(self.PRODUCT_INFO)

    def click_print(self):
        """点击打印按钮"""
        self.click_element(self.PRINT_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_order_details_page_displayed(self):
        """检查订单详情页面是否显示"""
        return self.wait_for_element_visible(self.ORDER_NUMBER)
