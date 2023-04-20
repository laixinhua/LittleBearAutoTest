import logging
import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_Latest_sample_selection_company_page import \
    ExhibitionLatestSampleSelectionCompanyPage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("展厅最新择样公司")#allure添加模块区分
class TestLatestSampleSelectionCompany:
    @allure.story("最新择样")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Latest_sample_selection()
        ExhibitionLatestSampleSelectionCompanyPage(app_page).Click_Back_button()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("最新择样")  # allure子模块名称
    @allure.title("查询最新择样公司")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Query_the_latest_sample_company(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Latest_sample_selection()
        ExhibitionLatestSampleSelectionCompanyPage(app_page).Search()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("最新择样")  # allure子模块名称
    @allure.title("查看最新择样公司")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_the_latest_sample_company(self, app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Latest_sample_selection()
        ExhibitionLatestSampleSelectionCompanyPage(app_page).View_search_results()
        logging.info("开始断言")
        time.sleep(5)