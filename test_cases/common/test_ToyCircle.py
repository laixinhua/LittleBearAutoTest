import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.Toy_circle_page import ToyCirclePage
from page_obj.common.login_page import LoginPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage


class TestToyCircle:
    @allure.story("玩具圈")  # allure子模块名称
    @allure.title("发布玩具圈")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Release_toy_circle(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).Release_toy_circle()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).Release_toy_circle()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).Release_toy_circle()

    @allure.story("玩具圈")  # allure子模块名称
    @allure.title("发布玩具圈图片")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Release_toy_circle_picture(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).Release_toy_circle_picture()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).Release_toy_circle_picture()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).Release_toy_circle_picture()

    @allure.story("玩具圈")  # allure子模块名称
    @allure.title("查看玩具圈或资讯类型")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_toy_circle_or_information(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        role = RolePage(app_page).Random_Select_role(app_page)
        if role == "公司":
            CompanyHomePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).View_toy_circle_or_information()
        elif role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).View_toy_circle_or_information()
        elif role == "厂商":
            ManufacturerHomepagePage(app_page).Click_toy_circle()
            ToyCirclePage(app_page).View_toy_circle_or_information()
