import random
import re
import time

import allure
from common import Random_name
from common.basepage import BasePage
from page_lct.common import product_lct, Album_permissions_lct, Figure_search_lct, Crop_lct
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_lct.company import Shopping_Cart_lct


class ProductPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(product_lct.Back_button)

    def photograph_search(self):
        if self.wait_eleVisible(product_lct.Camera_button) == True:
            # allure添加测试步骤
            with allure.step("点击相机按钮"):
                print("点击相机按钮")
            self.click_element(product_lct.Camera_button)
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


    def keyword_search(self,keyword):
        if self.wait_eleVisible(product_lct.Search_bar) == True:
            # allure添加测试步骤
            with allure.step("点击输入关键词+空格可模糊搜索"):
                print("点击输入关键词+空格可模糊搜索")
            self.click_element(product_lct.Search_bar)
            # allure添加测试步骤
            with allure.step("输入关键字"):
                print("输入关键字")
            self.input_text(keyword,product_lct.Search_bar1)
            with allure.step("点击搜索"):
                print("点击搜索")
            self.click_element(product_lct.Search_button1)

    def Comprehensive_search(self,keyword):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("输入关键字:{keyword}".format(keyword=keyword)):
                print("输入关键字:{}".format(keyword))
            self.input_text(keyword,product_lct.Please_enter_keywords)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Comprehensive_search_Select_Type(self,app_page,keyword):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("输入关键字:{keyword}".format(keyword=keyword)):
                print("输入关键字:{}".format(keyword))
            self.input_text(keyword,product_lct.Please_enter_keywords)
            Select_Type = Random_name.RandomName.RandomSelectType(app_page)
            if Select_Type == "全部":
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Select_Type == "货号":
                with allure.step("取消勾选名称"):
                    print("取消勾选名称")
                self.click_element(product_lct.Search_type_name)
                with allure.step("取消勾选编号"):
                    print("取消勾选编号")
                self.click_element(product_lct.Search_type_number)
                with allure.step("取消勾选平台编号"):
                    print("取消勾选平台编号")
                self.click_element(product_lct.Search_type_platform_number)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Select_Type == "名称":
                with allure.step("取消勾选货号"):
                    print("取消勾选货号")
                self.click_element(product_lct.Search_type_article_number)
                with allure.step("取消勾选编号"):
                    print("取消勾选编号")
                self.click_element(product_lct.Search_type_number)
                with allure.step("取消勾选平台编号"):
                    print("取消勾选平台编号")
                self.click_element(product_lct.Search_type_platform_number)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Select_Type == "编号":
                with allure.step("取消勾选货号"):
                    print("取消勾选货号")
                self.click_element(product_lct.Search_type_article_number)
                with allure.step("取消勾选名称"):
                    print("取消勾选名称")
                self.click_element(product_lct.Search_type_name)
                with allure.step("取消勾选平台编号"):
                    print("取消勾选平台编号")
                self.click_element(product_lct.Search_type_platform_number)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Select_Type == "平台编号":
                with allure.step("取消勾选货号"):
                    print("取消勾选货号")
                self.click_element(product_lct.Search_type_article_number)
                with allure.step("取消勾选名称"):
                    print("取消勾选名称")
                self.click_element(product_lct.Search_type_name)
                with allure.step("取消勾选编号"):
                    print("取消勾选编号")
                self.click_element(product_lct.Search_type_number)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)

    def Comprehensive_search_Select_Fuzzy_or_not(self,app_page,keyword):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("输入关键字:{keyword}".format(keyword=keyword)):
                print("输入关键字:{}".format(keyword))
            self.input_text(keyword,product_lct.Please_enter_keywords)
            Fuzzy_or_not = Random_name.RandomName.RandomSelectFuzzy_or_not(app_page)
            if Fuzzy_or_not == "模糊":
                with allure.step("是否模糊-点击模糊"):
                    print("是否模糊-点击模糊")
                self.click_element(product_lct.Accurate_Fuzzy)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Fuzzy_or_not == "精准":
                with allure.step("是否模糊-点击精准"):
                    print("是否模糊-点击精准")
                self.click_element(product_lct.Accurate_accurate)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)

    def Search_product_article_number(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("点击产品货号展开"):
                print("点击产品货号展开")
            self.click_element(product_lct.Product_article_number_expand)
            with allure.step("在多货号查询;以,隔开中输入-测试"):
                print("在多货号查询;以,隔开中输入-测试")
            self.input_text("测试",product_lct.Multiple_article_number_query_Separated_by)
            with allure.step("点击产品货号收起"):
                print("点击产品货号收起")
            self.click_element(product_lct.Product_article_number_stowed)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Multiple_article_number_search(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("点击产品货号展开"):
                print("点击产品货号展开")
            self.click_element(product_lct.Product_article_number_expand)
            with allure.step("在多货号查询;以,隔开中输入-测试,娃娃,遥控"):
                print("在多货号查询;以,隔开中输入-测试,娃娃,遥控")
            self.input_text("测试,娃娃,遥控",product_lct.Multiple_article_number_query_Separated_by)
            with allure.step("点击产品货号收起"):
                print("点击产品货号收起")
            self.click_element(product_lct.Product_article_number_stowed)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)




    def Comprehensive_search_Vendor_name_search(self, Vendor_name):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("点击厂商名称展开"):
                print("点击厂商名称展开")
            self.click_element(product_lct.Vendor_name_expand)
            with allure.step("输入厂商名称"):
                print("输入厂商名称")
            self.input_text(Vendor_name,product_lct.Vendor_name_please_enter)
            with allure.step("点击厂商名称收起"):
                print("点击厂商名称收起")
            self.click_element(product_lct.Vendor_name_stowed)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Comprehensive_search_Price_range(self,lowest_price,maximum_price):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            with allure.step("点击价格区间展开"):
                print("点击价格区间展开")
            self.click_element(product_lct.Price_range_expand)
            with allure.step("输入最低价：{}".format(lowest_price)):
                print("输入最低价：{}".format(lowest_price))
            self.input_text(lowest_price,product_lct.Price_range_lowest_price)
            with allure.step("输入最高价:{}".format(maximum_price)):
                print("输入最高价：{}".format(maximum_price))
            self.input_text(maximum_price,product_lct.Price_range_maximum_price)
            if lowest_price > maximum_price:
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
                time.sleep(5)
                self.click_element(product_lct.Price_range_lowest_price_after_entry)
                price1 = self.get_text(product_lct.Price_range_lowest_price_after_entry)
                print(price1)
                # 123 光标移至末尾
                self.driver.keyevent(123)
                for i in range(0, len(price1)):
                    # 67 退格键
                    self.driver.keyevent(67)
                self.clear_text(product_lct.Price_range_lowest_price_after_entry)
                with allure.step("输入最低价：{}".format(maximum_price)):
                    print("输入最低价：{}".format(maximum_price))
                self.input_text(maximum_price, product_lct.Price_range_lowest_price)
                self.click_element(product_lct.Price_range_maximum_price_after_entry)
                price2 = self.get_text(product_lct.Price_range_maximum_price_after_entry)
                # 123 光标移至末尾
                self.driver.keyevent(123)
                for i in range(0, len(price2)):
                    # 67 退格键
                    self.driver.keyevent(67)
                self.clear_text(product_lct.Price_range_lowest_price_after_entry)
                with allure.step("输入最高价:{}".format(lowest_price)):
                    print("输入最高价：{}".format(lowest_price))
                self.input_text(lowest_price, product_lct.Price_range_maximum_price)
                with allure.step("点击价格区间收起"):
                    print("点击价格区间收起")
                self.click_element(product_lct.Price_range_close)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            else:
                with allure.step("点击价格区间收起"):
                    print("点击价格区间收起")
                self.click_element(product_lct.Price_range_close)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)

    def Comprehensive_search_Time_period(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.8,0.5,0.2,1000)
            with allure.step("点击时间段展开"):
                print("点击时间段展开")
            self.click_element(product_lct.Time_period_expand)
            with allure.step("选择开始时间"):
                print("选择开始时间")
            self.click_element(product_lct.Time_period_start_time)
            Select_time_type = random.choice(['全部','年','月','日'])
            if Select_time_type == '全部':
                self.swipe(0.2, 0.8, 0.2, 0.9, 1000)
                self.swipe(0.5, 0.8, 0.5, 0.9, 1000)
                self.swipe(0.8, 0.8, 0.8, 0.9, 1000)
            elif Select_time_type == "年":
                self.swipe(0.2, 0.8, 0.2, 0.9,1000)
            elif Select_time_type == "月":
                self.swipe(0.5, 0.8, 0.5, 0.9,1000)
            elif Select_time_type == "日":
                self.swipe(0.8, 0.8, 0.8, 0.9,1000)
            with allure.step("点击保存"):
                print("点击保存")
            self.click_element(product_lct.Time_period_save)
            with allure.step("选择结束时间"):
                print("选择结束时间")
            self.click_element(product_lct.Time_period_end_time)
            Select_time_type = random.choice(['全部', '年', '月', '日'])
            if Select_time_type == '全部':
                self.swipe(0.2, 0.8, 0.2, 0.9, 1000)
                self.swipe(0.5, 0.8, 0.5, 0.9, 1000)
                self.swipe(0.8, 0.8, 0.8, 0.9, 1000)
            elif Select_time_type == "年":
                self.swipe(0.2, 0.8, 0.2, 0.9, 1000)
            elif Select_time_type == "月":
                self.swipe(0.5, 0.8, 0.5, 0.9, 1000)
            elif Select_time_type == "日":
                self.swipe(0.8, 0.8, 0.8, 0.9, 1000)
            with allure.step("点击保存"):
                print("点击保存")
            self.click_element(product_lct.Time_period_save)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Comprehensive_search_Packaging_method(self,app_page):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.8,0.5,0.2,1000)
            with allure.step("点击包装方式展开"):
                print("点击包装方式展开")
            self.click_element(product_lct.Packaging_method_expand)
            with allure.step("点击从平台选择"):
                print("点击从平台选择")
            self.click_element(product_lct.Packaging_method_Select_from_platform)
            packaging_method = Random_name.RandomName.RandomPackagingMethod(app_page)
            if packaging_method == '展示盒':
                with allure.step("点击展示盒"):
                    print("点击展示盒")
                self.click_element(product_lct.Packaging_method_display_box)
            elif packaging_method == '开窗盒':
                with allure.step("点击开窗盒"):
                    print("点击开窗盒")
                self.click_element(product_lct.Packaging_method_window_box)
            elif packaging_method == '彩盒':
                with allure.step("点击彩盒"):
                    print("点击彩盒")
                self.click_element(product_lct.Packaging_method_color_box)
            elif packaging_method == '吸盒':
                with allure.step("点击吸盒"):
                    print("点击吸盒")
                self.click_element(product_lct.Packaging_method_suction_plate)
            elif packaging_method == 'PVG圆筒':
                with allure.step("点击PVG圆筒"):
                    print("点击PVG圆筒")
                self.click_element(product_lct.Packaging_method_PVC_cylinder)
            with allure.step("点击确认"):
                print("点击确认")
            self.click_element(product_lct.confirm)
            with allure.step("点击收起"):
                print("点击收起")
            self.click_element(product_lct.Packaging_method_stowed)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Search_packaging_method(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.8,0.5,0.2,1000)
            with allure.step("点击包装方式展开"):
                print("点击包装方式展开")
            self.click_element(product_lct.Packaging_method_expand)
            with allure.step("点击从平台选择"):
                print("点击从平台选择")
            self.click_element(product_lct.Packaging_method_Select_from_platform)
            with allure.step("在请输入关键词中输入-开窗"):
                print("在请输入关键词中输入-开窗")
            self.input_text("开窗",product_lct.Packaging_method_Please_enter_keywords)
            with allure.step("点击搜索按钮"):
                print("点击搜索按钮")
            self.click_element(product_lct.Packaging_method_Search_button)
            with allure.step("勾选开窗盒"):
                print("勾选开窗盒")
            self.click_element(product_lct.Packaging_method_window_box)
            with allure.step("点击确认"):
                print("点击确认")
            self.click_element(product_lct.confirm)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Search_packaging_method_directly(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.8,0.5,0.2,1000)
            with allure.step("点击包装方式展开"):
                print("点击包装方式展开")
            self.click_element(product_lct.Packaging_method_expand)
            with allure.step("在请输入关键词中输入-开窗盒"):
                print("在请输入关键词中输入-开窗盒")
            self.input_text("开窗盒",product_lct.Search_packaging_method_directly)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)


    def Comprehensive_search_Certificate_authentication(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.8,0.5,0.2,1000)
            with allure.step("点击证书认证展开"):
                print("点击证书认证展开")
            self.click_element(product_lct.Certificate_authentication_expand)
            with allure.step("输入证书名称"):
                print("输入证书名称")
            Certificate_name = "综合搜索中的证书认证是输入证书名称来搜索的"
            self.input_text(Certificate_name,product_lct.Certificate_authentication_please_enter)
            with allure.step("点击证书认证收起"):
                print("点击证书认证收起")
            self.click_element(product_lct.Certificate_authentication_Stow)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Comprehensive_search_Outer_container_loading(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.5,0.5,0.2,1000)
            with allure.step("点击外箱装量展开"):
                print("点击外箱装量展开")
            self.click_element(product_lct.Outer_container_loading_expand)
            with allure.step("输入外箱装量-最低"):
                print("输入外箱装量-最低")
            Minimum = random.randint(1,1000)
            self.input_text(Minimum,product_lct.Outer_container_capacity_Minimum)
            with allure.step("输入外箱装量-最高"):
                print("输入外箱装量-最高")
            Max = random.randint(1,1000)
            self.input_text(Max,product_lct.Outer_container_capacity_max)
            if Minimum > Max:
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
                time.sleep(5)
                self.click_element(product_lct.Outer_container_capacity_Minimum_After_input)
                Minimum = self.find_element(product_lct.Outer_container_capacity_Minimum_After_input).text
                # 123 光标移至末尾
                self.driver.keyevent(123)
                for i in range(0, len(Minimum)):
                    # 67 退格键
                    self.driver.keyevent(67)
                self.clear_text(product_lct.Outer_container_capacity_Minimum_After_input)
                with allure.step("输入外箱装量-最低：{}".format(Max)):
                    print("输入外箱装量-最低：{}".format(Max))
                self.input_text(Max, product_lct.Outer_container_capacity_Minimum)
                self.click_element(product_lct.Outer_container_capacity_max_After_input)
                Max = self.find_element(product_lct.Outer_container_capacity_max_After_input).text
                # 123 光标移至末尾
                self.driver.keyevent(123)
                for i in range(0, len(Max)):
                    # 67 退格键
                    self.driver.keyevent(67)
                self.clear_text(product_lct.Outer_container_capacity_max_After_input)
                with allure.step("输入外箱装量-最高:{}".format(Minimum)):
                    print("输入外箱装量-最高：{}".format(Minimum))
                self.input_text(Minimum, product_lct.Outer_container_capacity_max)
                with allure.step("点击外箱装量收起"):
                    print("点击外箱装量收起")
                self.click_element(product_lct.Outer_container_loading_stowed)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            else:
                with allure.step("点击外箱装量收起"):
                    print("点击外箱装量收起")
                self.click_element(product_lct.Outer_container_loading_stowed)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)


    def Comprehensive_search_Outer_box_specification(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.5,0.5,0.2,1000)
            with allure.step("点击外箱规格展开"):
                print("点击外箱规格展开")
            self.click_element(product_lct.Outer_box_specification_expand)
            with allure.step("输入外箱规格-长"):
                print("输入外箱规格-长")
            long = random.randint(1,10)
            self.input_text(long,product_lct.Outer_box_specification_long)
            with allure.step("输入外箱规格-宽"):
                print("输入外箱规格-宽")
            width = random.randint(1,10)
            self.input_text(width,product_lct.Outer_box_specification_width)
            with allure.step("输入外箱规格-高"):
                print("输入外箱规格-高")
            high = random.randint(1,10)
            self.input_text(high,product_lct.Outer_box_specification_high)
            with allure.step("点击收起"):
                print("点击收起")
            self.click_element(product_lct.Outer_box_specification_stowed)
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(product_lct.determine)

    def Comprehensive_search_Authorization_Type(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.5,0.5,0.2,1000)
            with allure.step("点击授权类型展开"):
                print("点击授权类型展开")
            self.click_element(product_lct.Product_Authorization_expand)
            with allure.step("点击下拉"):
                print("点击下拉")
            self.click_element(product_lct.Product_Authorization_drop_down)
            Authorization_Type = random.choice(["全部","已授权","未授权","不侵权","其他","已授权和未授权","已授权和不侵权","未授权和不侵权","已授权和未授权和其他","已授权和不侵权和其他","未授权和不侵权和其他",])
            if Authorization_Type == "全部":
                with allure.step("点击全部"):
                    print("点击全部")
                self.click_element(product_lct.Product_Authorization_all)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "已授权":
                with allure.step("点击已授权"):
                    print("点击已授权")
                self.click_element(product_lct.Product_Authorization_authorized)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "未授权":
                with allure.step("点击未授权"):
                    print("点击未授权")
                self.click_element(product_lct.Product_Authorization_unauthorized)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "不侵权":
                with allure.step("点击不侵权"):
                    print("点击不侵权")
                self.click_element(product_lct.Product_Authorization_non_infringement)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "已授权和未授权":
                with allure.step("点击已授权"):
                    print("点击已授权")
                self.click_element(product_lct.Product_Authorization_authorized)
                time.sleep(2)
                with allure.step("点击未授权"):
                    print("点击未授权")
                self.click_element(product_lct.Product_Authorization_unauthorized)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "已授权和不侵权":
                with allure.step("点击已授权"):
                    print("点击已授权")
                self.click_element(product_lct.Product_Authorization_authorized)
                time.sleep(2)
                with allure.step("点击不侵权"):
                    print("点击不侵权")
                self.click_element(product_lct.Product_Authorization_non_infringement)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "未授权和不侵权":
                with allure.step("点击未授权"):
                    print("点击未授权")
                self.click_element(product_lct.Product_Authorization_unauthorized)
                time.sleep(2)
                with allure.step("点击不侵权"):
                    print("点击不侵权")
                self.click_element(product_lct.Product_Authorization_non_infringement)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "已授权和未授权和其他":
                with allure.step("点击已授权"):
                    print("点击已授权")
                self.click_element(product_lct.Product_Authorization_authorized)
                time.sleep(2)
                with allure.step("点击未授权"):
                    print("点击未授权")
                self.click_element(product_lct.Product_Authorization_unauthorized)
                time.sleep(2)
                with allure.step("点击其他"):
                    print("点击其他")
                self.click_element(product_lct.Product_Authorization_other)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "已授权和不侵权和其他":
                with allure.step("点击已授权"):
                    print("点击已授权")
                self.click_element(product_lct.Product_Authorization_authorized)
                time.sleep(2)
                with allure.step("点击不侵权"):
                    print("点击不侵权")
                self.click_element(product_lct.Product_Authorization_non_infringement)
                time.sleep(2)
                with allure.step("点击其他"):
                    print("点击其他")
                self.click_element(product_lct.Product_Authorization_other)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Authorization_Type == "未授权和不侵权和其他":
                with allure.step("点击未授权"):
                    print("点击未授权")
                self.click_element(product_lct.Product_Authorization_unauthorized)
                time.sleep(2)
                with allure.step("点击不侵权"):
                    print("点击不侵权")
                self.click_element(product_lct.Product_Authorization_non_infringement)
                time.sleep(2)
                with allure.step("点击其他"):
                    print("点击其他")
                self.click_element(product_lct.Product_Authorization_other)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Product_Authorization_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)

    def Query_whether_there_is_a_map(self):
        if self.wait_eleVisible(product_lct.Comprehensive_search_button) == True:
            # allure添加测试步骤
            with allure.step("点击综合搜索"):
                print("点击综合搜索")
            self.click_element(product_lct.Comprehensive_search_button)
            time.sleep(2)
            with allure.step("上拉屏幕"):
                print("上拉屏幕")
            self.swipe(0.5,0.5,0.5,0.2,1000)
            with allure.step("点击是否有图展开"):
                print("点击是否有图展开")
            self.click_element(product_lct.Search_type_is_there_a_graph_expand)
            with allure.step("点击请选择"):
                print("点击请选择")
            self.click_element(product_lct.Search_type_is_there_a_graph_drop_down)
            Is_there_a_map = random.choice(["全部","有图","无图"])
            if Is_there_a_map == "全部":
                with allure.step("点击全部"):
                    print("点击全部")
                self.click_element(product_lct.Search_type_is_there_a_graph_all)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Search_type_is_there_a_graph_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Is_there_a_map == "无图":
                with allure.step("点击无图"):
                    print("点击无图")
                self.click_element(product_lct.Search_type_is_there_a_graph_No_picture)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Search_type_is_there_a_graph_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)
            elif Is_there_a_map == "有图":
                with allure.step("点击有图"):
                    print("点击有图")
                self.click_element(product_lct.Search_type_is_there_a_graph_With_pictures)
                time.sleep(2)
                with allure.step("点击确认"):
                    print("点击确认")
                self.click_element(product_lct.Search_type_is_there_a_graph_confirm)
                time.sleep(2)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(product_lct.determine)

    def Sort(self):
        for i in range(3):
            # allure添加测试步骤
            with allure.step("点击热度排序"):
                print("点击热度排序")
            self.click_element(product_lct.Heat_ranking)
            time.sleep(5)
        for i in range(3):
            # allure添加测试步骤
            with allure.step("点击单价排序"):
                print("点击单价排序")
            self.click_element(product_lct.Unit_price_sorting)
            time.sleep(5)
        for i in range(3):
            # allure添加测试步骤
            with allure.step("点击时间排序"):
                print("点击时间排序")
            self.click_element(product_lct.Time_sorting)
            time.sleep(5)

    def classification(self,app_page):
        # allure添加测试步骤
        with allure.step("点击分类"):
            print("点击分类")
        self.click_element(product_lct.classification)
        with allure.step("点击电动玩具"):
            print("点击电动玩具")
        self.click_element(product_lct.Classification_electric_toys)
        Secondary_Classification = Random_name.RandomName.RandomSecondaryClassification(app_page)
        if Secondary_Classification == "电动机器人":
            with allure.step("点击电动机器人"):
                print("点击电动机器人")
            self.click_element(product_lct.Classification_electric_toys_electric_robots)
        elif Secondary_Classification == "电动车":
            with allure.step("点击电动车"):
                print("点击电动车")
            self.click_element(product_lct.Classification_electric_toys_electric_vehicles)
        elif Secondary_Classification == "电动飞机":
            with allure.step("点击电动飞机"):
                print("点击电动飞机")
            self.click_element(product_lct.Classification_electric_toys_electric_aircraft)
        elif Secondary_Classification == "电动船":
            with allure.step("点击电动船"):
                print("点击电动船")
            self.click_element(product_lct.Classification_electric_toys_electric_boats)
        elif Secondary_Classification == "电动动物":
            with allure.step("点击电动动物"):
                print("点击电动动物")
            self.click_element(product_lct.Classification_electric_toys_electric_animals)
        elif Secondary_Classification == "电动摩托":
            with allure.step("点击电动摩托"):
                print("点击电动摩托")
            self.click_element(product_lct.Classification_electric_toys_electric_motorcycles)
        elif Secondary_Classification == "电动坦克":
            with allure.step("点击电动坦克"):
                print("点击电动坦克")
            self.click_element(product_lct.Classification_electric_toys_electric_tanks)
        elif Secondary_Classification == "电动娃娃":
            with allure.step("点击电动娃娃"):
                print("点击电动娃娃")
            self.click_element(product_lct.Classification_electric_toys_electric_dolls)
        time.sleep(2)
        with allure.step("点击确定"):
            print("点击确定")
        self.click_element(product_lct.determine)

    def View_products(self):
        with allure.step("点击产品图片"):
            print("点击产品图片")
        self.click_element(product_lct.Product_picture)

    def Additional_purchase(self):
        with allure.step("点击加购"):
            print("点击加购")
        self.click_element(product_lct.Additional_purchase)

    def Collection(self):
        with allure.step("点击切换视图"):
            print("点击切换视图")
        self.click_element(product_lct.Switch_views)
        with allure.step("点击收藏"):
            print("点击收藏")
        self.click_element(product_lct.Favorite_button)

    def add_to_cart(self):
        with allure.step("点击切换视图"):
            print("点击切换视图")
        self.click_element(product_lct.Switch_views)
        with allure.step("点击加入购物车"):
            print("点击加入购物车")
        self.click_element(product_lct.add_to_cart)

    def chat(self):
        with allure.step("点击切换视图"):
            print("点击切换视图")
        self.click_element(product_lct.Switch_views)
        with allure.step("点击聊天按钮"):
            print("点击聊天按钮")
        self.click_element(product_lct.chat)

    def shopping_cart(self):
        with allure.step("点击购物车按钮"):
            print("点击购物车按钮")
        self.click_element(product_lct.Shopping_cart_button)
        number = self.get_text(Shopping_Cart_lct.Shopping_Cart_Statistics)
        pattern = '\d+'
        p = re.compile(pattern)
        match = re.search(p,number)
        #print(type(match.group(0)))
        if int(match.group(0)) > 0 :
            print("购物车内有产品")
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(Shopping_Cart_lct.Back_button)
            with allure.step("点击加购"):
                print("点击加购")
            self.click_element(product_lct.Additional_purchase)
            with allure.step("点击购物车按钮"):
                print("点击购物车按钮")
            self.click_element(product_lct.Shopping_cart_button)













