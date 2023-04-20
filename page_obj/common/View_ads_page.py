import random
import time

import allure

from common.basepage import BasePage
from page_lct.company import Company_home_page_lct


class ViewAdsPage(BasePage):
    def Click_Home_page_rotation_chart(self):
        # allure添加测试步骤
        with allure.step("点击公司首页广告轮播图"):
            print("点击公司首页广告轮播图")
        self.click_element(Company_home_page_lct.Home_page_rotation_chart)

    def Click_Home_page_large_exhibition_hall_rotation_map(self):
        # allure添加测试步骤
        time.sleep(5)
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.7,0.5,0.5,1000)
        with allure.step("点击公司首页大展厅广告轮播图"):
            print("点击公司首页大展厅广告轮播图")
        self.click_element(Company_home_page_lct.Home_page_large_exhibition_hall_rotation_map)

    def Click_Home_small_exhibition_hall_rotation_map(self):
        if self.wait_eleVisible(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_one) == True:
            number = random.randint(1,4)
            if number == 1:
                # allure添加测试步骤
                with allure.step("点击公司首页小展厅广告轮播图1"):
                    print("点击公司首页小展厅广告轮播图1")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_one)
            elif number == 2:
                with allure.step("点击公司首页小展厅广告轮播图2"):
                    print("点击公司首页小展厅广告轮播图2")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_two)
            elif number == 3:
                with allure.step("点击公司首页小展厅广告轮播图3"):
                    print("点击公司首页小展厅广告轮播图3")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_three)
            elif number == 4:
                with allure.step("点击公司首页小展厅广告轮播图4"):
                    print("点击公司首页小展厅广告轮播图4")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_four)
        else:
            self.swipe(0.5,0.7,0.5,0.5,1000)
            number = random.randint(1, 4)
            if number == 1:
                # allure添加测试步骤
                with allure.step("点击公司首页小展厅广告轮播图1"):
                    print("点击公司首页小展厅广告轮播图1")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_one)
            elif number == 2:
                with allure.step("点击公司首页小展厅广告轮播图2"):
                    print("点击公司首页小展厅广告轮播图2")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_two)
            elif number == 3:
                with allure.step("点击公司首页小展厅广告轮播图3"):
                    print("点击公司首页小展厅广告轮播图3")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_three)
            elif number == 4:
                with allure.step("点击公司首页小展厅广告轮播图4"):
                    print("点击公司首页小展厅广告轮播图4")
                self.click_element(Company_home_page_lct.Home_small_exhibition_hall_rotation_map_four)

    def Click_Homepage_banner_advertisement(self):
        self.swipe(0.5,0.8,0.5,0.2,1000)
        with allure.step("点击公司首页横幅广告轮播图"):
            print("点击公司首页横幅广告轮播图")
        self.click_element(Company_home_page_lct.Homepage_banner_advertisement)
