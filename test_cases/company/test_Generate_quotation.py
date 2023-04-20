import logging
import time

import allure
import pytest

from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.common.product_page import ProductPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.company.Generate_quotation_page import GenerateQuotationPage
from page_obj.company.Shopping_Cart_page import ShoppingCartPage


@allure.feature("找样报价")#allure添加模块区分
class TestGenerateQuotation:
    @allure.story("生成报价")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Generate_quotation()
        GenerateQuotationPage(app_page).Click_Back_button(app_page)
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("生成报价")  # allure子模块名称
    @allure.title("切换业务员")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Generate_quotation(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Generate_quotation()
        GenerateQuotationPage(app_page).Generate_quotation(app_page)
        time.sleep(5)
        logging.info("开始断言")