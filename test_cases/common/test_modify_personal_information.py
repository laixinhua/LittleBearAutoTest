import logging

import allure
import pytest

from common import Random_name
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Left_menu_bar_page import LeftMenuBarPage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.common.personal_information_page import PersonalInformationPage



@allure.feature("个人信息模块")#allure添加模块区分
class TestModifyPersonalInfomation:
    @allure.story("修改个人信息")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Click_Back_button()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Click_Back_button()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("修改个人信息")  # allure子模块名称
    @allure.title("修改头像")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Modify_Avatar(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Avatar()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Avatar()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Avatar()
        logging.info("开始断言")

    @allure.story("修改个人信息")  # allure子模块名称
    @allure.title("修改姓名")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Modify_Name(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            new_name = Random_name.RandomName.RandomNames(app_page)
            PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            new_name = Random_name.RandomName.RandomNames(app_page)
            PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            new_name = Random_name.RandomName.RandomNames(app_page)
            PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
        logging.info("开始断言")

    @allure.story("修改个人信息")  # allure子模块名称
    @allure.title("修改性别")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Modify_Gender(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Gender(app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Gender(app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Gender(app_page)
        logging.info("开始断言")

    @allure.story("修改个人信息")  # allure子模块名称
    @allure.title("修改生日")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Modify_Birthday(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Birthday(app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Birthday(app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Birthday(app_page)
        logging.info("开始断言")


    @allure.story("修改个人信息")  # allure子模块名称
    @allure.title("修改个人信息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Modify_personal_information(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Avatar()
            new_name = Random_name.RandomName.RandomNames(app_page)
            PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
            PersonalInformationPage(app_page).Modify_Gender(app_page)
            PersonalInformationPage(app_page).Modify_Birthday(app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Avatar()
            new_name = Random_name.RandomName.RandomNames(app_page)
            PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
            PersonalInformationPage(app_page).Modify_Gender(app_page)
            PersonalInformationPage(app_page).Modify_Birthday(app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_head_portrait()
            PersonalInformationPage(app_page).Modify_Avatar()
            new_name = Random_name.RandomName.RandomNames(app_page)
            PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
            PersonalInformationPage(app_page).Modify_Gender(app_page)
            PersonalInformationPage(app_page).Modify_Birthday(app_page)
        logging.info("开始断言")

