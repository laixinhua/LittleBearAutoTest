import logging
import time

import allure
import pytest

from common import Random_name
from page_obj.common.product_page import ProductPage
from page_obj.company.Company_home_page import CompanyHomePage
from page_obj.common.Crop_page import CropPage
from page_obj.common.Product_search_page import ProductSearchPage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage


@allure.feature("产品搜索")#allure添加模块区分
class TestProductSearch:
    @allure.story("产品搜索")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        ProductSearchPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("产品搜索")  # allure子模块名称
    @allure.title("相机搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_camera_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        ProductSearchPage(app_page).Click_camera()
        #CropPage(app_page).Click_Crop_button() 页面已弃用
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品搜索")  # allure子模块名称
    @allure.title("关键字搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_keyword_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductSearchPage(app_page).Search(keyword)
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("产品搜索")  # allure子模块名称
    @allure.title("历史记录搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_History_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductSearchPage(app_page).Search(keyword)
        time.sleep(2)
        app_page.keyevent(4)
        time.sleep(2)
        app_page.keyevent(4)
        time.sleep(2)
        CompanyHomePage(app_page).Please_enter_keyword()
        ProductSearchPage(app_page).Click_History()
        time.sleep(5)
        logging.info("开始断言")

    @allure.story("产品搜索")  # allure子模块名称
    @allure.title("删除历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Delete(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductSearchPage(app_page).Search(keyword)
        time.sleep(2)
        app_page.keyevent(4)
        time.sleep(2)
        app_page.keyevent(4)
        CompanyHomePage(app_page).Please_enter_keyword()
        time.sleep(2)
        ProductSearchPage(app_page).Click_Delete(app_page)
        logging.info("开始断言")

    @allure.story("产品搜索")  # allure子模块名称
    @allure.title("长按删除历史记录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Long_press_Delete(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductSearchPage(app_page).Search(keyword)
        time.sleep(2)
        app_page.keyevent(4)
        time.sleep(2)
        app_page.keyevent(4)
        CompanyHomePage(app_page).Please_enter_keyword()
        time.sleep(2)
        ProductSearchPage(app_page).Click_Product_search()
        ProductSearchPage(app_page).Click_Long_press_Delete(app_page)
        logging.info("开始断言")

    @allure.story("厂商搜索")  # allure子模块名称
    @allure.title("厂商搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Vendor_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        Vendor_name = Random_name.RandomName.RandomCompanyName(app_page)
        ProductSearchPage(app_page).Vendor_search(Vendor_name)
        logging.info("开始断言")

    @allure.story("厂商搜索")  # allure子模块名称
    @allure.title("推荐厂商")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Recommended_manufacturer_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Please_enter_keyword()
        ProductSearchPage(app_page).Click_Vendor_search()
        ProductSearchPage(app_page).Click_Recommended_manufacturer()
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("列表返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Total_number_of_products_clicked(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(2)
        ProductPage(app_page).Click_Back_button()
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("拍照搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_photograph_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).photograph_search()
        #CropPage(app_page).Click_Crop_button() 页面已弃用
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("关键字搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductPage(app_page).Comprehensive_search(keyword)
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("搜索类型")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Select_Type(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductPage(app_page).Comprehensive_search_Select_Type(app_page,keyword)
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("是否模糊")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Select_Fuzzy_or_not(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        ProductPage(app_page).Comprehensive_search_Select_Fuzzy_or_not(app_page,keyword)
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("搜索产品货号")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_product_article_number(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Search_product_article_number()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("多产品货号搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Multiple_article_number_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Multiple_article_number_search()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("厂商搜索")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Vendor_name_search(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Vendor_name_search("成卓")
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("价格区间")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Price_range(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        price = Random_name.RandomName.RandomPrice(app_page)
        lowest_price = price[0]
        print("最低价为："+lowest_price)
        maximum_price = price[1]
        print("最高价为："+maximum_price)
        ProductPage(app_page).Comprehensive_search_Price_range(lowest_price,maximum_price)
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("时间段查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Time_period(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Time_period()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("包装方式查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Packaging_method(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Packaging_method(app_page)
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("搜索包装方式")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Search_packaging_method(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Search_packaging_method()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表") #allure子模块名称
    @allure.title("直接搜索包装方式") #allure用例标题
    @pytest.mark.flaky(reruns=2,reruns_delay=3)#失败重跑
    def test_Search_packaging_method_directly(self,app_page):
        LoginPage(app_page).login('13538262412','868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Search_packaging_method_directly()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("证书认证查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Certificate_authentication(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Certificate_authentication()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("外箱装量查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Outer_container_loading(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Outer_container_loading()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("外箱规格查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Outer_box_specification(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Outer_box_specification()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("是否授权查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Authorization_Type(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Comprehensive_search_Authorization_Type()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("是否有图查询")  # allure用例标题
    #@pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Query_whether_there_is_a_map(self, app_page):
        LoginPage(app_page).login('13538262412', '868385', app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Query_whether_there_is_a_map()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("产品排序")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Sort(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Sort()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("产品分类")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_classification(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).classification(app_page)
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("查看产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_View_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).View_products()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Additional_purchase(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Additional_purchase()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("产品收藏")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_Collection(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).Collection()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Comprehensive_search_add_to_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).add_to_cart()
        time.sleep(10)
        logging.info("开始断言")

    @allure.story("产品列表")  # allure子模块名称
    @allure.title("点击购物车按钮")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_shopping_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Total_number_of_products_clicked()
        time.sleep(10)
        ProductPage(app_page).shopping_cart()
        logging.info("开始断言")



