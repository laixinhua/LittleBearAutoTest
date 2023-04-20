import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import product_area_lct


class threeDProductPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(product_area_lct.Back_button)

    def Query_product(self, app_page):
        # allure添加测试步骤
        with allure.step("搜索栏输入产品名称"):
            print("搜索栏输入产品名称")
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        self.input_text(keyword, product_area_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(product_area_lct.Search_button)

    def sort(self):
        for i in range(3):
            # allure添加测试步骤
            with allure.step("点击热度排序"):
                print("点击热度排序")
            self.click_element(product_area_lct.Heat_ranking)
            time.sleep(5)
        for i in range(3):
            # allure添加测试步骤
            with allure.step("点击单价排序"):
                print("点击单价排序")
            self.click_element(product_area_lct.Unit_price_sorting)
            time.sleep(5)
        for i in range(3):
            # allure添加测试步骤
            with allure.step("点击时间排序"):
                print("点击时间排序")
            self.click_element(product_area_lct.Time_sorting)
            time.sleep(5)

    def Collection(self):
        time.sleep(5)
        with allure.step("点击切换视图"):
            print("点击切换视图")
        self.click_element(product_area_lct.Switch_views)
        if self.wait_eleVisible(product_area_lct.Favorite_button) == True:
            with allure.step("点击收藏按钮"):
                print("点击收藏按钮")
            self.click_element(product_area_lct.Favorite_button)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(product_area_lct.Back_button)

    def View_product_pictures(self):
        time.sleep(5)
        if self.wait_eleVisible(product_area_lct.Product_picture) == True:
            with allure.step("点击产品图片"):
                print("点击产品图片")
            self.click_element(product_area_lct.Product_picture)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(product_area_lct.Back_button)

    def Additional_purchase(self):
        time.sleep(5)
        if self.wait_eleVisible(product_area_lct.Additional_purchase) == True:
            with allure.step("点击加购"):
                print("点击产品图片")
            self.click_element(product_area_lct.Additional_purchase)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(product_area_lct.Back_button)

    def add_to_cart(self):
        time.sleep(5)
        with allure.step("点击切换视图"):
            print("点击切换视图")
        self.click_element(product_area_lct.Switch_views)
        if self.wait_eleVisible(product_area_lct.add_to_cart) == True:
            with allure.step("点击加入购物车"):
                print("点击加入购物车")
            self.click_element(product_area_lct.add_to_cart)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(product_area_lct.Back_button)

    def shopping_cart_button(self):
        time.sleep(5)
        with allure.step("点击购物车按钮"):
            print("点击购物车按钮")
        self.click_element(product_area_lct.Shopping_cart_button)
