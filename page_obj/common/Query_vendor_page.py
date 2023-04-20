import random

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Query_vendor_lct, Album_permissions_lct
from page_lct.company import Company_home_page_lct


class QueryVendorPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Query_vendor_lct.Back_button)

    def Logo_search(self):
        # allure添加测试步骤
        with allure.step("点击相机按钮"):
            print("点击相机按钮")
        self.click_element(Query_vendor_lct.Camera_button)
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
        if self.wait_eleVisible(Album_permissions_lct.allow2) == True:
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
        if self.wait_eleVisible(Album_permissions_lct.allow) == True:
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)

    def Keyword_search(self,app_page):
        # allure添加测试步骤
        keyword = Random_name.RandomName.RandomCompanyName(app_page)
        with allure.step("关键词输入{}".format(keyword)):
            print("关键词输入{}".format(keyword))
        self.input_text(keyword,Query_vendor_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Query_vendor_lct.Search_button)

    def Search_fixed_vendor(self):
        # allure添加测试步骤
        Name_of_manufacturer_list = ["成卓玩具厂","czwjc"]
        Name_of_manufacturer = random.choice(list(Name_of_manufacturer_list))
        with allure.step("关键词输入{}".format(Name_of_manufacturer)):
            print("关键词输入{}".format(Name_of_manufacturer))
        self.input_text(Name_of_manufacturer,Query_vendor_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Query_vendor_lct.Search_button)
        with allure.step("点击搜索结果"):
            print("点击搜索结果")
        self.click_element(Query_vendor_lct.search_result)

    def History_Search(self):
        Name_of_manufacturer_list = ["成卓玩具厂", "czwjc"]
        Name_of_manufacturer = random.choice(list(Name_of_manufacturer_list))
        with allure.step("关键词输入{}".format(Name_of_manufacturer)):
            print("关键词输入{}".format(Name_of_manufacturer))
        self.input_text(Name_of_manufacturer, Query_vendor_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Query_vendor_lct.Search_button)
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Query_vendor_lct.Back_button)
        with allure.step("点击厂商总数"):
            print("点击厂商总数")
        self.click_element(Company_home_page_lct.Total_number_of_manufacturers)
        with allure.step("点击历史搜索"):
            print("点击历史搜索")
        self.click_element(Query_vendor_lct.History)

    def Delete_History_Search(self,app_page):
        Name_of_manufacturer_list = ["成卓玩具厂", "czwjc"]
        Name_of_manufacturer = random.choice(list(Name_of_manufacturer_list))
        with allure.step("关键词输入{}".format(Name_of_manufacturer)):
            print("关键词输入{}".format(Name_of_manufacturer))
        self.input_text(Name_of_manufacturer, Query_vendor_lct.Search_bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Query_vendor_lct.Search_button)
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Query_vendor_lct.Back_button)
        with allure.step("点击厂商总数"):
            print("点击厂商总数")
        self.click_element(Company_home_page_lct.Total_number_of_manufacturers)
        with allure.step("点击删除按钮"):
            print("点击删除按钮")
        self.click_element(Query_vendor_lct.Delete_button)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == "确定":
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(Query_vendor_lct.determine)
        elif Cancel_or_Confirm == "取消":
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(Query_vendor_lct.cancel)

    def Multiple_historical_searches(self):
        for i in range(11):
            Name_of_manufacturer = "我是厂商{}".format(i)
            with allure.step("关键词输入{}".format(Name_of_manufacturer)):
                print("关键词输入{}".format(Name_of_manufacturer))
            self.input_text(Name_of_manufacturer, Query_vendor_lct.Search_bar)
            with allure.step("点击搜索按钮"):
                print("点击搜索按钮")
            self.click_element(Query_vendor_lct.Search_button)
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(Query_vendor_lct.Back_button)
            with allure.step("点击厂商总数"):
                print("点击厂商总数")
            self.click_element(Company_home_page_lct.Total_number_of_manufacturers)












