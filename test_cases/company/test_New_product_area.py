import allure
import pytest

from common import Random_name
from page_obj.common.New_product_area_page import NewProductAreaPage
from page_obj.common.Select_role_page import RolePage
from page_obj.common.login_page import LoginPage
from page_obj.company.Company_home_page import CompanyHomePage


@allure.feature("新品区")#allure添加模块区分
class TestNewProductArea:
    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("点击返回")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Back_button(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).Click_Back_button()

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("点击最新产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_Latest_products(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).Click_Latest_products()

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("点击24小时新品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Click_New_products_in_24_hours(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).Click_New_products_in_24_hours()

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("产品查询")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Query_product(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).Query_product(app_page)

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("排序操作")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_sort(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).sort(app_page)

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("产品收藏")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Collection(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).Collection(app_page)

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("查看产品")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_product_pictures(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).View_product_pictures(app_page)

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Additional_purchase(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).Additional_purchase(app_page)

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("产品加购")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_add_to_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).add_to_cart(app_page)

    @allure.story("公司首页新品区")  # allure子模块名称
    @allure.title("点击购物车")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_shopping_cart(self, app_page):
        LoginPage(app_page).login('13538262412', '868385',app_page)
        RolePage(app_page).Select_company_role()
        CompanyHomePage(app_page).Click_new_product_area()
        NewProductAreaPage(app_page).shopping_cart_button(app_page)





