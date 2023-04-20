import time

import allure
import pytest

from page_obj.common.Select_role_page import RolePage
from page_obj.common.View_ads_page import ViewAdsPage
from page_obj.common.login_page import LoginPage


@allure.feature("查看广告")#allure添加模块区分
class TestViewAds:
    @allure.story("查看公司首页广告")  # allure子模块名称
    @allure.title("查看公司首页广告轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_Home_page_rotation_chart(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        ViewAdsPage(app_page).Click_Home_page_rotation_chart()

    @allure.story("查看广告")  # allure子模块名称
    @allure.title("查看公司首页大展厅广告轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_Home_page_large_exhibition_hall_rotation_map(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        ViewAdsPage(app_page).Click_Home_page_large_exhibition_hall_rotation_map()

    @allure.story("查看广告")  # allure子模块名称
    @allure.title("查看公司首页小展厅广告轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_Home_small_exhibition_hall_rotation_map(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        time.sleep(2)
        ViewAdsPage(app_page).Click_Home_small_exhibition_hall_rotation_map()

    @allure.story("查看广告")  # allure子模块名称
    @allure.title("查看公司首页横幅广告轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_Homepage_banner_advertisement(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        time.sleep(2)
        ViewAdsPage(app_page).Click_Homepage_banner_advertisement()