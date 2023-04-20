import logging
import time

import allure
import pytest

from page_obj.ExhibitionHall.Exhibition_New_product_area_page import ExhibitionNewProductAreaPage
from page_obj.ExhibitionHall.Exhibition_hall_Homepage_page import ExhibitionHallHomepagePage
from page_obj.ExhibitionHall.Operation_related_to_product_details_page import OperationRelatedToProductDetailsPage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("展厅产品详情")#allure添加模块区分
class TestProductDetail:
    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Click_Back_button()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("查看产品图片")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_product_pictures(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).View_product_pictures()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击收藏")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_Favorites_button(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Click_the_Favorites_button()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击截屏")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_the_screenshot(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Click_the_screenshot()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("截屏发给朋友")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Screenshot_send_to_friends(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Screenshot_send_to_friends()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("截屏发布玩具圈")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Screenshot_release_toy_circle(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Screenshot_release_toy_circle()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("截屏保存图片")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Screenshot_Save_Picture(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Screenshot_Save_Picture()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("截屏取消发送")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Screenshot_Cancel_sending(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Screenshot_Cancel_sending()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击店铺")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Shop(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Click_Shop()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击客服")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Customer_Service(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Click_Customer_Service()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击客服")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Send_product_information_to_customer_service(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Send_product_information_to_customer_service()
        logging.info("开始断言")
        time.sleep(5)

    @allure.story("产品详情")  # allure子模块名称
    @allure.title("点击发送")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Send(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_the_role_of_the_exhibition_hall()
        ExhibitionHallHomepagePage(app_page).Click_New_product_area()
        ExhibitionNewProductAreaPage(app_page).View_product_details()
        OperationRelatedToProductDetailsPage(app_page).Click_Send()
        logging.info("开始断言")
        time.sleep(5)



