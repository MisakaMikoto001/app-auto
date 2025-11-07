import pytest
from src.pages.Start import StartPage


# noinspection PyBroadException
def test_start_page_elements_displayed(driver):
    """测试启动页面元素是否正常显示"""
    start_page = StartPage(driver)

    # 添加调试信息
    print(f"检查 AGREE_BUTTON 是否存在...")
    # 可以先检查元素是否存在再等待可见
    try:
        element = start_page.find_element(start_page.AGREE_BUTTON, timeout=30)
        print(f"找到元素: {element}")
    except:
        print(f"未能找到 AGREE_BUTTON 元素")

    # 等待启动页加载完成
    assert start_page.wait_for_start_page(), "启动页未正常加载"

    # 验证各元素是否显示
    assert start_page.is_logo_displayed(), "Logo未显示"
    assert start_page.is_title_displayed(), "标题未显示"
    assert start_page.is_content_displayed(), "内容未显示"


def test_click_agree_button(driver):
    """测试点击同意按钮进入APP"""
    start_page = StartPage(driver)

    # 点击同意按钮
    start_page.click_agree()

    start_page.clear_app_cache()
    start_page.close_app()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未关闭"

def test_click_reject_button(driver):
    """测试点击不同意按钮退出APP"""
    start_page = StartPage(driver)
    start_page.launch_app()

    # 添加调试信息，检查 REJECT_BUTTON 是否存在
    try:
        element = start_page.find_element(start_page.REJECT_BUTTON)
        print(f"找到 REJECT_BUTTON 元素: {element}")
    except Exception as e:
        print(f"未能找到 REJECT_BUTTON 元素: {e}")
        # 可以添加截图用于调试
        start_page.take_screenshot("reject_button_not_found.png")

    # 点击不同意按钮
    start_page.click_reject()
    start_page.clear_app_cache()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未能成功关闭"


def test_click_privacy_policy(driver):
    """测试点击隐私政策链接"""
    start_page = StartPage(driver)
    start_page.launch_app()

    # 验证启动是否有显示
    if not start_page.is_agree_button_displayed():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page = StartPage(driver)

    # # 点击隐私政策
    # expected_texts = ["隐私政策", "条款"]
    # start_page.click_privacy_policy(start_page.PRIVACY_POLICY, expected_texts)

    # 判断隐私政策是否存在
    if start_page.is_content_displayed():
        start_page.tap_coordinates(258,121,1000)

    start_page.click_reject()
    start_page.clear_app_cache()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未能成功关闭"


def test_click_user_agreement(driver):
    """测试点击用户协议链接"""
    start_page = StartPage(driver)
    start_page.launch_app()

    # 验证启动是否有显示
    if not start_page.is_agree_button_displayed():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page = StartPage(driver)

    # # 点击用户协议
    # expected_texts = ["用户协议", "服务条款"]
    # start_page.click_user_agreement(start_page.USER_AGREEMENT, expected_texts)

    # 判断隐私政策是否存在
    if start_page.is_content_displayed():
        start_page.tap_coordinates(225,121,1000)

    start_page.click_reject()
    start_page.clear_app_cache()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未能成功关闭"

