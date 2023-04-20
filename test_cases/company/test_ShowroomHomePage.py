import logging

import allure
import pytest

from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.company.Showroom_Homepage_page import ShowroomHomePage


@allure.feature("展厅主页")#allure添加模块区分
class TestShowroomHomePage:
    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("查看更多")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_See_more(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).See_more()
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("扫码搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Code_scanning_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Code_scanning_search()
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("关键词搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Keyword_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Keyword_search(app_page)
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("选择入驻厂家")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Settled_manufacturer(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Settled_manufacturer()
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("入驻厂家查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Inquiry_of_settled_manufacturers(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Inquiry_of_settled_manufacturers()
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("选择展厅类目")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Exhibition_hall_category(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Exhibition_hall_category()
        logging.info("开始断言")

    @allure.story("展厅主页")  # allure子模块名称
    @allure.title("展厅类目-产品查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Exhibition_hall_category_Product_query(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        ShowroomHomePage(app_page).Exhibition_hall_category_Product_query(app_page)
        logging.info("开始断言")