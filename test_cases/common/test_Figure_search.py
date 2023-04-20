import logging
import time

import allure
import pytest

from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.common.Crop_page import CropPage
from page_obj.common.Figure_search_page import FigureSearchPage
from page_obj.common.Select_Picture_page import SelectPicturePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("图搜模块")#allure添加模块区分
class TestFigureSearch:
    @allure.story("扫码搜索")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_Scan()
        FigureSearchPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("扫码搜索")  # allure子模块名称
    @allure.title("相册扫码")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_album0(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_Scan()
        FigureSearchPage(app_page).Click_album0()
        SelectPicturePage(app_page).Select_single_graph()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("扫码搜索")  # allure子模块名称
    @allure.title("点击图搜")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Figure_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_Scan()
        FigureSearchPage(app_page).Click_Figure_search()
        CropPage(app_page).Click_Crop_button()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("扫码搜索")  # allure子模块名称
    @allure.title("图搜-旋转")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Figure_search_Rotate(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_Scan()
        FigureSearchPage(app_page).Click_Figure_search()
        CropPage(app_page).Click_Rotate_button()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("相机搜索")  # allure子模块名称
    @allure.title("拍照搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_camera_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_camera()
        FigureSearchPage(app_page).Click_camera_search()
        CropPage(app_page).Click_Crop_button()
        time.sleep(10)
        logging.info("开始断言")



