import logging
import time

import allure
import pytest

from common import Random_name
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Left_menu_bar_page import LeftMenuBarPage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage

@allure.feature("登录模块")#allure添加模块区分
class TestSelectRole:
    @allure.story("角色选择")  # allure子模块名称
    @allure.title("选择展厅角色")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_select_the_role_of_the_exhibition_hall(self,app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("角色选择")  # allure子模块名称
    @allure.title("选择公司角色")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_select_company_role(self,app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        RolePage(app_page).Select_company_role()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("角色选择")  # allure子模块名称
    @allure.title("选择厂商角色")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_select_vendor_role(self,app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        RolePage(app_page).Select_vendor_role()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("角色选择")  # allure子模块名称
    @allure.title("随机选择角色")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_random_select_role(self, app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        Role = Random_name.RandomName.RandomRole(app_page)
        if Role == "展厅":
            RolePage(app_page).Select_the_role_of_the_exhibition_hall()
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Switch_roles()
            New_Role = Random_name.RandomName.RandomRole(app_page)
            if New_Role == "展厅":
                RolePage(app_page).Select_the_role_of_the_exhibition_hall()
                time.sleep(10)
                logging.info("开始断言")
            elif New_Role == "公司":
                RolePage(app_page).Select_company_role()
                time.sleep(10)
                logging.info("开始断言")
            elif New_Role == "厂商":
                RolePage(app_page).Select_vendor_role()
                time.sleep(10)
                logging.info("开始断言")
        elif Role == "公司":
            RolePage(app_page).Select_company_role()
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Switch_roles()
            New_Role = Random_name.RandomName.RandomRole(app_page)
            if New_Role == "展厅":
                RolePage(app_page).Select_the_role_of_the_exhibition_hall()
                time.sleep(10)
                logging.info("开始断言")
            elif New_Role == "公司":
                RolePage(app_page).Select_company_role()
                time.sleep(10)
                logging.info("开始断言")
            elif New_Role == "厂商":
                RolePage(app_page).Select_vendor_role()
                time.sleep(10)
                logging.info("开始断言")
        elif Role == "厂商":
            RolePage(app_page).Select_vendor_role()
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Switch_roles()
            New_Role = Random_name.RandomName.RandomRole(app_page)
            if New_Role == "展厅":
                RolePage(app_page).Select_the_role_of_the_exhibition_hall()
                time.sleep(10)
                logging.info("开始断言")
            elif New_Role == "公司":
                RolePage(app_page).Select_company_role()
                time.sleep(10)
                logging.info("开始断言")
            elif New_Role == "厂商":
                RolePage(app_page).Select_vendor_role()
                time.sleep(10)
                logging.info("开始断言")

