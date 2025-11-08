# Tab_mine.py
"""
我的标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabMinePage(BasePage):
    # 页面元素定位器
    MY_TIMBRE = (AppiumBy.ID, "iv_mine_timbre")
    POINTS = (AppiumBy.ID, "ll_points")
    SET = (AppiumBy.ID, "siv_mine_settings")
    AVATAR = (AppiumBy.ID, "iv_avatar")
    NICK_NAME = (AppiumBy.ID, "tv_nickname")
    INVITATION_LEVEL = (AppiumBy.ID, "tv_invitation_level")
    MEMBERSHIP_LEVELS = (AppiumBy.ID, "iv_vip_rights_interests")
    ACCOUNT_ID = (AppiumBy.ID, "tv_id")
    MEMBERSHIP_CARD = (AppiumBy.ID, "iv_vip_bg")
    MEMBERSHIP_VALIDITY = (AppiumBy.XPATH, "*//[@text='会员有效期']")
    RENEWAL = (AppiumBy.ID, "tv_activate")
    MY_ORDER = (AppiumBy.ID, "ll_my_order")
    MY_WALLET = (AppiumBy.ID, "ll_my_wallet")
    PICTURE_BOOK_COVER = (AppiumBy.ID, "siv_picture")
    PLAY_ICON = (AppiumBy.ID, "iv_play_animation")
    VIEWS = (AppiumBy.ID, "tv_browse")
    PICTURE_BOOK_TITLE = (AppiumBy.ID, "tv_title")
    GENERATION_TIME = (AppiumBy.ID, "tv_time")
    MENU = (AppiumBy.ID, "iv_menu")
    MORE_TITLES = (AppiumBy.ID, "tv_title")
    MORE_RENAME = (AppiumBy.XPATH, "*//[@text='修改']")
    MORE_SHARE = (AppiumBy.XPATH, "*//[@text='分享']")
    MORE_DELETE = (AppiumBy.XPATH, "*//[@text='删除']")
    GO_CUSTOMIZED_BOOK = (AppiumBy.ID, "tv_custom")

    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_mine(self):
        """切换到我的标签"""
        self.click_element(self.TAB_MINE)

    def get_nickname(self):
        """获取昵称"""
        return self.get_text(self.NICK_NAME)

    def is_invitation_level(self):
        """检查邀请等级是否显示"""
        return self.is_element_displayed(self.INVITATION_LEVEL)

    def is_membership_levels(self):
        """检查会员等级是否显示"""
        return self.is_element_displayed(self.MEMBERSHIP_LEVELS)

    def is_membership_validity_displayed(self):
        """检查会员有效期是否显示"""
        return self.is_element_displayed(self.MEMBERSHIP_VALIDITY)

    def is_more_displayed(self):
        """检查更多按钮是否显示"""
        return self.is_element_displayed(self.MORE_TITLES)

    def click_my_timbre(self):
        """点击我的音色"""
        self.click_element(self.MY_TIMBRE)

    def click_points(self):
        """点击积分按钮"""
        self.click_element(self.POINTS)

    def click_settings(self):
        """点击设置按钮"""
        self.click_element(self.SET)

    def click_avatar(self):
        """点击头像"""
        self.click_element(self.AVATAR)

    def click_nickname(self):
        """点击昵称"""
        self.click_element(self.NICK_NAME)

    def click_account_id(self):
        """点击账号ID"""
        self.click_element(self.ACCOUNT_ID)

    def click_membership_card(self):
        """点击会员卡"""
        self.click_element(self.MEMBERSHIP_CARD)

    def click_my_order(self):
        """点击我的订单"""
        self.click_element(self.MY_ORDER)

    def click_my_wallet(self):
        """点击我的钱包"""
        self.click_element(self.MY_WALLET)

    def click_picture_book_cover(self):
        """点击绘本封面"""
        self.click_element(self.PICTURE_BOOK_COVER)

    def click_menu(self):
        """点击菜单按钮"""
        self.click_element(self.MENU)

    def click_more_titles(self):
        """点击更多标题"""
        self.click_element(self.MORE_TITLES)

    def click_rename(self):
        """点击修改选项"""
        self.click_element(self.MORE_RENAME)

    def click_share(self):
        """点击分享选项"""
        self.click_element(self.MORE_SHARE)

    def click_delete(self):
        """点击删除选项"""
        self.click_element(self.MORE_DELETE)

    def click_go_customized_book(self):
        """点击去定制书"""
        self.click_element(self.GO_CUSTOMIZED_BOOK)

    def navigate_to_index(self):
        """切换到首页标签"""
        self.click_element(self.TAB_INDEX)

    def navigate_to_create(self):
        """切换到创作标签"""
        self.click_element(self.TAB_CREATE)

    def navigate_to_ability(self):
        """切换到能力标签"""
        self.click_element(self.TAB_ABILITY)

    def navigate_to_invitation(self):
        """切换到邀请标签"""
        self.click_element(self.TAB_INVITATION)



