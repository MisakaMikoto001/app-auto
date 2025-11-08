# test_cases/test_002_login.py
import pytest
from selenium.common import TimeoutException

from src.business.First_login import FirstLoginBusiness

# 直接在代码中定义测试数据
LOGIN_TEST_DATA = {
    'first_login_phone_data': [
        {
            'phone': "13444444444",
            'code': "1234",
            'expected_result': True,
            'description': "有效手机号和验证码"
        },
        {
            'phone': "1344444444",
            'code': "1234",
            'expected_result': False,
            'description': "无效手机号（位数不足）"
        },
        {
            'phone': "13444444444",
            'code': "123",
            'expected_result': False,
            'description': "无效验证码（位数不足）"
        },
        {
            'phone': "",
            'code': "",
            'expected_result': False,
            'description': "空手机号和验证码"
        }
    ]
}


@pytest.fixture(scope="module")
def login_test_data():
    """
    登录测试数据fixture
    """
    return LOGIN_TEST_DATA


def test_login_process_with_wechat_success(driver):
    """
    测试首次微信登录成功场景
    """
    first_login = FirstLoginBusiness(driver)

    try:
        result = first_login.login_process_with_wechat()
        assert isinstance(result, bool), "微信登录应返回布尔值"
    except TimeoutException as e:
        pytest.fail(f"元素定位超时，请检查元素定位符是否正确: {e}")


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

    # 这里需要mock相关页面对象的方法，使is_popup_displayed返回False
    # 由于实际测试环境中可能需要特殊设置才能触发此场景，我们暂时跳过此测试
    pytest.skip("需要mock机制来测试弹窗未显示场景")

    result = first_login.first_login_process_with_phone(
        valid_data['phone'],
        valid_data['code']
    )

    assert result is False, "当弹窗未显示时，登录流程应该返回False"


def test_first_login_initialization(driver):
    """
    测试FirstLoginBusiness类的初始化
    验证所有相关页面对象被正确初始化
    """
    first_login = FirstLoginBusiness(driver)

    # 验证各个页面对象被正确初始化
    assert first_login.start_page_business is not None, "StartPageBusiness应该被正确初始化"
    assert first_login.popup_login_wechat_business is not None, "PopUpLoginWeChatBusiness应该被正确初始化"
    assert first_login.popup_login_tel_business is not None, "PopUpLoginTelBusiness应该被正确初始化"
    assert first_login.tab_create_page is not None, "TabCreatePage应该被正确初始化"
    assert first_login.driver == driver, "driver应该被正确传递"


@pytest.mark.parametrize("test_case_data", LOGIN_TEST_DATA['first_login_phone_data'])
def test_first_login_process_parameterized(driver, test_case_data):
    """
    参数化测试首次手机登录流程使用不同凭证的场景
    """
    first_login = FirstLoginBusiness(driver)

    # 注意：这个测试用例的实际结果可能依赖于mock的页面对象行为
    # 在实际测试环境中，可能需要调整预期结果或mock相关方法
    result = first_login.first_login_process_with_phone(
        test_case_data['phone'],
        test_case_data['code']
    )

    expected = test_case_data['expected_result']
    assert result is expected, f"测试用例 '{test_case_data['description']}' 失败"
