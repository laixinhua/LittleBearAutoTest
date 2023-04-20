import logging
import time

import allure
import pytest

from page_obj.common.Crop_page import CropPage
from page_obj.common.Select_Picture_page import SelectPicturePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.common.product_page import ProductPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.company.Shopping_Cart_page import ShoppingCartPage


@allure.feature("购物车")#allure添加模块区分
class TestShoppingCart:
    @allure.story("购物车")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("扫码二维码")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Scanning_QR_code(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Code_scanning_query()
        SelectPicturePage(app_page).Select_Figure_two()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("关键字搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Keyword_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Keyword_search(app_page)
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("购物车排序")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_sort(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).sort()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("箱数操作")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Number_of_operation_boxes(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Number_of_operation_boxes()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("勾选产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Tick_product(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).shopping_cart()
        time.sleep(5)
        ShoppingCartPage(app_page).Tick_product()
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("删除产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_delete_product(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).delete_product(app_page)
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("购物车")  # allure子模块名称
    @allure.title("生成报价")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Generate_quotation(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        ProductPage(app_page).shopping_cart()
        ShoppingCartPage(app_page).Generate_quotation()
        time.sleep(5)
        logging.info("开始断言")


