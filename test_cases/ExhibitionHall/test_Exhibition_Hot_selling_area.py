import logging
import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_Hot_selling_area_page import ExhibitionHotSellingAreaPage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("展厅热销区")#allure添加模块区分
class TestExhibitionNewPorductArea:
    @allure.story("展厅热销")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_hot_sale_product()
        ExhibitionHotSellingAreaPage(app_page).Click_Back_button()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅热销")  # allure子模块名称
    @allure.title("产品搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_Products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_hot_sale_product()
        ExhibitionHotSellingAreaPage(app_page).Search_Products()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅热销")  # allure子模块名称
    @allure.title("产品收藏")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Product_Collection(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_hot_sale_product()
        ExhibitionHotSellingAreaPage(app_page).Product_Collection()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅热销")  # allure子模块名称
    @allure.title("切换月份")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Switch_Month(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_hot_sale_product()
        ExhibitionHotSellingAreaPage(app_page).Switch_Month()
        logging.info("开始断言")
        time.sleep(5)


