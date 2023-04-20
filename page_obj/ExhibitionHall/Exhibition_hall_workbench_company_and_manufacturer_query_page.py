import time

import allure
from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from page_lct.ExhibitionHall import Exhibition_hall_workbench_lct, Exhibition_workbench_Company_query_lct, \
    Exhibition_workbench_Manufacturer_query_lct
from page_lct.common import Album_permissions_lct, Select_Picture_lct
from appium.webdriver.common.touch_action import TouchAction

class ExhibitionHallWorkbenchPage(BasePage):
    def Company_query(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌安安",Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)

    def View_search_results(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌安安",Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击搜索结果"):
            print("点击搜索结果")
        self.click_element(Exhibition_workbench_Company_query_lct.search_result)

    def Search_by_graph(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("点击相机按钮"):
            print("点击相机按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Camera_button)
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
        else:
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)

    def Search_again_after_searching_by_image(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("点击相机按钮"):
            print("点击相机按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Camera_button)
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
            with allure.step("点击相机按钮"):
                print("点击相机按钮")
            self.click_element(Exhibition_workbench_Company_query_lct.Search_and_take_photos_button_by_image)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
        else:
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
            with allure.step("点击相机按钮"):
                print("点击相机按钮")
            self.click_element(Exhibition_workbench_Company_query_lct.Search_and_take_photos_button_by_image)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)

    def Delete_a_single_history(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌安安", Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Back_button)
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        time.sleep(2)
        with allure.step("长按单个历史记录"):
            print("长按单个历史记录")
        el = self.find_element(Exhibition_workbench_Company_query_lct.History)
        TouchAction(self.driver).long_press(el).perform()
        time.sleep(2)
        with allure.step("点击确定"):
            print("点击确定")
        self.click_element(Exhibition_workbench_Company_query_lct.determine)

    def Undelete_a_single_history(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌安安", Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Back_button)
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        time.sleep(2)
        with allure.step("长按单个历史记录"):
            print("长按单个历史记录")
        el = self.find_element(Exhibition_workbench_Company_query_lct.History)
        TouchAction(self.driver).long_press(el).perform()
        time.sleep(2)
        with allure.step("点击取消"):
            print("点击取消")
        self.click_element(Exhibition_workbench_Company_query_lct.cancel)

    def Delete_all_history(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌安安", Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Back_button)
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌康马", Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Back_button)
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("点击删除按钮"):
            print("点击删除按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.delete_button)
        with allure.step("点击确定"):
            print("点击确定")
        self.click_element(Exhibition_workbench_Company_query_lct.determine)

    def Cancel_deleting_all_history_records(self):
        # allure添加测试步骤
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌安安", Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Back_button)
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("在请输入公司名/电话/手机号码中输入-义乌安安"):
            print("在请输入公司名/电话/手机号码中输入-义乌安安")
        self.input_text("义乌康马", Exhibition_workbench_Company_query_lct.Please_enter_company_name_phone_mobile_number)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.Back_button)
        with allure.step("点击公司查询"):
            print("点击公司查询")
        self.click_element(Exhibition_hall_workbench_lct.Company_Query)
        with allure.step("点击删除按钮"):
            print("点击删除按钮")
        self.click_element(Exhibition_workbench_Company_query_lct.delete_button)
        with allure.step("点击取消"):
            print("点击取消")
        self.click_element(Exhibition_workbench_Company_query_lct.cancel)

    def Manufacturer_query(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("在请输入关键词中输入-奥航玩具厂"):
            print("在请输入关键词中输入-奥航玩具厂")
        self.input_text("奥航玩具厂",Exhibition_workbench_Manufacturer_query_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_button)

    def Enter_the_store(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("在请输入关键词中输入-奥航玩具厂"):
            print("在请输入关键词中输入-奥航玩具厂")
        self.input_text("奥航玩具厂",Exhibition_workbench_Manufacturer_query_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_button)
        with allure.step("点击进店"):
            print("点击进店")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.search_result)

    def Search_for_manufacturers_by_graph(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("点击相机按钮"):
            print("点击相机按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Camera_button)
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
        else:
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)

    def Search_the_manufacturer_again_according_to_the_figure(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("点击相机按钮"):
            print("点击相机按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Camera_button)
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
            with allure.step("点击相机按钮"):
                print("点击相机按钮")
            self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_and_take_photos_button_by_image)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
        else:
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
            with allure.step("点击相机按钮"):
                print("点击相机按钮")
            self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_and_take_photos_button_by_image)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)

    def Delete_single_vendor_search_history(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("在请输入关键词中输入-奥航玩具厂"):
            print("在请输入关键词中输入-奥航玩具厂")
        self.input_text("奥航玩具厂", Exhibition_workbench_Manufacturer_query_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Back_button)
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        time.sleep(2)
        with allure.step("长按单个历史记录"):
            print("长按单个历史记录")
        el = self.find_element(Exhibition_workbench_Manufacturer_query_lct.History)
        TouchAction(self.driver).long_press(el).perform()
        time.sleep(2)
        with allure.step("点击确定"):
            print("点击确定")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.determine)

    def Undelete_single_vendor_search_history(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("在请输入关键词中输入-奥航玩具厂"):
            print("在请输入关键词中输入-奥航玩具厂")
        self.input_text("奥航玩具厂", Exhibition_workbench_Manufacturer_query_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Back_button)
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        time.sleep(2)
        with allure.step("长按单个历史记录"):
            print("长按单个历史记录")
        el = self.find_element(Exhibition_workbench_Manufacturer_query_lct.History)
        TouchAction(self.driver).long_press(el).perform()
        time.sleep(2)
        with allure.step("点击取消"):
            print("点击取消")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.cancel)

    def Delete_all_vendor_search_history(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("在请输入关键词中输入-奥航玩具厂"):
            print("在请输入关键词中输入-奥航玩具厂")
        self.input_text("奥航玩具厂", Exhibition_workbench_Manufacturer_query_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Back_button)
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("点击删除按钮"):
            print("点击删除按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.delete_button)
        with allure.step("点击取消"):
            print("点击取消")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.determine)

    def Cancel_deleting_all_vendor_search_history(self):
        # allure添加测试步骤
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("在请输入关键词中输入-奥航玩具厂"):
            print("在请输入关键词中输入-奥航玩具厂")
        self.input_text("奥航玩具厂", Exhibition_workbench_Manufacturer_query_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Search_button)
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.Back_button)
        with allure.step("点击厂商查询"):
            print("点击厂商查询")
        self.click_element(Exhibition_hall_workbench_lct.Manufacturer_query)
        with allure.step("点击删除按钮"):
            print("点击删除按钮")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.delete_button)
        with allure.step("点击取消"):
            print("点击取消")
        self.click_element(Exhibition_workbench_Manufacturer_query_lct.cancel)



















