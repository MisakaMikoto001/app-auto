# Pop_up_dubbing.py
"""
弹窗配音页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpDubbingPage(BasePage):
    # 页面元素定位器
    DUBBING_TITLE = (AppiumBy.ID, "dubbing_title_id")
    RECORD_BUTTON = (AppiumBy.ID, "record_button_id")
    PLAY_BUTTON = (AppiumBy.ID, "play_button_id")
    STOP_BUTTON = (AppiumBy.ID, "stop_button_id")
    SAVE_BUTTON = (AppiumBy.ID, "save_button_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

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

    def click_cancel(self):
        """点击取消按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_dubbing_popup_displayed(self):
        """检查配音弹窗是否显示"""
        return self.wait_for_element_visible(self.DUBBING_TITLE)
