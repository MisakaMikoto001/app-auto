"""
登录业务流程类
处理从应用启动到登录完成的完整业务流程
"""

from src.pages.Start import StartPage
from src.pages.Pop_up_login import PopUpLoginPage


class LoginBusiness:
    """登录业务流程类"""

    def __init__(self, driver):
        """
        初始化登录业务流程

        Args:
            driver: Appium WebDriver实例
        """
        self.driver = driver
        self.start_page = StartPage(driver)
        self.popup_login_page = PopUpLoginPage(driver)

    def bring_up_the_login_pop_up(self):
        """
        处理启动页面并显示登录弹窗

        Returns:
            bool: 登录弹窗已显示返回True
        """
        return self.start_page.wait_for_start_page()

    def first_launch_and_login(self, phone_number, verification_code):
        """
        首次启动应用并登录

        Args:
            phone_number (str): 手机号码
            verification_code (str): 验证码

        Returns:
            bool: 登录成功返回True
        """
        # 处理启动页面
        if self.start_page.wait_for_start_page():
            self.start_page.click_agree()

        # 等待登录弹窗出现
        if self.popup_login_page.is_popup_displayed():
            # 点击手机登录
            self.popup_login_page.click_login_tel()

            # 确保手机登录界面已显示
            if self.popup_login_page.is_popup_tel_displayed():
                # 输入手机号和验证码
                self.popup_login_page.input_user_tel(phone_number)
                self.popup_login_page.input_user_code(verification_code)

                # 勾选协议
                self.popup_login_page.click_check_box()

                # 点击登录
                self.popup_login_page.click_login()

                # 验证登录成功
                return self.popup_login_page.is_toast_displayed("登录成功")

        return False

    def login_with_popup(self, phone_number, verification_code):
        """
        通过弹窗登录（非首次启动）

        Args:
            phone_number (str): 手机号码
            verification_code (str): 验证码

        Returns:
            bool: 登录成功返回True
        """
        # 确保登录弹窗已显示
        if self.popup_login_page.is_popup_displayed():
            # 点击手机登录
            self.popup_login_page.click_login_tel()

            # 确保手机登录界面已显示
            if self.popup_login_page.is_popup_tel_displayed():
                # 输入手机号和验证码
                self.popup_login_page.input_user_tel(phone_number)
                self.popup_login_page.input_user_code(verification_code)

                # 勾选协议
                self.popup_login_page.click_check_box()

                # 点击登录
                self.popup_login_page.click_login()

                # 验证登录成功
                return self.popup_login_page.is_toast_displayed("登录成功")

        return False

    def wechat_login(self):
        """
        微信登录流程

        Returns:
            bool: 登录流程启动成功返回True
        """
        # 确保登录弹窗已显示
        if self.popup_login_page.is_popup_displayed():
            # 点击微信登录
            self.popup_login_page.click_login_wechat()
            return True

        return False

    def logout(self):
        """
        退出登录

        Returns:
            bool: 退出成功返回True
        """
        try:
            # 启动应用
            self.popup_login_page.launch_app()

            # 点击我的页面
            self.popup_login_page.click_element(("id", "tab_mine"))

            # 点击设置
            self.popup_login_page.click_element(("id", "siv_mine_settings"))

            # 点击退出登录
            self.popup_login_page.click_element(("id", "stv_log_out"))

            # 确认退出
            self.popup_login_page.click_element(("id", "confirm"))

            # 关闭应用
            self.popup_login_page.close_app()

            return True
        except Exception as e:
            print(f"退出登录失败: {e}")
            return False
