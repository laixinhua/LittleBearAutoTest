import logging

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Left_menu_bar_page import LeftMenuBarPage
from page_obj.manufacturer.Manufacturer_Homepage_page import ManufacturerHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.Toy_Circle_Collection_page import ToyCircleCollectionPage
from page_obj.common.login_page import LoginPage


@allure.feature("玩具圈收藏模块")#allure添加模块区分
class TestToyCircleCollection:
    @allure.story("玩具圈收藏")  # allure子模块名称
    @allure.title("玩具圈收藏返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Toy_Circle_Collection_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Toy_Circle_Collection()
            ToyCircleCollectionPage(app_page).Click_Back_button()
        elif Role == "公司":
            print("公司的玩具圈收藏已去掉")
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Toy_Circle_Collection()
            ToyCircleCollectionPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("玩具圈收藏")  # allure子模块名称
    @allure.title("玩具圈收藏删除")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Toy_Circle_Collection_Delete_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        Role = RolePage(app_page).Random_Select_role(app_page)
        if Role == "展厅":
            ExhibitionHallHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Toy_Circle_Collection()
            ToyCircleCollectionPage(app_page).Click_Delete_button(app_page)
        elif Role == "公司":
            print("公司的玩具圈收藏已去掉")
        elif Role == "厂商":
            ManufacturerHomepagePage(app_page).Click_Avatar()
            LeftMenuBarPage(app_page).Click_Toy_Circle_Collection()
            ToyCircleCollectionPage(app_page).Click_Delete_button(app_page)
        logging.info("开始断言")
