import random

import allure

from common.basepage import BasePage
from page_lct.company import Company_home_page_lct


class CompanyHomePage(BasePage):
    def Click_Scan(self):
        # allure添加测试步骤
        with allure.step("点击扫描"):
            print("点击扫描")
        self.click_element(Company_home_page_lct.scanning)

    def Click_camera(self):
        # allure添加测试步骤
        with allure.step("点击相机"):
            print("点击相机")
        self.click_element(Company_home_page_lct.camera)

    def Please_enter_keyword(self):
        # allure添加测试步骤
        with allure.step("请输入产品关键词"):
            print("请输入产品关键词")
        self.click_element(Company_home_page_lct.Please_enter_keyword)

    def Click_on_the_home_page_of_the_big_rotation_chart(self):
        # allure添加测试步骤
        with allure.step("点击首页大轮播图"):
            print("点击首页大轮播图")
        self.click_element(Company_home_page_lct.Home_page_rotation_chart)

    def Click_new_product_area(self):
        # allure添加测试步骤
        with allure.step("点击行业新品"):
            print("点击行业新品")
        self.click_element(Company_home_page_lct.New_product_area)

    def Click_the_industry_hot_sale(self):
        # allure添加测试步骤
        with allure.step("点击行业热销"):
            print("点击行业热销")
        self.click_element(Company_home_page_lct.Hot_sales_in_the_industry)

    def Click_to_select_activities(self):
        # allure添加测试步骤
        with allure.step("点击甄选活动"):
            print("点击甄选活动")
        self.click_element(Company_home_page_lct.Selection_activities)

    def Click_GCC_products(self):
        # allure添加测试步骤
        with allure.step("点击GCC产品"):
            print("点击GCC产品")
        self.click_element(Company_home_page_lct.GCC_products)

    def Click_3D_products(self):
        # allure添加测试步骤
        with allure.step("点击3D产品"):
            print("点击3D产品")
        self.click_element(Company_home_page_lct.three_D_products)

    def Click_the_spot_area(self):
        # allure添加测试步骤
        with allure.step("点击现货区"):
            print("点击现货区")
        self.click_element(Company_home_page_lct.Spot_area)

    def Click_on_the_video_area(self):
        # allure添加测试步骤
        with allure.step("点击视频区"):
            print("点击视频区")
        self.click_element(Company_home_page_lct.Video_area)

    def Click_to_select_good_items(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.7,0.5,0.3,1000)
        with allure.step("点击精选好物"):
            print("点击精选好物")
        self.click_element(Company_home_page_lct.Select_good_things)

    def Click_select_good_items_products(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.7,0.5,0.3,1000)
        with allure.step("点击精选好物的推荐产品"):
            print("点击精选好物的推荐产品")
        Select_good_things_products = random.choice(list([1,2,3,4]))
        if Select_good_things_products == 1:
            self.click_element(Company_home_page_lct.Select_good_things_products_1)
        elif Select_good_things_products == 2:
            self.click_element(Company_home_page_lct.Select_good_things_products_2)
        elif Select_good_things_products == 3:
            self.click_element(Company_home_page_lct.Select_good_things_products_3)
        else:
            self.click_element(Company_home_page_lct.Select_good_things_products_4)

    def Click_the_manufacturer_main_products(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5, 0.8, 0.5, 0.3, 1000)
        with allure.step("点击厂商主推精品"):
            print("点击厂商主推精品")
        self.click_element(Company_home_page_lct.Manufacturer_main_products)

    def Click_the_manufacturer_main_product(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.3,1000)
        with allure.step("点击厂商主推精品的产品"):
            print("点击厂商主推精品的产品")
        Manufacturer_main_products = random.choice(list([1,2,3,4]))
        if Manufacturer_main_products == 1:
            self.click_element(Company_home_page_lct.Manufacturer_main_products_1)
        elif Manufacturer_main_products == 2:
            self.click_element(Company_home_page_lct.Manufacturer_main_products_2)
        elif Manufacturer_main_products == 3:
            self.click_element(Company_home_page_lct.Manufacturer_main_products_3)
        else:
            self.click_element(Company_home_page_lct.Manufacturer_main_products_4)

    def Click_exposure_statistics(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.9,0.5,0.3,1000)
        with allure.step("点击产品曝光"):
            print("点击产品曝光")
        self.click_element(Company_home_page_lct.Total_exposure)

    def Total_number_of_products_clicked(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.9,0.5,0.3,1000)
        with allure.step("点击产品数量"):
            print("点击产品数量")
        self.click_element(Company_home_page_lct.Total_products)

    def Total_number_of_manufacturers_clicked(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.9,0.5,0.2,1000)
        with allure.step("点击厂商总数"):
            print("点击厂商总数")
        self.click_element(Company_home_page_lct.Total_number_of_manufacturers)

    def New_product_quantity(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.9,0.5,0.3,1000)
        with allure.step("点击新品数量"):
            print("点击新品数量")
        self.click_element(Company_home_page_lct.New_product_quantity)

    def Click_the_rotation_map_of_the_large_exhibition_hall_on_the_home_page(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.7,0.5,0.3,1000)
        with allure.step("点击首页大展厅轮播图"):
            print("点击首页大展厅轮播图")
        number = random.randint(1,2)
        if number == 1:
            self.click_element(Company_home_page_lct.Home_page_large_exhibition_hall_rotation_map_one)
        elif number == 2:
            self.click_element(Company_home_page_lct.Home_page_large_exhibition_hall_rotation_map_two)

    def Click_the_small_exhibition_hall_rotation_map_on_the_home_page(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.7,0.5,0.5,1000)
        with allure.step("点击首页小展厅轮播图"):
            print("点击首页小展厅轮播图")
        number = random.randint(1,3)
        if number == 1:
            self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_one)
        elif number == 2:
            self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_two)
        elif number == 3:
            self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_three)

    def Click_brand_showroom_more(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.7,0.5,0.3,1000)
        with allure.step("点击品牌展厅-更多"):
            print("点击品牌展厅-更多")
        self.click_element(Company_home_page_lct.Brand_showroom_more)

    def Click_banner_ad(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.2,1000)
        with allure.step("点击横幅广告"):
            print("点击横幅广告")
        self.click_element(Company_home_page_lct.Homepage_banner_advertisement)

    def Click_to_enter_the_store(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.9,0.5,0.2,1000)
        with allure.step("点击进店"):
            print("点击进店")
        self.click_element(Company_home_page_lct.Recommended_manufacturers)

    def Click_message(self):
        # allure添加测试步骤
        with allure.step("点击消息"):
            print("点击消息")
        self.click_element(Company_home_page_lct.news)

    def Click_toy_circle(self):
        # allure添加测试步骤
        with allure.step("点击玩具圈"):
            print("点击玩具圈")
        self.click_element(Company_home_page_lct.Toy_circle)

    def Click_workbench(self):
        # allure添加测试步骤
        with allure.step("点击工作台"):
            print("点击工作台")
        self.click_element(Company_home_page_lct.workbench)




