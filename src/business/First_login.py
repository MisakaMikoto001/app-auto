# First_login.py
"""
首次登录业务逻辑类
"""

from src.pages.Start import StartPageBusiness
from src.pages.Pop_up_login import PopUpLoginWeChatBusiness,PopUpLoginTelBusiness
from src.pages.Tab_create import TabCreatePage



class FirstLoginBusiness(StartPageBusiness, TabCreatePage, PopUpLoginWeChatBusiness, PopUpLoginTelBusiness):
    """首次登录业务逻辑类"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.start_page_business = StartPageBusiness(driver)
        self.popup_login_wechat_business = PopUpLoginWeChatBusiness(driver)
        self.popup_login_tel_business = PopUpLoginTelBusiness(driver)
        self.tab_create_page = TabCreatePage(driver)

    def login_process_with_wechat(self):
        """首次微信登录完整流程"""
        # 1. 启动APP并同意协议进入
        if self.start_page_business.is_agree_button_displayed():
            self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗
        self.tab_create_page.click_tab_mine()

        # 4. 检查弹窗是否显示
        if self.popup_login_wechat_business.is_popup_title_displayed():
            self.popup_login_wechat_business.login_with_wechat()
            assert self.popup_login_wechat_business.assert_toast_visible("没有安装微信"), "没有安装微信"
            return True
        else:
            print("login_process_with_wechat：登录弹窗未显示")
            return False

    def login_process_with_flash_test(self):
        """首次闪验登录完整流程"""
        # 1. 启动APP并同意协议进入
        if self.start_page_business.is_agree_button_displayed():
            self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗
        # self.tab_create_page.click_one_click_creation()
        self.tab_create_page.click_tab_mine()

        # 4. 检查弹窗是否显示
        if self.popup_login_tel_business.is_popup_title_displayed():
            self.popup_login_tel_business.login_with_flash_test()
            return True
        else:
            print("login_process_with_flash_test：登录弹窗未显示")
            return False

        # 5. 确认一键登录
        self.popup_login_tel_business.click_confirm_popup_agree()
        return self.popup_login_tel_business.is_confirm_popup_displayed()

    def first_login_process_with_phone(self,phone, code):
        """首次手机登录完整流程"""
        # 1. 启动APP并同意协议进入
        if self.start_page_business.is_agree_button_displayed():
            self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗
        if  self.tab_create_page.wait_for_element_visible(self.tab_create_page.TAB_MINE):
            self.tab_create_page.click_tab_mine()
        else:
            print("未找到TAB_MINE 元素")
            return False

        # 4. 检查弹窗是否显示
        if self.popup_login_wechat_business.is_popup_title_displayed():
            self.popup_login_tel_business.login_with_phone(phone, code)
            return True
        else:
            print("first_login_process_with_phone：登录弹窗未显示")
            return False

    def pop_up_wechat_closes(self):
        """关闭微信登录弹窗"""
        # 1. 启动APP并同意协议进入
        if self.start_page_business.is_agree_button_displayed():
            self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗
        # self.tab_create_page.click_one_click_creation()
        self.tab_create_page.click_tab_mine()

        # 4. 检查弹窗是否显示
        if self.popup_login_wechat_business.is_popup_title_displayed():
            self.popup_login_wechat_business.close_popup()
            return True
        else:
            print("pop_up_wechat_closes：登录弹窗未显示")
            return False

    def pop_up_phone_closes(self):
        """关闭手机登录弹窗"""
        # 1. 启动APP并同意协议进入
        if self.start_page_business.is_agree_button_displayed():
            self.start_page_business.start_page_get_in()

        # 2. 进入创作页
        self.tab_create_page.navigate_to_create()

        # 3. 触发登录弹窗
        self.tab_create_page.click_tab_mine()

        # 4. 检查弹窗是否显示
        if self.popup_login_wechat_business.is_popup_title_displayed():
            self.popup_login_tel_business.close_popup()
            return True
        else:
            print("pop_up_phone_closes：登录弹窗未显示")
            return False

