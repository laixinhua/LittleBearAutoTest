import logging
import time

import allure
import pytest

from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.ExhibitionHall.Exhibition_hall_General_settings_page import ExhibitionHallGeneralSettingsPage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.company.Company_General_settings_page import CompanyGeneralSettingsPage
from page_obj.company.General_settings_company_settings_page import GeneralSettingsCompanySettingsPage
from page_obj.common.Left_menu_bar_page import LeftMenuBarPage
from page_obj.manufacturer.Manufacturer_General_settings_page import ManufacturerGeneralSettingsPage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.ExhibitionHall.View_unpublished_products_in_the_exhibition_hall_page import \
    ViewUnpublishedProductsInTheExhibitionHallPage
from page_obj.common.login_page import LoginPage
from page_obj.common.set_up_page import SetUpPage


@allure.feature("通用设置模块")#allure添加模块区分
class TestGeneralSettings:
    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            time.sleep(2)
            ExhibitionHallGeneralSettingsPage(app_page).Click_Back_button()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            time.sleep(2)
            CompanyGeneralSettingsPage(app_page).Click_Back_button()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            time.sleep(2)
            ManufacturerGeneralSettingsPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Company_settings(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击产品隐私设置")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Personal_settings(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Product_privacy_settings()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Product_privacy_settings()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_Back_button(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Back_button()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Back_button()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-查询员工")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_Search_employees(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Search_employees()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Search_employees()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Search_employees()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-点击全部员工接收推送信息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_All_employees_receive_push_information(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_All_employees_receive_push_information()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_All_employees_receive_push_information()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_All_employees_receive_push_information()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-点击全部员工接收短信")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_All_employees_receive_SMS(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_All_employees_receive_SMS()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_All_employees_receive_SMS()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_All_employees_receive_SMS()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-点击接收业务咨询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_Employee_receive_business_consultation(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_business_consultation()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_business_consultation()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_business_consultation()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-点击接收推送信息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_Employee_receive_push_information(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_push_information()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_push_information()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_push_information()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("点击业务咨询、推送、短信设置-点击接收短信")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Business_consultation_push_and_SMS_settings_Employee_receive_SMS(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ExhibitionHallGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_SMS()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            CompanyGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_SMS()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
            ManufacturerGeneralSettingsPage(app_page).Click_Business_consultation_push_and_SMS_settings()
            GeneralSettingsCompanySettingsPage(app_page).Click_Employee_receive_SMS()
        logging.info("开始断言")

    @allure.story("通用设置")  # allure子模块名称
    @allure.title("展厅通用设置其他操作")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_General_setting_other_operations(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Avatar()
        LeftMenuBarPage(app_page).Click_set_up()
        SetUpPage(app_page).Click_General_settings()
        ExhibitionHallGeneralSettingsPage(app_page).Click_Display_showroom_sample_selection_record()
        ExhibitionHallGeneralSettingsPage(app_page).Click_Show_visit_records()
        ExhibitionHallGeneralSettingsPage(app_page).Click_View_unpublished_products_in_the_exhibition_hall()
        ViewUnpublishedProductsInTheExhibitionHallPage(app_page).Click_All_employees_are_allowed_to_see()
        ViewUnpublishedProductsInTheExhibitionHallPage(app_page).Click_staff()