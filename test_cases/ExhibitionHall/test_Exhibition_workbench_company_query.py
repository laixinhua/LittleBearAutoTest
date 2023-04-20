import logging
import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.ExhibitionHall.Exhibition_hall_workbench_company_and_manufacturer_query_page import ExhibitionHallWorkbenchPage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


class TestExhibitionWorkbenchCompanyQuery:
    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("公司查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_workbench_Company_query(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Company_query()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("查看查询结果")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_search_results(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).View_search_results()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("按图搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_by_graph(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Search_by_graph()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("按图搜索后再次搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_again_after_searching_by_image(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Search_again_after_searching_by_image()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("删除单个历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Delete_a_single_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Delete_a_single_history()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("取消删除单个历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Undelete_a_single_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Undelete_a_single_history()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("删除全部历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Delete_all_history(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Delete_all_history()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅工作台")  # allure子模块名称
    @allure.title("取消删除全部历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Cancel_deleting_all_history_records(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        ExhibitionHallWorkbenchPage(app_page).Cancel_deleting_all_history_records()
        logging.info("开始断言")
        time.sleep(5)




