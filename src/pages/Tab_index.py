# Tab_index.py
"""
首页标签页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class TabIndexPage(BasePage):
    # 页面元素定位器
    INDEX_TITLE = (AppiumBy.ID, "index_title_id")
    SEARCH_INPUT = (AppiumBy.ID, "search_input_id")
    BANNER_IMAGE = (AppiumBy.ID, "banner_image_id")
    MENU_LIST = (AppiumBy.ID, "menu_list_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_index_title(self):
        """获取首页标题"""
        return self.get_text(self.INDEX_TITLE)

    def input_search_keyword(self, keyword):
        """输入搜索关键词"""
        self.input_text(self.SEARCH_INPUT, keyword)

    def click_search(self):
        """点击搜索（通常在输入后按回车或点击搜索图标）"""
        # 根据具体实现可能需要特殊处理
        pass

    def is_banner_displayed(self):
        """检查横幅图片是否显示"""
        return self.wait_for_element_visible(self.BANNER_IMAGE)

    def get_menu_list(self):
        """获取菜单列表"""
        return self.find_elements(self.MENU_LIST)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_index_page_displayed(self):
        """检查首页是否显示"""
        return self.wait_for_element_visible(self.INDEX_TITLE)
