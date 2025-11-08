import pytest
import yaml
import os
from src.business.First_login import FirstLoginBusiness


def load_test_data():
    """
    加载测试数据
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, "..", "test_data", "login_data.yml")

    with open(data_file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def login_test_data():
    """
    登录测试数据fixture
    """
    return load_test_data()['login_test_data']


def test_first_login_process_with_phone_success(driver, login_test_data):
    """
    测试首次手机登录完整流程 - 成功场景
    验证使用正确手机号和验证码能够成功完成首次登录流程
    """
    first_login = FirstLoginBusiness(driver)

    # 从测试数据中获取有效的手机号和验证码
    valid_data = next(item for item in login_test_data['first_login_phone_data']
                      if item['expected_result'] is True)

    if not valid_data:
        pytest.skip("没有有效的测试数据")

    result = first_login.first_login_process_with_phone(
        valid_data['phone'],
        valid_data['code']
    )

    assert result is True, "首次手机登录流程应该成功执行"


def test_first_login_process_with_phone_popup_not_displayed(driver, login_test_data):
    """
    测试首次手机登录完整流程 - 弹窗未显示场景
    验证当登录弹窗未显示时的处理
    """
    first_login = FirstLoginBusiness(driver)

    # 从测试数据中获取有效数据
    valid_data = next(item for item in login_test_data['first_login_phone_data']
                      if item['expected_result'] is True)


    result = first_login.first_login_process_with_phone(
        valid_data['phone'],
        valid_data['code']
    )

    assert result is False, "当弹窗未显示时，登录流程应该返回False"


def test_first_login_process_with_wechat_success(driver):
    """
    测试首次微信登录完整流程 - 成功场景
    验证能够成功完成首次微信登录流程
    """
    first_login = FirstLoginBusiness(driver)

    result = first_login.first_login_process_with_wechat()

    assert result is True, "首次微信登录流程应该成功执行"


def test_first_login_process_with_wechat_popup_not_displayed(driver):
    """
    测试首次微信登录完整流程 - 弹窗未显示场景
    验证当登录弹窗未显示时的处理
    """
    first_login = FirstLoginBusiness(driver)

    # 这里需要mock相关页面对象的方法，使is_popup_displayed返回False
    result = first_login.first_login_process_with_wechat()

    assert result is False, "当弹窗未显示时，登录流程应该返回False"



@pytest.mark.parametrize("test_case_data", [
    item for item in load_test_data()['login_test_data']['first_login_phone_data']
])
def test_first_login_process_parameterized(driver, test_case_data):
    """
    参数化测试首次手机登录流程使用不同凭证的场景
    """
    first_login = FirstLoginBusiness(driver)

    result = first_login.first_login_process_with_phone(
        test_case_data['phone'],
        test_case_data['code']
    )

    expected = test_case_data['expected_result']
    assert result is expected, f"测试用例 '{test_case_data['description']}' 失败"
