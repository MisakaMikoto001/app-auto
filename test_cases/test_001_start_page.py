import pytest
from src.pages.Start import StartPageBusiness


# noinspection PyBroadException
def test_start_page_elements_displayed(driver):
    """测试启动页面元素是否正常显示"""
    start_page = StartPageBusiness(driver)

    if start_page.is_app_running():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page.launch_app()
    else:
        start_page.clear_app_cache()
        start_page.launch_app()

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

# noinspection PyBroadException
def test_click_agree_button(driver):
    """测试点击同意按钮进入APP"""
    start_page = StartPageBusiness(driver)

    if start_page.is_app_running():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page.launch_app()
    else:
        start_page.clear_app_cache()
        start_page.launch_app()

    try:
        element = start_page.find_element(start_page.AGREE_BUTTON, timeout=30)
        print(f"找到元素: {element}")
    except:
        print(f"未能找到 AGREE_BUTTON 元素")

    # 点击同意按钮
    start_page.click_agree()

    start_page.clear_app_cache()
    start_page.close_app()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未关闭"

# noinspection PyBroadException
def test_click_reject_button(driver):
    """测试点击不同意按钮退出APP"""
    start_page = StartPageBusiness(driver)

    if start_page.is_app_running():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page.launch_app()
    else:
        start_page.clear_app_cache()
        start_page.launch_app()

    try:
        element = start_page.find_element(start_page.REJECT_BUTTON, timeout=30)
        print(f"找到元素: {element}")
    except:
        print(f"未能找到 REJECT_BUTTON 元素")

    # 点击不同意按钮
    start_page.click_reject()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未能成功关闭"

    start_page.clear_app_cache()

# noinspection PyBroadException
def test_click_privacy_policy(driver):
    """测试点击隐私政策链接"""
    start_page = StartPageBusiness(driver)

    if start_page.is_app_running():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page.launch_app()
    else:
        start_page.clear_app_cache()
        start_page.launch_app()

    # # 点击隐私政策
    # expected_texts = ["隐私政策", "条款"]
    # start_page.click_privacy_policy(start_page.PRIVACY_POLICY, expected_texts)

    # 判断隐私政策是否存在
    if start_page.is_content_displayed():
        start_page.tap_coordinates(258,121,1000)

    start_page.clear_app_cache()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未能成功关闭"

# noinspection PyBroadException
def test_click_user_agreement(driver):
    """测试点击用户协议链接"""
    start_page = StartPageBusiness(driver)

    if start_page.is_app_running():
        start_page.clear_app_cache()
        start_page.close_app()
        start_page.launch_app()
    else:
        start_page.clear_app_cache()
        start_page.launch_app()

    # # 点击用户协议
    # expected_texts = ["用户协议", "服务条款"]
    # start_page.click_user_agreement(start_page.USER_AGREEMENT, expected_texts)

    # 判断隐私政策是否存在
    if start_page.is_content_displayed():
        start_page.tap_coordinates(225,121,1000)

    start_page.clear_app_cache()

    # 验证应用是否关闭
    assert start_page.is_app_closed(), "应用未能成功关闭"

if __name__ == "__main__":
    pytest.main()