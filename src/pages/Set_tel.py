# Set_tel.py
"""
电话设置页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SetTelPage(BasePage):
    # 页面元素定位器
    TEL_TITLE = (AppiumBy.ID, "tel_title_id")
    TEL_INPUT = (AppiumBy.ID, "tel_input_id")
    SAVE_BUTTON = (AppiumBy.ID, "save_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_tel_number(self, tel_number):
        """输入电话号码"""
        self.input_text(self.TEL_INPUT, tel_number)

    def click_save(self):
        """点击保存按钮"""
        self.click_element(self.SAVE_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def update_tel_number(self, tel_number):
        """更新电话号码完整流程"""
        self.input_tel_number(tel_number)
        self.click_save()

    def is_tel_page_displayed(self):
        """检查电话设置页面是否显示"""
        return self.wait_for_element_visible(self.TEL_TITLE)
