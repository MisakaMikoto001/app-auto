# My_tamber.py
"""
我的模板页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MyTamberPage(BasePage):
    # 页面元素定位器
    TEMPLATE_LIST = (AppiumBy.ID, "template_list_id")
    TEMPLATE_ITEM = (AppiumBy.ID, "template_item_id")
    CREATE_TEMPLATE_BUTTON = (AppiumBy.ID, "create_template_button_id")
    DELETE_TEMPLATE_BUTTON = (AppiumBy.ID, "delete_template_button_id")
    EDIT_TEMPLATE_BUTTON = (AppiumBy.ID, "edit_template_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_template_list(self):
        """获取模板列表"""
        return self.find_elements(self.TEMPLATE_LIST)

    def click_template(self, template_index=0):
        """点击指定模板"""
        templates = self.find_elements(self.TEMPLATE_ITEM)
        if template_index < len(templates):
            templates[template_index].click()

    def click_create_template(self):
        """点击创建模板按钮"""
        self.click_element(self.CREATE_TEMPLATE_BUTTON)

    def click_delete_template(self):
        """点击删除模板按钮"""
        self.click_element(self.DELETE_TEMPLATE_BUTTON)

    def click_edit_template(self):
        """点击编辑模板按钮"""
        self.click_element(self.EDIT_TEMPLATE_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_template_page_displayed(self):
        """检查模板页面是否显示"""
        return self.wait_for_element_visible(self.TEMPLATE_LIST)
