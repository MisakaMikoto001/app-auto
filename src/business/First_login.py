# First_login.py
"""
首次登录业务逻辑类
"""

from src.pages.Start import StartPageBusiness
from src.pages.Pop_up_login import PopUpLoginBusiness
from src.pages.Tab_create import TabCreatePage


class FirstLoginBusiness:
    """首次登录业务逻辑类"""

    def __init__(self, driver):
        self.driver = driver
        self.start_page_business = StartPageBusiness(driver)
        self.popup_login_page = PopUpLoginBusiness(driver)
        self.tab_create_page = TabCreatePage(driver)

    def first_login_process_with_phone(self,phone, code):
        """首次手机登录完整流程"""
        # 1. 启动APP并同意协议进入
        self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗（点击一键创作）
        self.tab_create_page.click_one_click_creation()

        # 4. 检查弹窗是否显示
        if self.popup_login_page.is_popup_displayed():
            print("登录弹窗已显示")
            self.popup_login_page.login_with_phone(phone, code)
            return True
        else:
            print("登录弹窗未显示")
            return False

    def first_login_process_with_wechat(self):
        """首次微信登录完整流程"""
        # 1. 启动APP并同意协议进入
        self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗（点击一键创作）
        self.tab_create_page.click_one_click_creation()

        # 4. 检查弹窗是否显示
        if self.popup_login_page.is_popup_displayed():
            print("登录弹窗已显示")
            self.popup_login_page.login_with_wechat()
            return True
        else:
            print("登录弹窗未显示")
            return False
