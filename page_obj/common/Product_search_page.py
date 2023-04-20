import time

import allure
from appium.webdriver.common.touch_action import TouchAction
from common import Random_name
from common.basepage import BasePage
from page_lct.common import Album_permissions_lct, Figure_search_lct, Product_search_lct, Crop_lct


class ProductSearchPage(BasePage):


    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Product_search_lct.Back_button)

    def Click_Vendor_search(self):
        # allure添加测试步骤
        with allure.step("点击厂商搜索"):
            print("点击厂商搜索")
        self.click_element(Product_search_lct.Vendor_search)

    def Click_Recommended_manufacturer(self):
        # allure添加测试步骤
        with allure.step("点击推荐厂商"):
            print("点击推荐厂商")
        self.click_element(Product_search_lct.Recommended_manufacturer)
        time.sleep(2)

    def Vendor_search(self,Vendor_name):
        # allure添加测试步骤
        with allure.step("点击厂商搜索"):
            print("点击厂商搜索")
        self.click_element(Product_search_lct.Vendor_search)
        with allure.step("输入厂商名称"):
            print("输入厂商名称")
        self.input_text(Vendor_name, Product_search_lct.Please_enter_a_keyword)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(Product_search_lct.search)
        time.sleep(2)

    def Click_Product_search(self):
        # allure添加测试步骤
        with allure.step("点击产品搜索"):
            print("点击产品搜索")
        self.click_element(Product_search_lct.Product_search)


    def Click_camera(self):
        # allure添加测试步骤
        with allure.step("点击相机"):
            print("点击相机")
        self.click_element(Product_search_lct.camera)
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
        with allure.step("点击拍照"):
            print("点击拍照")
        self.click_element(Figure_search_lct.photograph)
        with allure.step("点击完成"):
            print("点击完成")
        self.click_element(Crop_lct.complete)


    def Search(self,keyword):
        with allure.step("点击产品搜索"):
            print("点击产品搜索")
        self.click_element(Product_search_lct.Product_search)
        with allure.step("输入关键字"):
            print("输入关键字")
        self.input_text(keyword, Product_search_lct.Search_bar)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(Product_search_lct.search)
        # if self.wait_eleVisible(Product_search_lct.Keyword_recommendation) == True:
        #     with allure.step("点击关键词推荐"):
        #         print("点击关键词推荐")
        #     self.click_element(Product_search_lct.Keyword_one)
        #     time.sleep(5)
        # else:
        #     with allure.step("点击搜索"):
        #         print("点击搜索")
        #     self.click_element(Product_search_lct.Search_button)
        # time.sleep(5)

    def Click_History(self):
        if self.wait_eleVisible(Product_search_lct.History) == True:
            with allure.step("点击历史记录"):
                print("点击历史记录")
            self.click_element(Product_search_lct.History)
        else:
            with allure.step("点击搜索"):
                print("点击搜索")
            self.click_element(Product_search_lct.search)
            time.sleep(5)

    def Click_Delete(self,app_page):
        if self.wait_eleVisible(Product_search_lct.Delete_button) == True:
            with allure.step("点击删除"):
                print("点击删除")
            self.click_element(Product_search_lct.Delete_button)
            Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
            if Cancel_or_Confirm == "取消":
                with allure.step("点击取消"):
                    print("点击取消")
                self.click_element(Product_search_lct.cancel)
            elif Cancel_or_Confirm == "确定":
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(Product_search_lct.determine)
        else:
            with allure.step("点击搜索"):
                print("点击搜索")
            self.click_element(Product_search_lct.search)
            time.sleep(5)

    def Click_Long_press_Delete(self,app_page):
        if self.wait_eleVisible(Product_search_lct.History) == True:
            with allure.step("长按删除"):
                print("长按删除")
            #根据元素长按
            # TouchAction(app_page).long_press(Product_search_lct.History).perform().wait(3000)
            # self.click_element(Product_search_lct.History)
            #根据坐标长按
            #TouchAction(app_page).long_press(x=148,y=609).wait(2000).release().perform()
            el = self.find_element(Product_search_lct.History)
            TouchAction(self.driver).long_press(el).perform()
            Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
            if Cancel_or_Confirm == "取消":
                with allure.step("点击取消"):
                    print("点击取消")
                self.click_element(Product_search_lct.cancel)
            elif Cancel_or_Confirm == "确定":
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(Product_search_lct.determine)
        else:
            with allure.step("点击搜索"):
                print("点击搜索")
            self.click_element(Product_search_lct.search)
            time.sleep(5)





