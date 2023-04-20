import time

import allure

from common.basepage import BasePage
from page_lct.common import product_area_lct


class Exhibition3DProductPage(BasePage):
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

    def Sorting_of_3D_products_in_the_exhibition_hall(self):
        # allure添加测试步骤
        for i in range(3):
            if i == 1:
                with allure.step("点击热度降序"):
                    print("点击热度降序")
                self.click_element(product_area_lct.Heat_ranking)
                time.sleep(2)
            elif i == 2:
                with allure.step("点击热度升序"):
                    print("点击热度升序")
                self.click_element(product_area_lct.Heat_ranking)
                time.sleep(2)
            else:
                with allure.step("点击热度恢复默认"):
                    print("点击热度恢复默认")
                self.click_element(product_area_lct.Heat_ranking)
                time.sleep(2)
        for i in range(3):
            if i == 1:
                with allure.step("点击单价降序"):
                    print("点击单价降序")
                self.click_element(product_area_lct.Unit_price_sorting)
                time.sleep(2)
            elif i == 2:
                with allure.step("点击单价升序"):
                    print("点击单价升序")
                self.click_element(product_area_lct.Unit_price_sorting)
                time.sleep(2)
            else:
                with allure.step("点击单价恢复默认"):
                    print("点击单价恢复默认")
                self.click_element(product_area_lct.Unit_price_sorting)
                time.sleep(2)
        for i in range(3):
            if i == 1:
                with allure.step("点击时间降序"):
                    print("点击时间降序")
                self.click_element(product_area_lct.Time_sorting)
                time.sleep(2)
            elif i == 2:
                with allure.step("点击时间升序"):
                    print("点击时间升序")
                self.click_element(product_area_lct.Time_sorting)
                time.sleep(2)
            else:
                with allure.step("点击时间恢复默认"):
                    print("点击时间恢复默认")
                self.click_element(product_area_lct.Time_sorting)
                time.sleep(2)

    def Product_Collection(self):
        # allure添加测试步骤
        with allure.step("点击切换列表"):
            print("点击切换列表")
        self.click_element(product_area_lct.Switch_views)
        with allure.step("点击收藏按钮"):
            print("点击收藏按钮")
        self.click_element(product_area_lct.Favorite_button)