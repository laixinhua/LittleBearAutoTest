import random
import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Showroom_Homepage_lct, Album_permissions_lct, Figure_search_lct, Select_Picture_lct, \
    Crop_lct
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShowroomHomePage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Showroom_Homepage_lct.Back_button)

    def See_more(self):
        # allure添加测试步骤
        with allure.step("点击查看更多"):
            print("点击查看更多")
        self.click_element(Showroom_Homepage_lct.See_more)
        time.sleep(5)

    def Code_scanning_search(self):
        # allure添加测试步骤
        Product_or_manufacturer = random.choice(list(["产品","厂家"]))
        if Product_or_manufacturer == "产品":
            with allure.step("点击产品"):
                print("点击产品")
            self.click_element(Showroom_Homepage_lct.product)
        elif Product_or_manufacturer == "厂家":
            with allure.step("点击厂家"):
                print("点击厂家")
            self.click_element(Showroom_Homepage_lct.manufactor)
        with allure.step("点击产品扫码按钮"):
            print("点击产品扫码按钮")
        self.click_element(Showroom_Homepage_lct.Code_scanning_button)
        with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
            print("要允许小竹熊拍摄照片和录制视频吗？-允许")
        self.click_element(Album_permissions_lct.allow1)
        with allure.step("要允许小竹熊录制音频吗？-允许"):
            print("要允许小竹熊录制音频吗？-允许")
        self.click_element(Album_permissions_lct.allow2)
        with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
            print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
        self.click_element(Album_permissions_lct.allow)
        with allure.step("扫码-相册"):
            print("扫码-相册")
        self.click_element(Figure_search_lct.album0)
        with allure.step("选择图片"):
            print("选择图片")
        self.click_element(Select_Picture_lct.Select_Figure_two)
        with allure.step("点击完成"):
            print("点击完成")
        self.click_element(Select_Picture_lct.complete)

    def Keyword_search(self,app_page):
        # allure添加测试步骤
        Product_or_manufacturer = random.choice(list(["产品", "厂家"]))
        if Product_or_manufacturer == "产品":
            with allure.step("点击产品"):
                print("点击产品")
            self.click_element(Showroom_Homepage_lct.product)
            Product_name = Random_name.RandomName.RandomKeyword(app_page)
            with allure.step("输入产品名称:{}".format(Product_name)):
                print("输入产品名称:{}".format(Product_name))
            self.input_text(Product_name,Showroom_Homepage_lct.Search_bar)
        elif Product_or_manufacturer == "厂家":
            with allure.step("点击厂家"):
                print("点击厂家")
            self.click_element(Showroom_Homepage_lct.manufactor)
            Name_of_manufacturer = random.choice(list(["永辉达玩具厂","仲盛玩具厂","开智玩具","汇生","欣盛","广兴玩具","ch","hf","pg","yw","azb"]))
            with allure.step("输入厂商名称:{}".format(Name_of_manufacturer)):
                print("输入厂商名称:{}".format(Name_of_manufacturer))
            self.input_text(Name_of_manufacturer,Showroom_Homepage_lct.Please_enter_the_manufacturer_name)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Showroom_Homepage_lct.Search_button)
        time.sleep(5)

    def Settled_manufacturer(self):
        with allure.step("点击入驻厂家"):
            print("点击入驻厂家")
        self.click_element(Showroom_Homepage_lct.Settled_manufacturer)
        with allure.step("选择入驻厂家"):
            print("选择入驻厂家")
        self.click_element(Showroom_Homepage_lct.Settled_manufacturer1)
        time.sleep(5)

    def Inquiry_of_settled_manufacturers(self):
        with allure.step("点击入驻厂家"):
            print("点击入驻厂家")
        self.click_element(Showroom_Homepage_lct.Settled_manufacturer)
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.2,1000)
        Name_of_manufacturer = random.choice(
            list(["永辉达玩具厂", "仲盛玩具厂", "开智玩具", "汇生", "欣盛", "广兴玩具", "ch", "hf", "pg", "yw", "azb"]))
        with allure.step("输入厂商名称:{}".format(Name_of_manufacturer)):
            print("输入厂商名称:{}".format(Name_of_manufacturer))
        self.input_text(Name_of_manufacturer, Showroom_Homepage_lct.Please_enter_the_manufacturer_name)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(Showroom_Homepage_lct.Search_button1)
        time.sleep(5)

    def Exhibition_hall_category(self):
        with allure.step("点击展厅类目"):
            print("点击展厅类目")
        self.click_element(Showroom_Homepage_lct.Exhibition_hall_category)
        with allure.step("选择类目一"):
            print("选择类目一")
        self.click_element(Showroom_Homepage_lct.Exhibition_hall_category1)
        time.sleep(5)

    def Exhibition_hall_category_Product_query(self,app_page):
        with allure.step("点击展厅类目"):
            print("点击展厅类目")
        self.click_element(Showroom_Homepage_lct.Exhibition_hall_category)
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.2,1000)
        Product_name = Random_name.RandomName.RandomKeyword(app_page)
        with allure.step("输入产品名称:{}".format(Product_name)):
            print("输入产品名称:{}".format(Product_name))
        self.input_text(Product_name, Showroom_Homepage_lct.Please_enter_the_product_name)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(Showroom_Homepage_lct.Search_button2)
        time.sleep(5)