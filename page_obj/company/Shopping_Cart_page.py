import random
import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Album_permissions_lct, Figure_search_lct
from page_lct.company import Shopping_Cart_lct
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShoppingCartPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Shopping_Cart_lct.Back_button)

    def Code_scanning_query(self):
            # allure添加测试步骤
            with allure.step("点击扫码"):
                print("点击扫码")
            self.click_element(Shopping_Cart_lct.Scanning_code)
            with allure.step("拍照权限允许"):
                print("拍照权限允许")
            self.click_element(Album_permissions_lct.allow1)
            time.sleep(2)
            with allure.step("音频权限允许"):
                print("音频权限允许")
            self.click_element(Album_permissions_lct.allow2)
            time.sleep(2)
            with allure.step("文件权限允许"):
                print("文件权限允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Figure_search_lct.album0)

    def Keyword_search(self,app_page):
        # allure添加测试步骤
        keyword = Random_name.RandomName.RandomKeyword(app_page)
        with allure.step("输入关键字{}".format(keyword)):
            print("输入关键字{}".format(keyword))
        self.input_text(keyword,Shopping_Cart_lct.Please_enter_a_keyword)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(Shopping_Cart_lct.Search_button)

    def sort(self):
        # allure添加测试步骤
        for i in range(3):
            with allure.step("单价排序"):
                print("单价排序")
            self.click_element(Shopping_Cart_lct.Unit_price_sorting)
            time.sleep(2)
        for i in range(3):
            with allure.step("时间排序"):
                print("时间排序")
            self.click_element(Shopping_Cart_lct.Time_sorting)
            time.sleep(2)

    def Number_of_operation_boxes(self):
        # allure添加测试步骤
        Number_of_operation_boxes = random.choice(list(["加箱数","加箱数","加箱数"]))
        if Number_of_operation_boxes == "减箱数":
            with allure.step("点击减箱数"):
                print("点击减箱数")
            self.click_element(Shopping_Cart_lct.Reduce_the_number_of_boxes)
            toast_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((MobileBy.XPATH, ".//*[contains(@text,'箱数不能小于1')]")))
            if toast_element.text == "箱数不能小于1":
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Shopping_Cart_lct.Back_button)
        elif Number_of_operation_boxes == "填箱数":
            with allure.step("填写箱数"):
                print("填写箱数")
            number = random.randint(2,10)
            self.clear_text(Shopping_Cart_lct.Number_of_boxes_filled)
            self.input_text(number,Shopping_Cart_lct.Number_of_boxes_filled)
        elif Number_of_operation_boxes == "加箱数":
            number = random.randint(2, 10)
            with allure.step("加箱数:{}".format(number)):
                print("加箱数:".format(number))
            for i in range(number):
                self.click_element(Shopping_Cart_lct.Number_of_additional_boxes)
                time.sleep(2)

    def Tick_product(self):
        # allure添加测试步骤
        text1 = self.get_element_attribute("checked",Shopping_Cart_lct.Tick_product)
        if text1 == "true":
            with allure.step("取消勾选产品"):
                print("取消勾选产品")
            self.click_element(Shopping_Cart_lct.Tick_product)
        elif text1 == "false":
            with allure.step("勾选产品"):
                print("勾选产品")
            self.click_element(Shopping_Cart_lct.Tick_product)
        text2 = self.get_element_attribute("checked", Shopping_Cart_lct.Select_all)
        if text2 == "true":
            with allure.step("取消勾选全部"):
                print("取消勾选全部")
            self.click_element(Shopping_Cart_lct.Select_all)
        elif text2 == "false":
            with allure.step("勾选全部"):
                print("勾选全部")
            self.click_element(Shopping_Cart_lct.Select_all)

    def delete_product(self,app_page):
        # allure添加测试步骤
        with allure.step("点击删除"):
            print("点击删除")
        self.click_element(Shopping_Cart_lct.Delete_button)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == "确定":
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(Shopping_Cart_lct.determine)
        elif Cancel_or_Confirm == "取消":
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(Shopping_Cart_lct.cancel)

    def Generate_quotation(self):
        # allure添加测试步骤
        with allure.step("点击生成报价"):
            print("点击生成报价")
        self.click_element(Shopping_Cart_lct.Generate_quotation)


