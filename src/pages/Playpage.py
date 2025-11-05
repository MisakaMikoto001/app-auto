# Playpage.py
"""
播放页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PlayPage(BasePage):
    # 页面元素定位器
    PLAY_BUTTON = (AppiumBy.ID, "play_button_id")
    PAUSE_BUTTON = (AppiumBy.ID, "pause_button_id")
    STOP_BUTTON = (AppiumBy.ID, "stop_button_id")
    NEXT_BUTTON = (AppiumBy.ID, "next_button_id")
    PREVIOUS_BUTTON = (AppiumBy.ID, "previous_button_id")
    PROGRESS_BAR = (AppiumBy.ID, "progress_bar_id")
    VOLUME_SLIDER = (AppiumBy.ID, "volume_slider_id")
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

    def click_next(self):
        """点击下一曲按钮"""
        self.click_element(self.NEXT_BUTTON)

    def click_previous(self):
        """点击上一曲按钮"""
        self.click_element(self.PREVIOUS_BUTTON)

    def adjust_volume(self, level):
        """调整音量"""
        self.input_text(self.VOLUME_SLIDER, level)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def is_playing(self):
        """检查是否正在播放"""
        return self.wait_for_element_visible(self.PAUSE_BUTTON)
