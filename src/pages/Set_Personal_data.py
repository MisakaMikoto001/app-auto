# Set_Personal_data.py
"""
个人资料设置页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SetPersonalDataPage(BasePage):
    # 页面元素定位器
    PERSONAL_DATA_TITLE = (AppiumBy.ID, "personal_data_title_id")
    NICKNAME_INPUT = (AppiumBy.ID, "nickname_input_id")
    PHONE_NUMBER = (AppiumBy.ID, "phone_number_id")
    EMAIL_INPUT = (AppiumBy.ID, "email_input_id")
    SAVE_BUTTON = (AppiumBy.ID, "save_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def input_nickname(self, nickname):
        """输入昵称"""
        self.input_text(self.NICKNAME_INPUT, nickname)

    def input_email(self, email):
        """输入邮箱"""
        self.input_text(self.EMAIL_INPUT, email)

    def get_phone_number(self):
        """获取手机号码"""
        return self.get_text(self.PHONE_NUMBER)

    def click_save(self):
        """点击保存按钮"""
        self.click_element(self.SAVE_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def update_personal_data(self, nickname, email):
        """更新个人资料完整流程"""
        self.input_nickname(nickname)
        self.input_email(email)
        self.click_save()

    def is_personal_data_page_displayed(self):
        """检查个人资料页面是否显示"""
        return self.wait_for_element_visible(self.PERSONAL_DATA_TITLE)
