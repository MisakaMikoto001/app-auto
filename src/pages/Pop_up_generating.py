# Pop_up_generating.py
"""
弹窗生成中页面对象类
"""

from src.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PopUpGeneratingPage(BasePage):
    # 页面元素定位器
    GENERATING_TITLE = (AppiumBy.ID, "generating_title_id")
    PROGRESS_BAR = (AppiumBy.ID, "progress_bar_id")
    CANCEL_BUTTON = (AppiumBy.ID, "cancel_button_id")
    CLOSE_BUTTON = (AppiumBy.ID, "close_button_id")

    def __init__(self, driver):
        super().__init__(driver)

    def get_generating_title(self):
        """获取生成中弹窗标题"""
        return self.get_text(self.GENERATING_TITLE)

    def click_cancel(self):
        """点击取消按钮"""
        self.click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        """关闭弹窗"""
        self.click_element(self.CLOSE_BUTTON)

    def is_generating_popup_displayed(self):
        """检查生成中弹窗是否显示"""
        return self.wait_for_element_visible(self.GENERATING_TITLE)

    def wait_for_generation_complete(self, timeout=60):
        """等待生成完成"""
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(self.GENERATING_TITLE)
            )
            return True
        except TimeoutException:
            return False
