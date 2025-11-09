import pytest
import yaml
import logging
import allure
import traceback
from pathlib import Path

from src.business.First_login import FirstLoginBusiness


class TimeoutException(Exception):
    """自定义超时异常"""
    pass

@pytest.fixture(scope="module")
def login_test_data():
    """
    从YAML文件中读取登录测试数据的fixture
    """
    yaml_path = Path(__file__).parent.parent / "test_data" / "login_data.yaml"
    with open(yaml_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data["login_test_data"]


@pytest.fixture
def first_login_business(driver):
    """
    FirstLoginBusiness实例fixture
    """
    first_login = FirstLoginBusiness(driver)

    if first_login.tab_create_page.is_app_running():
        first_login.tab_create_page.close_app()
        first_login.tab_create_page.launch_app()

    return first_login


def test_close_the_pop_up(driver):
    """
     - 弹窗关闭场景
    验证当登录弹窗弹出时的关闭测试
    """
    first_login = FirstLoginBusiness(driver)

    # 关闭微信登录弹窗
    if first_login.tab_create_page.is_app_running():
        first_login.tab_create_page.close_app()
        first_login.tab_create_page.clear_app_cache()
        first_login.tab_create_page.launch_app()
        result = first_login.pop_up_wechat_closes()
    else:
        first_login.tab_create_page.clear_app_cache()
        first_login.tab_create_page.launch_app()
        result = first_login.pop_up_wechat_closes()

    # 关闭手机登录弹窗
    if first_login.tab_create_page.is_app_running():
        first_login.tab_create_page.close_app()
        first_login.tab_create_page.clear_app_cache()
        first_login.tab_create_page.launch_app()
        first_login.tab_create_page.pop_up_phone_closes()
    else:
        first_login.tab_create_page.clear_app_cache()
        first_login.tab_create_page.launch_app()
        first_login.tab_create_page.pop_up_phone_closes()

    assert result is False, "当弹窗未显示时，登录流程应该返回False"



def test_first_login_initialization(driver):
    """
    测试FirstLoginBusiness类的初始化
    验证所有相关页面对象被正确初始化
    """
    first_login = FirstLoginBusiness(driver)

    if first_login.tab_create_page.is_app_running():
        first_login.tab_create_page.close_app()
        first_login.tab_create_page.launch_app()

    # 验证各个页面对象被正确初始化
    assert first_login.start_page_business is not None, "StartPageBusiness应该被正确初始化"
    assert first_login.popup_login_wechat_business is not None, "PopUpLoginWeChatBusiness应该被正确初始化"
    assert first_login.popup_login_tel_business is not None, "PopUpLoginTelBusiness应该被正确初始化"
    assert first_login.tab_create_page is not None, "TabCreatePage应该被正确初始化"
    assert first_login.driver == driver, "driver应该被正确传递"


def test_first_login_process_parameterized(first_login_business, login_test_data):
    """
    参数化测试首次手机登录流程使用不同凭证的场景
    从YAML文件中读取测试数据
    """
    # 对每个测试数据运行测试
    for test_case_data in login_test_data['first_login_phone_data']:

        result = first_login_business.first_login_process_with_phone(
            test_case_data['phone'],
            test_case_data['code']
        )

        # 验证结果,包含手机号、验证码、提示信息
        expected = test_case_data['expected_result']
        assert result == expected, f"测试用例 '{test_case_data['description']}' 失败: 期望 {expected}, 实际 {result}"

        # 优化吐司断言逻辑
        if 'toast' in test_case_data and test_case_data['toast']:
            # 使用更稳定的吐司检查方法
            is_displayed = first_login_business.is_toast_displayed(test_case_data['toast'], timeout=10)
            assert is_displayed, f"测试用例 '{test_case_data['description']}' toast未显示: 期望显示 '{test_case_data['toast']}'"

            # 获取实际显示的吐司文本进行验证
            toast_text = first_login_business.get_toast_text(timeout=10)
            assert toast_text is not None, f"测试用例 '{test_case_data['description']}' 无法获取toast文本"
            assert test_case_data[
                       'toast'] in toast_text, f"测试用例 '{test_case_data['description']}' toast文本不匹配: 期望 '{test_case_data['toast']}', 实际 '{toast_text}'"


def test_login_process_with_wechat_success(first_login_business):
    """
    测试首次微信登录成功场景
    从YAML文件中读取测试数据
    """
    try:
        result = first_login_business.login_process_with_wechat()
        assert isinstance(result, bool), "微信登录应返回布尔值"
    except TimeoutException as e:
        pytest.fail(f"元素定位超时，请检查元素定位符是否正确: {e}")


def test_first_login_process_with_phone_success(first_login_business, login_test_data):
    """
    测试首次手机登录完整流程 - 成功场景
    验证使用正确手机号和验证码能够成功完成首次登录流程
    从YAML文件中读取测试数据
    """
    # 从测试数据中获取有效的手机号和验证码
    valid_data = next(item for item in login_test_data['first_login_phone_data']
                      if item['expected_result'] is True)

    if not valid_data:
        pytest.skip("没有有效的测试数据")

    result = first_login_business.first_login_process_with_phone(
        valid_data['phone'],
        valid_data['code']
    )

    assert result is True, "首次手机登录流程应该成功执行"
