# Pop_up_baby_information.py
"""
弹窗宝宝信息页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpBabyInformationPage(BasePage):
    # 页面元素定位器
    BABY_NAME_INPUT = (AppiumBy.ID, "baby_name_input_id")
    BABY_AGE_INPUT = (AppiumBy.ID, "baby_age_input_id")
    BABY_GENDER_SELECTOR = (AppiumBy.ID, "baby_gender_selector_id")
    CONFIRM_BUTTON = (AppiumBy.ID, "confirm_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_baby_name(self, name):
        """输入宝宝姓名"""
        self.input_text(self.BABY_NAME_INPUT, name)

    def input_baby_age(self, age):
        """输入宝宝年龄"""
        self.input_text(self.BABY_AGE_INPUT, age)

    def select_baby_gender(self, gender):
        """选择宝宝性别"""
        self.click_element(self.BABY_GENDER_SELECTOR)
        # 根据具体实现选择性别选项

    def click_confirm(self):
        """点击确认按钮"""
        self.click_element(self.CONFIRM_BUTTON)

    def click_cancel(self):
        """点击取消按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def fill_baby_information(self, name, age, gender):
        """填写宝宝信息完整流程"""
        self.input_baby_name(name)
        self.input_baby_age(age)
        self.select_baby_gender(gender)
        self.click_confirm()
