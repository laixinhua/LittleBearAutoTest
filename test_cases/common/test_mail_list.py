import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.common.mail_list_page import MailListPage
from page_obj.common.news_page import NewsPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage


class TestMailList:
    @allure.story("通讯录")  # allure子模块名称
    @allure.title("添加好友")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Add_friends(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Add_friends(app_page)
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Add_friends(app_page)
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Add_friends(app_page)

    @allure.story("通讯录")  # allure子模块名称
    @allure.title("发起群聊")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Initiate_group_chat(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Initiate_group_chat()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Initiate_group_chat()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Initiate_group_chat()

    @allure.story("通讯录")  # allure子模块名称
    @allure.title("处理好友请求")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Process_friend_requests(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Friend_request_operation(app_page)
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Friend_request_operation(app_page)
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Friend_request_operation(app_page)

    @allure.story("通讯录")  # allure子模块名称
    @allure.title("查看公司主页")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_company_homepage(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).View_company_homepage()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).View_company_homepage()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).View_company_homepage()

    @allure.story("通讯录")  # allure子模块名称
    @allure.title("查询未分组成员")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Ungrouped_member_query(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Ungrouped_member_query()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Ungrouped_member_query()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Ungrouped_member_query()

    @allure.story("通讯录")  # allure子模块名称
    @allure.title("好友相关操作")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Friend_Action(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Friend_Action(app_page)
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Friend_Action(app_page)
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            NewsPage(app_page).Click_Address_Book()
            time.sleep(5)
            MailListPage(app_page).Friend_Action(app_page)

