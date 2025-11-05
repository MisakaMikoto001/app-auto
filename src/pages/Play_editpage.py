# Play_editpage.py
"""
播放编辑页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PlayEditPage(BasePage):
    # 页面元素定位器
    PLAY_BUTTON = (AppiumBy.ID, "play_button_id")
    PAUSE_BUTTON = (AppiumBy.ID, "pause_button_id")
    STOP_BUTTON = (AppiumBy.ID, "stop_button_id")
    SEEK_BAR = (AppiumBy.ID, "seek_bar_id")
    VOLUME_CONTROL = (AppiumBy.ID, "volume_control_id")
    SAVE_BUTTON = (AppiumBy.ID, "save_button_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def click_play(self):
        """点击播放按钮"""
        self.click_element(self.PLAY_BUTTON)

    def click_pause(self):
        """点击暂停按钮"""
        self.click_element(self.PAUSE_BUTTON)

    def click_stop(self):
        """点击停止按钮"""
        self.click_element(self.STOP_BUTTON)

    def adjust_seek_bar(self, position):
        """调整播放进度条"""
        # 这里可以实现具体的拖拽逻辑
        pass

    def adjust_volume(self, volume_level):
        """调整音量"""
        # 实现音量调节逻辑
        pass

    def click_save(self):
        """点击保存按钮"""
        self.click_element(self.SAVE_BUTTON)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_play_edit_page_displayed(self):
        """检查播放编辑页面是否显示"""
        return self.wait_for_element_visible(self.PLAY_BUTTON)
