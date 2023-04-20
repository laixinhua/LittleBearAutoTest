import logging
import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.ExhibitionHall.Exhibition_hall_workbench_company_and_manufacturer_query_page import ExhibitionHallWorkbenchPage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


class TestExhibitionWorkbenchManufacturerQuery:
    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("厂商查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_workbench_Manufacturer_query(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Manufacturer_query()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("访问店铺")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Enter_the_store(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Enter_the_store()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("按图搜索厂商")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_for_manufacturers_by_graph(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Search_for_manufacturers_by_graph()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("按图搜索后再次搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_the_manufacturer_again_according_to_the_figure(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Search_the_manufacturer_again_according_to_the_figure()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("删除单个厂商历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Delete_single_vendor_search_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Delete_single_vendor_search_history()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("取消删除单个厂商历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Undelete_single_vendor_search_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Undelete_single_vendor_search_history()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("删除全部厂商历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Delete_all_vendor_search_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Delete_all_vendor_search_history()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("取消删除全部厂商历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Cancel_deleting_all_vendor_search_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Cancel_deleting_all_vendor_search_history()
        logging.info("开始断言")
        time.sleep(5)




