# # test_cases/test_login.py
# """
# 弹窗登录功能测试用例
# 测试用户通过弹窗登录的各种场景
# """
#
# import pytest
# from appium.webdriver.common.appiumby import AppiumBy
# from src.pages.Pop_up_login import PopUpLoginPage
#
# def login_out(driver):
#     """
#     退出登录
#     """
#     login_out = PopUpLoginPage(driver)
#     login_out.launch_app()
#
#     login_out.wait(10)
#
#     login_out.click_element(AppiumBy.ID, "tab_mine")
#     login_out.click_element(AppiumBy.ID, "siv_mine_settings")
#
#     login_out.click_element(AppiumBy.ID, "stv_log_out")
#     login_out.click_element(AppiumBy.ID, "confirm")
#
#     login_out.close_app()
#
# def test_valid_popup_login(driver):
#     """
#     测试有效的弹窗登录
#     验证使用正确手机号和验证码能够成功登录
#     """
#     popup_login = PopUpLoginPage(driver)
#     popup_login.launch_app()
#
#     # 确保弹窗已显示
#     assert popup_login.is_popup_displayed(), "弹窗登录页面未显示"
#
#     # 点击手机登录按钮
#     popup_login.click_login_tel()
#
#     # 确保手机登录界面已显示
#     assert popup_login.is_popup_tel_displayed(), "手机登录界面未显示"
#
#     # 执行登录操作
#     popup_login.input_user_tel("13444444444")
#     popup_login.input_user_code("1234")
#     popup_login.click_check_box()
#     popup_login.click_login()
#
#     # 验证登录成功（这里需要根据实际业务逻辑添加验证点）
#     popup_login.assert_toast_visible("登录成功")
#
#     popup_login.close_popup()
#     popup_login.close_app()
#     login_out(driver)
#
#
# def test_invalid_popup_tel_login(driver):
#     """
#     测试无效的弹窗登录
#     验证使用错误手机登录时的处理
#     """
#     popup_login = PopUpLoginPage(driver)
#
#     # 确保弹窗已显示
#     assert popup_login.is_popup_displayed(), "弹窗登录页面未显示"
#
#     # 点击手机登录按钮
#     popup_login.click_login_tel()
#
#     # 确保手机登录界面已显示
#     assert popup_login.is_popup_tel_displayed(), "手机登录界面未显示"
#
#     # 输入无效凭证
#     popup_login.input_user_tel("1344444444")
#     popup_login.input_user_code("1233")
#     popup_login.click_check_box()
#     popup_login.click_login()
#
#     # 验证错误处理
#     popup_login.assert_toast_visible("请输入正确的手机号")
#
# def test_invalid_popup_code_login(driver):
#     """
#     测试无效的弹窗登录
#     验证使用错误凭证登录时的处理
#     """
#     popup_login = PopUpLoginPage(driver)
#
#     # 确保弹窗已显示
#     assert popup_login.is_popup_displayed(), "弹窗登录页面未显示"
#
#     # 点击手机登录按钮
#     popup_login.click_login_tel()
#
#     # 确保手机登录界面已显示
#     assert popup_login.is_popup_tel_displayed(), "手机登录界面未显示"
#
#
# def test_empty_credentials_popup_login(driver):
#     """
#     测试空凭证弹窗登录
#     验证不输入手机号或验证码时的处理
#     """
#     popup_login = PopUpLoginPage(driver)
#
#     # 确保弹窗已显示
#     assert popup_login.is_popup_displayed(), "弹窗登录页面未显示"
#
#     # 点击手机登录按钮
#     popup_login.click_login_tel()
#
#     # 确保手机登录界面已显示
#     assert popup_login.is_popup_tel_displayed(), "手机登录界面未显示"
#
#     # 不输入任何信息直接点击登录
#     popup_login.click_login()
#
#     # 验证表单验证（根据实际业务添加具体验证）
#     popup_login.assert_toast_visible("请输入正确的手机号")
#
# def test_wechat_login(driver):
#     """
#     测试微信登录功能
#     验证点击微信登录按钮的处理
#     """
#     popup_login = PopUpLoginPage(driver)
#
#     # 确保弹窗已显示
#     assert popup_login.is_popup_displayed(), "弹窗登录页面未显示"
#
#     # 点击微信登录按钮
#     popup_login.click_login_wechat()
#
#     # 验证微信登录处理（根据实际业务添加具体验证）
