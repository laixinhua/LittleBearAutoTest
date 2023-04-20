import logging
import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("展厅首页")#allure添加模块区分
class TestExhibitionHallHomePage:
    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击头像")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Avatar(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Avatar()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击消息")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_message(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_message()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")#allure子模块名称
    @allure.title("点击玩具圈")#allure用例标题
    @pytest.mark.flaky(reruns=2,reruns_delay=3)#失败重跑
    def test_Click_toy_circle(self,app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_toy_circle()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击工作台")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_workbench(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_workbench()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击新品区")  # allure用例标题
    #@pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_New_product_area(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击3D产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_3D_product(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_3D_product()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击视频区")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Video_area(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Video_area()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击热销择样")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Video_area(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Hot_sales_sample_selection()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击产品总数")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Total_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Total_products()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击厂商总数")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Total_number_of_manufacturers(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Total_number_of_manufacturers()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击展厅热销产品-更多")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Hot_Products_in_the_Exhibition_Hall_More(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Hot_Products_in_the_Exhibition_Hall_More()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("随机点击展厅热销产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Randomly_click_the_hot_selling_products_in_the_exhibition_hall(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Randomly_click_the_hot_selling_products_in_the_exhibition_hall()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击最新择样公司-更多")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Latest_sample_company_more(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Latest_sample_company_more()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("随机点击最新择样公司")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Randomly_click_the_latest_sample_company(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Randomly_click_the_latest_sample_company()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("搜索最新择样公司")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Latest_sample_company_Search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Latest_sample_company_Search()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("点击最新入驻厂商-更多")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Latest_settled_manufacturers_more(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_Latest_settled_manufacturers_more()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("搜索最新入驻厂商")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Latest_settled_manufacturers_Search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Latest_settled_manufacturers_Search()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("展厅首页")  # allure子模块名称
    @allure.title("随机点击最新入驻厂商")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Randomly_click_the_latest_settled_manufacturer(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Randomly_click_the_latest_settled_manufacturer()
        logging.info("开始断言")
        time.sleep(5)




