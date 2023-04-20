import logging
import time

import allure
import pytest

from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("公司首页")#allure添加模块区分
class TestCompanyHomePage:
    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击扫描")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Scan(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_Scan()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击相机")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_camera(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_camera()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击请输入关键字")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Please_enter_keyword(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击首页大轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_on_the_home_page_of_the_big_rotation_chart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_on_the_home_page_of_the_big_rotation_chart()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击新品区")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_new_product_area(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击行业热销")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_industry_hot_sale(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_industry_hot_sale()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击甄选活动")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_to_select_activities(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_to_select_activities()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击品牌展厅-更多")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_brand_showroom_more(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        time.sleep(2)
        CompanyHomePage(app_page).Click_brand_showroom_more()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击首页大展厅轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击首页小展厅轮播图")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_small_exhibition_hall_rotation_map_on_the_home_page(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_small_exhibition_hall_rotation_map_on_the_home_page()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击GCC产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_GCC_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_GCC_products()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击3D产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_3D_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_3D_products()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击现货区")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_spot_area(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_spot_area()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击视频区")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_on_the_video_area(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_on_the_video_area()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击精选好物")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_to_select_good_items(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_to_select_good_items()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击精选好物产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_select_good_items_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_select_good_items_products()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击厂商主推精品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_manufacturer_main_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_manufacturer_main_products()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击厂商主推精品产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_manufacturer_main_product(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_the_manufacturer_main_product()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击产品数量")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Total_number_of_products_clicked(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击厂商总数")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Total_number_of_manufacturers_clicked(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击横幅广告")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_banner_ad(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_banner_ad()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击进店")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_to_enter_the_store(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_to_enter_the_store()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击消息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_message(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_message()
        logging.info("开始断言")

    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击玩具圈")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_toy_circle(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_toy_circle()
        logging.info("开始断言")


    @allure.story("首页展示")  # allure子模块名称
    @allure.title("点击工作台")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_workbench(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_workbench()
        logging.info("开始断言")