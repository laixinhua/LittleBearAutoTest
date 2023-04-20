import logging
import random
import time

import allure
import pytest

from common import Random_name
from common.basepage import BasePage
from page_obj.common.Visitor_login_page import VisitorLoginPage
from page_obj.common.login_page import LoginPage
from page_obj.common.register_page import RegisterPage
from page_obj.company.Company_home_page import CompanyHomePage
from test_cases.common.test_visitor_login import TestVisitorLogin
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("登录模块")#allure添加模块区分
class TestVisitorRegister:
    @allure.story("游客注册")  # allure子模块名称
    @allure.title("公司游客点击跳过")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Company_visitor_login_skip(self, app_page):
        """公司游客登录"""  # 这是描述
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Visitor_login(app_page)
        VisitorLoginPage(app_page).Company_visitor_login()
        RegisterPage(app_page).click_skip()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("游客注册")  # allure子模块名称
    @allure.title("厂商游客点击跳过")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Vendor_visitor_login_skip(self, app_page):
        """厂商游客登录"""  # 这是描述
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Visitor_login(app_page)
        VisitorLoginPage(app_page).Vendor_visitor_login()
        RegisterPage(app_page).click_skip()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("游客注册")  # allure子模块名称
    @allure.title("公司游客注册")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Company_visitor_registration(self, app_page):
        """公司游客登录"""  # 这是描述
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Visitor_login(app_page)
        VisitorLoginPage(app_page).Company_visitor_login()
        compyany_name = Random_name.RandomName.RandomCompanyName(app_page)
        RegisterPage(app_page).Fill_in_the_company_name(compyany_name)
        customer_name = Random_name.RandomName.RandomNames(app_page)
        RegisterPage(app_page).Fill_in_contact(customer_name)
        phone_number = Random_name.RandomName.RandomPhoneNumber(app_page)
        RegisterPage(app_page).Fill_in_the_mobile_phone_number(phone_number)
        Telephone_landline = Random_name.RandomName.RandomLandlineNumber(app_page)
        RegisterPage(app_page).Fill_in_Telephone_landline(Telephone_landline)
        QQnumber = Random_name.RandomName.RandomQQNumber(app_page)
        RegisterPage(app_page).Fill_in_QQNumber(QQnumber)
        address = Random_name.RandomName.RandomAddress(app_page)
        RegisterPage(app_page).Fill_in_Address(address)
        RegisterPage(app_page).visitor_swipe()
        RegisterPage(app_page).Upload_company_logo()
        RegisterPage(app_page).Upload_business_license()
        RegisterPage(app_page).Visitor_registration()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("游客注册")  # allure子模块名称
    @allure.title("厂商游客注册")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Vendor_visitor_registration(self, app_page):
        """厂商游客登录"""  # 这是描述
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Visitor_login(app_page)
        VisitorLoginPage(app_page).Vendor_visitor_login()
        compyany_name = Random_name.RandomName.RandomCompanyName(app_page)
        RegisterPage(app_page).Fill_in_the_company_name(compyany_name)
        customer_name = Random_name.RandomName.RandomNames(app_page)
        RegisterPage(app_page).Fill_in_contact(customer_name)
        phone_number = Random_name.RandomName.RandomPhoneNumber(app_page)
        RegisterPage(app_page).Fill_in_the_mobile_phone_number(phone_number)
        Telephone_landline = Random_name.RandomName.RandomLandlineNumber(app_page)
        RegisterPage(app_page).Fill_in_Telephone_landline(Telephone_landline)
        QQnumber = Random_name.RandomName.RandomQQNumber(app_page)
        RegisterPage(app_page).Fill_in_QQNumber(QQnumber)
        address = Random_name.RandomName.RandomAddress(app_page)
        RegisterPage(app_page).Fill_in_Address(address)
        RegisterPage(app_page).visitor_swipe()
        RegisterPage(app_page).Upload_company_logo()
        RegisterPage(app_page).Upload_business_license()
        RegisterPage(app_page).Visitor_registration()
        time.sleep(5)
        logging.info("开始断言")


