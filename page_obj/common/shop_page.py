import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import shop_lct
from appium.webdriver.common.touch_action import TouchAction


class ShopPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(shop_lct.Back_button)

    def selcet_product(self,product_name):
        # allure添加测试步骤
        with allure.step("搜索栏输入产品名称"):
            print("搜索栏输入产品名称")
        self.input_text(product_name, shop_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(shop_lct.Search_button)

    def View_logo(self):
        # allure添加测试步骤
        with allure.step("查看logo"):
            print("查看logo")
        self.click_element(shop_lct.Logo_diagram)

    def copy_mobile_phone(self,app_page):
        time.sleep(2)
        # allure添加测试步骤
        with allure.step("长按手机号"):
            print("长按手机号")
        TouchAction(app_page).long_press(x=274,y=880).wait(2000).release().perform()
        with allure.step("点击复制"):
            print("点击复制")
        self.click_element(shop_lct.copy)
        time.sleep(2)
        with allure.step("长按搜索栏粘贴"):
            print("长按搜索栏粘贴")
        TouchAction(app_page).long_press(x=508,y=138).wait(2000).release().perform()
        #暂时无法定位到粘贴，跳过这个-_-!

    def location_address(self):
        if self.wait_eleVisible(shop_lct.navigation_button) == True:
            with allure.step("点击定位"):
                print("点击定位")
            self.click_element(shop_lct.navigation_button)
            if self.wait_eleVisible(shop_lct.Use_Baidu_map) == True:
                with allure.step("使用百度地图"):
                    print("使用百度地图")
                self.click_element(shop_lct.Use_Baidu_map)
                time.sleep(20)
            else:
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(shop_lct.Back_button)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(shop_lct.Back_button)

    def All_products_add_cart(self):
        if self.wait_eleVisible(shop_lct.All_products) == True:
            with allure.step("点击所有产品"):
                print("点击所有产品")
            self.click_element(shop_lct.All_products)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.7,0.5,0.5,1000)
            with allure.step("点击加购"):
                print("点击加购")
            self.click_element(shop_lct.Additional_purchase)
            time.sleep(5)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(shop_lct.Back_button)
    def Recommended_products_add_cart(self):
        if self.wait_eleVisible(shop_lct.All_products) == True:
            with allure.step("点击推荐产品"):
                print("点击推荐产品")
            self.click_element(shop_lct.Recommended_products)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.7,0.5,0.5,1000)
            with allure.step("点击加购"):
                print("点击加购")
            self.click_element(shop_lct.Additional_purchase)
            time.sleep(5)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(shop_lct.Back_button)

    def Video_products_add_cart(self):
        if self.wait_eleVisible(shop_lct.All_products) == True:
            with allure.step("点击视频产品"):
                print("点击推荐产品")
            self.click_element(shop_lct.Video_products)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.7,0.5,0.5,1000)
            with allure.step("点击加购"):
                print("点击加购")
            self.click_element(shop_lct.Additional_purchase)
            time.sleep(5)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(shop_lct.Back_button)

    def threeD_products_add_cart(self):
        if self.wait_eleVisible(shop_lct.All_products) == True:
            with allure.step("点击3D产品"):
                print("点击3D产品")
            self.click_element(shop_lct.threeD_products)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.7,0.5,0.5,1000)
            with allure.step("点击加购"):
                print("点击加购")
            self.click_element(shop_lct.Additional_purchase)
            time.sleep(5)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(shop_lct.Back_button)

    def Latest_products_add_cart(self):
        if self.wait_eleVisible(shop_lct.Latest_products) == True:
            with allure.step("点击最新产品"):
                print("点击最新产品")
            self.click_element(shop_lct.Latest_products)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.7,0.5,0.5,1000)
            with allure.step("点击加购"):
                print("点击加购")
            self.click_element(shop_lct.Additional_purchase)
            time.sleep(5)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(shop_lct.Back_button)

    def Random_additional_purchase(self,app_page):
        product_type = Random_name.RandomName.RandomSelectProductType(app_page)
        if product_type == "所有产品":
            self.All_products_add_cart()
        elif product_type == "推荐产品":
            self.Recommended_products_add_cart()
        elif product_type == "视频产品":
            self.Video_products_add_cart()
        elif product_type == "3D产品":
            self.threeD_products_add_cart()
        elif product_type == "最新产品":
            self.Latest_products_add_cart()

    def Collection(self):
        # with allure.step("点击切换视图"):
        #     print("点击切换视图")
        # self.click_element(shop_lct.Switch_views)
        with allure.step("点击产品跳转产品详情"):
            print("点击产品跳转产品详情")
        self.click_element(shop_lct.product)
        with allure.step("点击收藏"):
            print("点击收藏")
        self.click_element(shop_lct.Favorite_button)

    def add_cart(self):
        # with allure.step("点击切换视图"):
        #     print("点击切换视图")
        # self.click_element(shop_lct.Switch_views)
        with allure.step("点击加入购物车"):
            print("点击加入购物车")
        self.click_element(shop_lct.add_cart)

    def sort(self):
        for i in range(3):
            with allure.step("点击货号排序"):
                print("点击货号排序")
            self.click_element(shop_lct.Sort_item_No)
            time.sleep(2)
        for i in range(3):
            with allure.step("点击单价排序"):
                print("点击单价排序")
            self.click_element(shop_lct.Price_sort)
            time.sleep(2)
        for i in range(3):
            with allure.step("点击时间排序"):
                print("点击时间排序")
            self.click_element(shop_lct.Time_sorting)
            time.sleep(2)

    def Follow_the_store(self):
        with allure.step("点击关注按钮"):
            print("点击关注按钮")
        self.click_element(shop_lct.Follow_button)







