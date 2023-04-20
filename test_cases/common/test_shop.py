import time

import allure
import pytest

from common import Random_name
from page_obj.common.Query_vendor_page import QueryVendorPage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.View_ads_page import ViewAdsPage
from page_obj.common.login_page import LoginPage
from page_obj.common.shop_page import ShopPage
from page_obj.company.Company_home_page import CompanyHomePage


@allure.feature("店铺模块")#allure添加模块区分
class TestShop:
    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self,app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()点击广告跳转店铺
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Click_Back_button()

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("产品查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_selcet_product(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        time.sleep(10)
        product_name = Random_name.RandomName.RandomKeyword(app_page)
        ShopPage(app_page).selcet_product(product_name)
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("查看logo")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_logo(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).View_logo()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("复制手机号")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_copy_mobile_phone(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).copy_mobile_phone(app_page)
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("定位地址")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_location_address(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).location_address()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("所有产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_All_products_add_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).All_products_add_cart()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("推荐产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Recommended_products_add_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Recommended_products_add_cart()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("视频产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Video_products_add_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Video_products_add_cart()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("3D产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_threeD_products_add_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).threeD_products_add_cart()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("最新产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Latest_products_add_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        # ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Latest_products_add_cart()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("随机产品专区加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Random_additional_purchase(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Random_additional_purchase(app_page)
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("产品收藏")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Collection(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Collection()
        time.sleep(5)
    #店铺内已弃用列表模式
    # @allure.story("店铺页面")  # allure子模块名称
    # @allure.title("加入购物车")  # allure用例标题
    # @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    # def test_add_cart(self, app_page):
    #     LoginPage(app_page).login('13538262412', '868385',app_page)
    #     RolePage(app_page).Select_company_role()
    #     #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
    #     CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
    #     QueryVendorPage(app_page).Search_fixed_vendor()
    #     ShopPage(app_page).add_cart()
    #     time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("点击排序")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_sort(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        #ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).sort()
        time.sleep(5)

    @allure.story("店铺页面")  # allure子模块名称
    @allure.title("关注店铺")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Follow_the_store(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        # ViewAdsPage(app_page).Click_Home_page_rotation_chart()
        CompanyHomePage(app_page).Total_number_of_manufacturers_clicked()
        QueryVendorPage(app_page).Search_fixed_vendor()
        ShopPage(app_page).Follow_the_store()
        time.sleep(5)