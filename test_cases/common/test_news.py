import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.common.news_page import NewsPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage


@allure.feature("消息模块")#allure添加模块区分
class TestNews:
    @allure.story("消息")  # allure子模块名称
    @allure.title("点击通讯录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Address_Book(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Address_Book()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Address_Book()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Address_Book()

    @allure.story("消息")  # allure子模块名称
    @allure.title("点击添加好友")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_to_add_friends(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_to_add_friends()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_to_add_friends()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_to_add_friends()

    @allure.story("消息")  # allure子模块名称
    @allure.title("消息页添加好友")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Message_page_to_add_friends(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Message_page_to_add_friends(app_page)
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Message_page_to_add_friends(app_page)
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Message_page_to_add_friends(app_page)

    @allure.story("消息")  # allure子模块名称
    @allure.title("消息页发起群聊")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Message_page_launches_group_chat(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Message_page_launches_group_chat()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Message_page_launches_group_chat()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Message_page_launches_group_chat()

    @allure.story("消息")  # allure子模块名称
    @allure.title("消息页点击系统消息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Message_page_Click_System_messages(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_System_messages()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_System_messages()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_System_messages()

    @allure.story("消息")  # allure子模块名称
    @allure.title("系统消息页点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_System_message_page_return(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).System_message_page_return()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).System_message_page_return()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).System_message_page_return()

    @allure.story("消息")  # allure子模块名称
    @allure.title("系统消息页点击全部")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_All_on_the_system_message_page(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_All_on_the_system_message_page()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_All_on_the_system_message_page()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_All_on_the_system_message_page()

    @allure.story("消息")  # allure子模块名称
    @allure.title("系统消息页点击未读")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_System_message_page_click_unread(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).System_message_page_click_unread()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).System_message_page_click_unread()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).System_message_page_click_unread()

    @allure.story("消息")  # allure子模块名称
    @allure.title("系统消息页点击已读")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Read_on_the_system_message_page(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Read_on_the_system_message_page()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Read_on_the_system_message_page()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Read_on_the_system_message_page()

    @allure.story("消息")  # allure子模块名称
    @allure.title("系统消息页点击一键已读")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_One_click_on_the_system_message_page_to_read(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).One_click_on_the_system_message_page_to_read()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).One_click_on_the_system_message_page_to_read()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).One_click_on_the_system_message_page_to_read()

    @allure.story("消息")  # allure子模块名称
    @allure.title("系统消息页查看系统消息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_system_messages(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).View_system_messages()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).View_system_messages()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).View_system_messages()

    @allure.story("消息")  # allure子模块名称
    @allure.title("删除系统消息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Delete_System_Message(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Delete_System_Message()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Delete_System_Message()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Delete_System_Message()

    @allure.story("消息")  # allure子模块名称
    @allure.title("点击询价消息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_RFQ_Message(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_RFQ_Message()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_RFQ_Message()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_RFQ_Message()

    @allure.story("消息")  # allure子模块名称
    @allure.title("点击聊天消息")  # allure用例标题
    #@pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Chat_Message(self, app_page):
        LoginPage(app_page).login('13695632145', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Chat_Message()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Chat_Message()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_message()
            time.sleep(5)
            NewsPage(app_page).Click_Chat_Message()
        RolePage(app_page).Select_vendor_role()






