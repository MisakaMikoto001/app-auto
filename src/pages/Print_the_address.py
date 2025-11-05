# Print_the_address.py
"""
打印地址页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PrintTheAddressPage(BasePage):
    # 页面元素定位器
    ADDRESS_TITLE = (AppiumBy.ID, "address_title_id")
    ADDRESS_LIST = (AppiumBy.ID, "address_list_id")
    ADD_ADDRESS_BUTTON = (AppiumBy.ID, "add_address_button_id")
    EDIT_ADDRESS_BUTTON = (AppiumBy.ID, "edit_address_button_id")
    DELETE_ADDRESS_BUTTON = (AppiumBy.ID, "delete_address_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_address_title(self):
        """获取地址页面标题"""
        return self.get_text(self.ADDRESS_TITLE)

    def get_address_list(self):
        """获取地址列表"""
        return self.find_elements(self.ADDRESS_LIST)

    def click_add_address(self):
        """点击添加地址按钮"""
        self.click_element(self.ADD_ADDRESS_BUTTON)

    def click_edit_address(self):
        """点击编辑地址按钮"""
        self.click_element(self.EDIT_ADDRESS_BUTTON)

    def click_delete_address(self):
        """点击删除地址按钮"""
        self.click_element(self.DELETE_ADDRESS_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_address_page_displayed(self):
        """检查地址页面是否显示"""
        return self.wait_for_element_visible(self.ADDRESS_TITLE)
