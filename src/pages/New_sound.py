# New_sound.py
"""
新建音频页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class NewSoundPage(BasePage):
    # 页面元素定位器
    RECORD_BUTTON = (AppiumBy.ID, "record_button_id")
    PLAY_BUTTON = (AppiumBy.ID, "play_button_id")
    STOP_BUTTON = (AppiumBy.ID, "stop_button_id")
    SAVE_BUTTON = (AppiumBy.ID, "save_button_id")
    AUDIO_TITLE_INPUT = (AppiumBy.ID, "audio_title_input_id")
    BACK_BUTTON = (AppiumBy.ID, "back_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def click_record(self):
        """点击录音按钮"""
        self.click_element(self.RECORD_BUTTON)

    def click_play(self):
        """点击播放按钮"""
        self.click_element(self.PLAY_BUTTON)

    def click_stop(self):
        """点击停止按钮"""
        self.click_element(self.STOP_BUTTON)

    def click_save(self):
        """点击保存按钮"""
        self.click_element(self.SAVE_BUTTON)

    def input_audio_title(self, title):
        """输入音频标题"""
        self.input_text(self.AUDIO_TITLE_INPUT, title)

    def go_back(self):
        """返回上一页"""
        self.click_element(self.BACK_BUTTON)

    def record_audio(self, title):
        """录制音频完整流程"""
        self.click_record()
        # 这里可以添加录制时长的处理
        self.click_stop()
        self.input_audio_title(title)
        self.click_save()
