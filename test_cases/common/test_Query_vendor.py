import time

import allure
import pytest

from page_obj.common.Crop_page import CropPage
from page_obj.common.Query_vendor_page import QueryVendorPage
from page_obj.common.Select_Picture_page import SelectPicturePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.company.Company_home_page import CompanyHomePage


@allure.feature("查询厂商")#allure添加模块区分
class TestQueryVendor:
    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Click_Back_button()

    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("Logo查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Logo_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Logo_search()
        SelectPicturePage(app_page).Select_Figure_two()
        time.sleep(5)

    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("厂商名称查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Keyword_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Keyword_search(app_page)
        time.sleep(5)

    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("厂商名称查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_fixed_vendor(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        time.sleep(5)

    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("历史查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_History_Search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).History_Search()
        time.sleep(5)

    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("是否删除历史查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Delete_History_Search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Delete_History_Search(app_page)
        time.sleep(5)

    @allure.story("查询厂商")  # allure子模块名称
    @allure.title("多次查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Multiple_historical_searches(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Multiple_historical_searches()
        time.sleep(5)

