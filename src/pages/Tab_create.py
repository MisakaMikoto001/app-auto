# Tab_create.py
"""
创建标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabCreatePage(BasePage):
    # 页面元素定位器
    CREATE_TITLE = (AppiumBy.XPATH, "//*[@text='创作绘本']")
    BANNER_JUMP = (AppiumBy.ID, "banner_view_pager")
    CREATIVE_PICTURE_BOOK_COVER = (AppiumBy.ID, "iv_cover")
    CREATIVE_PICTURE_BOOK_TITLES = (AppiumBy.ID, "tv_title")
    CREATIVE_PICTURE_BOOK_DESCRIBE = (AppiumBy.ID, "tv_describe")
    GO_CREATE_BUTTON = (AppiumBy.ID, "button_to_make")
    ONE_CLICK_CREATION = (AppiumBy.ID, "mfl_create")
    TAB_INDEX = (AppiumBy.ID, "tab_index")
    TAB_CREATE = (AppiumBy.ID, "tab_create")
    TAB_ABILITY = (AppiumBy.ID, "tab_ability")
    TAB_INVITATION = (AppiumBy.ID, "tab_invitation")
    TAB_MINE = (AppiumBy.ID, "tab_mine")
    

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_create(self):
        """切换到创作标签"""
        self.click_element(self.TAB_CREATE)

    def get_create_title(self):
        """获取创作绘本标题"""
        return self.find_element(*self.CREATE_TITLE)

    def get_picture_book_title(self):
        """获取绘本标题"""
        return self.find_element(*self.CREATIVE_PICTURE_BOOK_TITLES)

    def get_picture_book_describe(self):
        """获取绘本描述"""
        return self.find_element(*self.CREATIVE_PICTURE_BOOK_DESCRIBE)

    def click_banner_jump(self):
        """点击横幅跳转"""
        self.click_element(*self.BANNER_JUMP)

    def click_creative_picture_book(self):
        """点击创作绘本封面"""
        self.click_element(*self.CREATIVE_PICTURE_BOOK_COVER)

    def click_create_title(self):
        """点击绘本标题"""
        self.click_element(*self.CREATIVE_PICTURE_BOOK_TITLES)

    def click_create_describe(self):
        """点击绘本描述"""
        self.click_element(*self.CREATIVE_PICTURE_BOOK_DESCRIBE)

    def click_go_create_button(self):
        """点击去创作按钮"""
        self.click_element(*self.GO_CREATE_BUTTON)

    def click_one_click_creation(self):
        """点击一键创作"""
        self.click_element(*self.ONE_CLICK_CREATION)

    def click_tab_index(self):
        """点击首页标签"""
        self.click_element(*self.TAB_INDEX)

    def click_tab_create(self):
        """点击创作标签"""
        self.click_element(*self.TAB_CREATE)

    def click_tab_ability(self):
        """点击能力标签"""
        self.click_element(*self.TAB_ABILITY)

    def click_tab_invitation(self):
        """点击邀请标签"""
        self.click_element(*self.TAB_INVITATION)

    def click_tab_mine(self):
        """点击我的标签"""
        self.click_element(*self.TAB_MINE)
