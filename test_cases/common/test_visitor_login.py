import logging
import time

import allure
import pytest

from page_obj.common.Visitor_login_page import VisitorLoginPage
from page_obj.common.login_page import LoginPage


@allure.feature("登录模块")#allure添加模块区分
class TestVisitorLogin:
    @allure.story("游客登录")  # allure子模块名称
    @allure.title("公司游客登录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Company_visitor_login(self,app_page):
        """公司游客登录"""  # 这是描述
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Visitor_login(app_page)
        LoginPage(app_page).Company_visitor_login()


    @allure.story("游客登录")  # allure子模块名称
    @allure.title("厂商游客登录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Vendor_visitor_login(self, app_page):
        """厂商游客登录"""  # 这是描述
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Visitor_login(app_page)
        LoginPage(app_page).Vendor_visitor_login()