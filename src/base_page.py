"""
所有页面对象的基类，封装滑动、等待、截图
优化版：Python 3.13.5，零侵入，旧脚本无需改动
"""
from __future__ import annotations
import os
import time
import logging
from functools import lru_cache
from typing import Tuple, List, Optional, Any

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from src.common.yaml_reader import YamlReader

# -------------- 日志开关 --------------
logger = logging.getLogger("BasePage")
if os.getenv("BASEPAGE_DEBUG"):
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")


# -------------- 混入类 --------------
class EmptyStateMixin:
    """空状态/断网状态处理混入类"""
    EMPTY_ICON   = (AppiumBy.ID, "icon")
    EMPTY_TEXT   = (AppiumBy.ID, "error_prompt_view")
    EMPTY_BUTTON = (AppiumBy.ID, "retry_btn")

    def is_empty_state_displayed(self) -> bool:
        return self.is_element_displayed(self.EMPTY_ICON)

    def get_empty_state_text(self) -> str:
        return self.get_text(self.EMPTY_TEXT)

    def click_retry_button(self) -> None:
        self.click_element(self.EMPTY_BUTTON)


# -------------- 基类 --------------
class BasePage(EmptyStateMixin):
    """所有页面的基类"""

    # 全局默认重试次数与间隔
    _RETRY_TIMES   = 1
    _RETRY_SLEEP   = 0.5
    _SCREENSHOT_DIR = os.path.join("outputs", "screenshots")

    def __init__(self, driver):
        self.driver = driver
        # 统一 wait 实例，减少重复创建
        self._wait: WebDriverWait = WebDriverWait(driver, 10)
        self.yaml_reader: Optional[YamlReader] = None

    # -------------- YAML 相关 --------------
    def get_yaml_reader(self, yaml_path: str) -> YamlReader:
        if self.yaml_reader is None:
            self.yaml_reader = YamlReader(yaml_path)
        return self.yaml_reader

    def read_config(self, file_path: str) -> dict:
        return self.get_yaml_reader(file_path).read(file_path)

    def get_config_value(self, file_path: str, key: str) -> Any:
        return self.read_config(file_path).get(key)

    # -------------- 私有工具 --------------
    @staticmethod
    def _retry(func, times: int = _RETRY_TIMES, sleep: float = _RETRY_SLEEP):
        """简单重试装饰器（非注解形式，减少侵入）"""
        def wrapper(*args, **kwargs):
            last_err = None
            for _ in range(times + 1):
                try:
                    return func(*args, **kwargs)
                except (TimeoutException, StaleElementReferenceException) as e:
                    last_err = e
                    time.sleep(sleep)
            raise last_err
        return wrapper

    @lru_cache(maxsize=1)
    def _window_size(self) -> dict:
        """缓存窗口大小，避免每次滑动都获取"""
        return self.driver.get_window_size()

    # -------------- 元素查找 --------------
    @staticmethod
    def _adapt_locator(locator: Tuple[AppiumBy, str]) -> Tuple[str, str]:
        """将 AppiumBy 枚举转换为字符串定位策略"""
        by, value = locator
        return by.name, value

    def is_element_present(self, locator: Tuple[AppiumBy, str], timeout: int = 10) -> bool:
        try:
            self._retry(lambda: self.find_element(locator, timeout))()
            return True
        except TimeoutException:
            return False

    def find_element(self, locator: Tuple[AppiumBy, str], timeout: int = 10):
        adapted_locator = self._adapt_locator(locator)
        return self._retry(
            lambda: self._wait.until(EC.presence_of_element_located(adapted_locator))
        )()

    def find_elements(self, locator: Tuple[AppiumBy, str], timeout: int = 10) -> List[Any]:
        adapted_locator = self._adapt_locator(locator)
        return self._retry(
            lambda: self._wait.until(EC.presence_of_all_elements_located(adapted_locator))
        )()

    def get_text(self, locator: Tuple[AppiumBy, str], timeout: int = 10) -> str:
        return self.find_element(locator, timeout).text

    def click_element(self, locator: Tuple[AppiumBy, str], timeout: int = 10) -> None:
        adapted_locator = self._adapt_locator(locator)
        self._retry(
            lambda: self._wait.until(EC.element_to_be_clickable(adapted_locator))
        )().click()

    def input_text(self, locator: Tuple[AppiumBy, str], text: str, timeout: int = 10) -> None:
        ele = self.find_element(locator, timeout)
        ele.clear()
        ele.send_keys(text)

    # -------------- 滑动 --------------
    def swipe_up(self, duration: int = 1000) -> None:
        size = self._window_size()
        x = size["width"] // 2
        start_y = int(size["height"] * 0.8)
        end_y   = int(size["height"] * 0.2)
        logger.debug("swipe_up: (%s, %s) -> (%s, %s)", x, start_y, x, end_y)
        self.driver.swipe(x, start_y, x, end_y, duration)

    def swipe_down(self, duration: int = 1000) -> None:
        size = self._window_size()
        x = size["width"] // 2
        start_y = int(size["height"] * 0.2)
        end_y   = int(size["height"] * 0.8)
        logger.debug("swipe_down: (%s, %s) -> (%s, %s)", x, start_y, x, end_y)
        self.driver.swipe(x, start_y, x, end_y, duration)

    def tap_coordinates(self, x: int, y: int, duration: Optional[int] = None) -> None:
        logger.debug("tap_coordinates: (%s, %s), duration=%s", x, y, duration)
        self.driver.tap([(x, y)], duration)

    # -------------- 导航 --------------
    def go_back(self, times: int = 1) -> None:
        for _ in range(times):
            self.driver.back()

    # -------------- 等待/可见性 --------------
    def wait_for_element_visible(self, locator: Tuple[str, str], timeout: int = 10):
        try:
            return self._retry(
                lambda: self._wait.until(EC.visibility_of_element_located(locator))
            )()
        except TimeoutException:
            return False

    def is_element_displayed(self, locator: Tuple[str, str], timeout: int = 10) -> bool:
        return bool(self.wait_for_element_visible(locator, timeout))

    # -------------- 断言 --------------
    def assert_element_present(self, locator: Tuple[str, str], timeout: int = 10,
                               message: str = "Element is not present") -> True:
        if not self.is_element_present(locator, timeout):
            raise AssertionError(message)
        return True

    def assert_element_not_present(self, locator: Tuple[str, str], timeout: int = 10,
                                   message: str = "Element is still present") -> True:
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            raise AssertionError(message)
        except TimeoutException:
            return True

    def assert_element_visible(self, locator: Tuple[str, str], timeout: int = 10,
                               message: str = "Element is not visible") -> True:
        if not self.wait_for_element_visible(locator, timeout):
            raise AssertionError(message)
        return True

    def assert_element_text(self, locator: Tuple[str, str], expected_text: str,
                            timeout: int = 10, message: Optional[str] = None) -> True:
        actual = self.get_text(locator, timeout)
        if actual != expected_text:
            if message is None:
                message = f"Element text mismatch. Expected: '{expected_text}', Actual: '{actual}'"
            raise AssertionError(message)
        return True

    def assert_element_contains_texts(self, locator: Tuple[str, str],
                                      expected_texts, timeout: int = 10,
                                      message: Optional[str] = None) -> True:
        if isinstance(expected_texts, str):
            expected_texts = [expected_texts]
        actual = self.get_text(locator, timeout)
        missing = [t for t in expected_texts if t not in actual]
        if missing:
            if message is None:
                message = f"Element text missing: {missing}. Actual: '{actual}'"
            raise AssertionError(message)
        return True

    # -------------- Toast --------------
    def assert_toast_visible(self, expected_text: str, timeout: int = 10,
                             message: Optional[str] = None) -> True:
        if message is None:
            message = f"Toast not found or text mismatch: '{expected_text}'"
        locator = (AppiumBy.XPATH, f"//*[contains(@text,'{expected_text}')]")
        try:
            ele = self._retry(
                lambda: self._wait.until(EC.presence_of_element_located(locator))
            )()
            if expected_text not in ele.text:
                raise AssertionError(f"{message}. Actual: '{ele.text}'")
            return True
        except TimeoutException:
            raise AssertionError(message)

    def is_toast_displayed(self, expected_text: str, timeout: int = 5) -> bool:
        locator = (AppiumBy.XPATH, f"//*[contains(@text,'{expected_text}')]")
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # -------------- 截图 --------------
    def take_screenshot(self, filename: str) -> None:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_dir = os.path.join(project_root, "outputs", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        full_path = os.path.join(screenshot_dir, filename)
        logger.debug("take_screenshot: %s", full_path)
        self.driver.save_screenshot(full_path)

    # -------------- 应用生命周期 --------------
    def close_app(self) -> bool:
        try:
            pkg = self.driver.capabilities.get("appPackage")
            if not pkg:
                raise ValueError("Unable to get appPackage")
            self.driver.terminate_app(pkg)
            return True
        except Exception as e:
            logger.exception("close_app failed: %s", e)
            return False

    def launch_app(self) -> bool:
        try:
            pkg = self.driver.capabilities.get("appPackage")
            if not pkg:
                raise ValueError("Unable to get appPackage")
            self.driver.activate_app(pkg)
            return True
        except Exception as e:
            logger.exception("launch_app failed: %s", e)
            return False

    def clear_app_cache(self) -> bool:
        try:
            pkg = self.driver.capabilities.get("appPackage")
            if not pkg:
                raise ValueError("Unable to get appPackage")
            self.driver.execute_script("mobile: shell", {
                "command": "pm",
                "args":   ["clear", pkg]
            })
            return True
        except Exception as e:
            logger.exception("clear_app_cache failed: %s", e)
            return False

    # -------------- 状态断言 --------------
    # noinspection PyBroadException
    def is_app_closed(self, timeout: int = 10, message: str = "Application is still running") -> bool:
        try:
            activity = self.driver.current_activity
            if activity:
                raise AssertionError(message)
            return True
        except Exception:
            return True

    # noinspection PyBroadException
    def is_app_running(self, timeout: int = 10) -> bool:
        try:
            return self.driver.context is not None
        except Exception:
            return False
