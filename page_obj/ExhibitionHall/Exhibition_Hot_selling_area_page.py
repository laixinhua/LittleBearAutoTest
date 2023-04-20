import allure

from common.basepage import BasePage
from page_lct.common import product_area_lct


class ExhibitionHotSellingAreaPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(product_area_lct.Back_button)

    def Search_Products(self):
        # allure添加测试步骤
        with allure.step("输入产品名称"):
            print("输入产品名称")
        self.input_text("娃娃",product_area_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(product_area_lct.Search_button)

    def Product_Collection(self):
        # allure添加测试步骤
        with allure.step("点击切换列表"):
            print("点击切换列表")
        self.click_element(product_area_lct.Hot_sale_area_Switch_views)
        with allure.step("点击收藏按钮"):
            print("点击收藏按钮")
        self.click_element(product_area_lct.Favorite_button)

    def Switch_Month(self):
        # allure添加测试步骤
        with allure.step("点击月份"):
            print("点击月份")
        self.click_element(product_area_lct.Hot_sale_area_month)
        with allure.step("选择月份"):
            print("选择月份")
        self.click_element(product_area_lct.month)

