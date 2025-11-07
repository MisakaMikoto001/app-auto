from src.pages.Start import StartPage
from src.pages.Pop_up_login import PopUpLoginPage
from src.pages.Tab_index import TabIndexPage
from src.pages.Tab_create import TabCreatePage
from src.pages.Tab_ablility import TabAbilityPage
from src.pages.Tab_invite import TabInvitePage
from src.pages.Tab_mine import TabMinePage


class LoginPopUpBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.popup_login_page = PopUpLoginPage(driver)
        self.start_page = StartPage(driver)
        self.tab_index_page = TabIndexPage(driver)
        self.tab_create_page = TabCreatePage(driver)
        self.tab_ability_page = TabAbilityPage(driver)
        self.tab_invite_page = TabInvitePage(driver)
        self.tab_mine_page = TabMinePage(driver)

    # 首页弹窗登录验证
    def index_popup_login(self):
        if self.popup_login_page.is_popup_displayed():
            self.popup_login_page.close_popup()

    # 创作页弹窗调起
    def create_popup_login(self):
        if self.popup_login_page.is_popup_displayed():
            # 点击横幅跳转
            self.tab_create_page.click_banner_jump()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击创作绘本封面
            self.tab_create_page.click_creative_picture_book()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击创作绘本标题
            self.tab_create_page.click_create_title()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击创作绘本描述
            self.tab_create_page.click_create_describe()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击去创作按钮
            self.tab_create_page.click_go_create_button()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击一键创作
            self.tab_create_page.click_one_click_creation()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 关闭最终的弹窗
            self.popup_login_page.close_popup()

    # 能力页弹窗调起
    def ability_popup_login(self):
        if self.popup_login_page.is_popup_displayed():
            # 点击轮播图
            self.tab_ability_page.click_carousel_chart()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击购买按钮
            self.tab_ability_page.click_ability_buy()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 点击封面
            self.tab_ability_page.click_ability_cover()
            if self.popup_login_page.is_popup_displayed():
                self.popup_login_page.close_popup()
                return

            # 关闭最终的弹窗
            self.popup_login_page.close_popup()
