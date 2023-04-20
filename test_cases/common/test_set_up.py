import logging
import time

import allure
import pytest

import common.Modify_Personal_Information
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Left_menu_bar_page import LeftMenuBarPage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.common.set_up_page import SetUpPage


@allure.feature("设置模块")#allure添加模块区分
class TestSetUp:
    @allure.story("设置页面")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Back_button()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Back_button()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("个人信息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_personal_information(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_personal_information()
            common.Modify_Personal_Information.ModifyPersonalInformation.ModifyPersonalInformation(app_page,app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_personal_information()
            common.Modify_Personal_Information.ModifyPersonalInformation.ModifyPersonalInformation(app_page, app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_personal_information()
            common.Modify_Personal_Information.ModifyPersonalInformation.ModifyPersonalInformation(app_page, app_page)
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("清除缓存")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Clear_cache(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Clear_cache(app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Clear_cache(app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Clear_cache(app_page)
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("通用设置")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_General_settings(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_General_settings()
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("关于小竹熊云科技")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_About_Xiao_zhu_xiong_yun_Technology(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_About_Xiao_zhu_xiong_yun_Technology()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_About_Xiao_zhu_xiong_yun_Technology()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_About_Xiao_zhu_xiong_yun_Technology()
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("更新历史")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Update_History(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Update_History()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Update_History()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Update_History()
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("联系我们")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_contact_us(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_contact_us()
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_contact_us()
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_contact_us()
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("切换角色")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Switch_roles(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Switch_roles()
            RolePage(app_page).Random_Select_role(app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Switch_roles()
            RolePage(app_page).Random_Select_role(app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Switch_roles()
            RolePage(app_page).Random_Select_role(app_page)
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("退出登录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Logout(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Logout(app_page)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Logout(app_page)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Logout(app_page)
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("用户服务协议")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_User_service_agreement(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_User_service_agreement()
            time.sleep(3)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_User_service_agreement()
            time.sleep(3)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_User_service_agreement()
            time.sleep(3)
        logging.info("开始断言")

    @allure.story("设置页面")  # allure子模块名称
    @allure.title("隐私政策")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Privacy_policy(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Privacy_policy()
            time.sleep(3)
        elif Role == "公司":
            CompanyHomePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Privacy_policy()
            time.sleep(3)
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_set_up()
            SetUpPage(app_page).Click_Privacy_policy()
            time.sleep(3)
        logging.info("开始断言")