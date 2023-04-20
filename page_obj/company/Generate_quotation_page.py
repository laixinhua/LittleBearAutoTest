import random
import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.company import Generate_quotation_lct
from page_obj.company.customer_management_page import CustomerManagementPage


class GenerateQuotationPage(BasePage):
    def Click_Back_button(self,app_page):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Generate_quotation_lct.Back_button)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == "确定":
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(Generate_quotation_lct.determine)
        elif Cancel_or_Confirm == "取消":
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(Generate_quotation_lct.cancel)

    def Generate_quotation(self,app_page):
        # allure添加测试步骤
        Switch_operator = random.choice(list(["是","否"]))
        time.sleep(5)
        if Switch_operator == "是":
            with allure.step("切换业务员"):
                print("切换业务员")
            self.click_element(Generate_quotation_lct.Select_salesperson)
            Select_salesman_randomly = random.choice(list(["业务员一","业务员二","业务员三"]))
            if Select_salesman_randomly == "业务员一":
                if self.wait_eleVisible(Generate_quotation_lct.Salesman_I) == True:
                    with allure.step("选择业务员一"):
                        print("选择业务员一")
                    self.click_element(Generate_quotation_lct.Salesman_I)
                else:
                    with allure.step("点击返回"):
                        print("点击返回")
                    self.driver.keyevent(4)
            elif Select_salesman_randomly == "业务员二":
                if self.wait_eleVisible(Generate_quotation_lct.Salesman_II) == True:
                    with allure.step("选择业务员二"):
                        print("选择业务员二")
                    self.click_element(Generate_quotation_lct.Salesman_II)
                else:
                    with allure.step("点击返回"):
                        print("点击返回")
                    self.driver.keyevent(4)
            elif Select_salesman_randomly == "业务员三":
                if self.wait_eleVisible(Generate_quotation_lct.Salesman_III) == True:
                    with allure.step("选择业务员三"):
                        print("选择业务员三")
                    self.click_element(Generate_quotation_lct.Salesman_III)
                else:
                    with allure.step("点击返回"):
                        print("点击返回")
                    self.driver.keyevent(4)
            time.sleep(5)
            with allure.step("选择客户"):
                print("选择客户")
            self.click_element(Generate_quotation_lct.Select_customer)
            if self.wait_eleVisible(Generate_quotation_lct.Customer_I) == True:
                with allure.step("选择客户一"):
                    print("选择客户一")
                self.click_element(Generate_quotation_lct.Customer_I)
            else:
                self.driver.keyevent(4)
                with allure.step("新增客户"):
                    print("新增客户")
                self.click_element(Generate_quotation_lct.customer_management)
                CustomerManagementPage(app_page).Add_customer(app_page)
                CustomerManagementPage(app_page).Click_Back_button()
                with allure.step("选择客户"):
                    print("选择客户")
                self.click_element(Generate_quotation_lct.Select_customer)
                if self.wait_eleVisible(Generate_quotation_lct.Customer_I) == True:
                    with allure.step("选择客户一"):
                        print("选择客户一")
                    self.click_element(Generate_quotation_lct.Customer_I)
                else:
                    self.driver.keyevent(4)
            with allure.step("填写备注"):
                print("填写备注")
            remarks = Random_name.RandomName.RandomRemarks(app_page)
            self.input_text(remarks,Generate_quotation_lct.remarks)
            with allure.step("选择默认方式"):
                print("选择默认方式")
            self.click_element(Generate_quotation_lct.Default_mode)
            Default_mode = random.choice(list(["报出厂价","美元","人民币"]))
            if Default_mode == "报出厂价":
                with allure.step("选择报出厂价"):
                    print("选择报出厂价")
                self.click_element(Generate_quotation_lct.Quoted_factory_price)
            elif Default_mode == "美元":
                with allure.step("选择美元"):
                    print("选择美元")
                self.click_element(Generate_quotation_lct.dollar)
            elif Default_mode == "人民币":
                with allure.step("选择人民币"):
                    print("选择人民币")
                self.click_element(Generate_quotation_lct.RMB)
            Generate_quotation_or_continue_filling = random.choice(list(["生成报价","继续添加"]))
            if Generate_quotation_or_continue_filling == "生成报价":
                with allure.step("生成报价"):
                    print("生成报价")
                self.click_element(Generate_quotation_lct.Confirm_to_generate_quotation)
            elif Generate_quotation_or_continue_filling == "继续添加":
                with allure.step("选择报价方式"):
                    print("选择报价方式")
                self.click_element(Generate_quotation_lct.Quotation_method)
                Quotation_method = random.choice(list(["FOB","FOB SHANTOU","FOB SHENZHEN","出厂价"]))
                if Quotation_method == "FOB":
                    with allure.step("选择报价公式为：FOB"):
                        print("选择报价公式为：FOB")
                    self.click_element(Generate_quotation_lct.FOB)
                elif Quotation_method == "FOB SHANTOU":
                    with allure.step("选择报价公式为：FOB SHANTOU"):
                        print("选择报价公式为：FOB SHANTOU")
                    self.click_element(Generate_quotation_lct.FOB_SHANTOU)
                elif Quotation_method == "FOB SHENZHEN":
                    with allure.step("选择报价公式为：FOB SHENZHEN"):
                        print("选择报价公式为：FOB SHENZHEN")
                    self.click_element(Generate_quotation_lct.FOB_SHENZHEN)
                with allure.step("输入利润:15%"):
                    print("输入利润:15%")
                self.clear_text(Generate_quotation_lct.profit)
                self.input_text("15",Generate_quotation_lct.profit)
                with allure.step("选择币种"):
                    print("选择币种")
                self.click_element(Generate_quotation_lct.currency)
                currency = random.choice(list(["RMB","USD","HKD","EUR"]))
                if currency == "RMB":
                    with allure.step("选择币种-RMB"):
                        print("选择币种-RMB")
                    self.click_element(Generate_quotation_lct.currency_RMB)
                elif currency == "USD":
                    with allure.step("选择币种-USD"):
                        print("选择币种-USD")
                    self.click_element(Generate_quotation_lct.currency_USD)
                elif currency == "HKD":
                    with allure.step("选择币种-HKD"):
                        print("选择币种-HKD")
                    self.click_element(Generate_quotation_lct.currency_HKD)
                elif currency == "EUR":
                    with allure.step("选择币种-EUR"):
                        print("选择币种-EUR")
                    self.click_element(Generate_quotation_lct.currency_EUR)
                with allure.step("输入总费用:100000"):
                    print("输入总费用:100000")
                self.clear_text(Generate_quotation_lct.Total_cost)
                self.input_text("100000",Generate_quotation_lct.Total_cost)
                with allure.step("输入汇率:0.7"):
                    print("输入汇率:0.7")
                self.clear_text(Generate_quotation_lct.exchange_rate)
                self.input_text("0.7",Generate_quotation_lct.exchange_rate)
                with allure.step("选择每车尺码"):
                    print("选择每车尺码")
                self.click_element(Generate_quotation_lct.Size_per_car)
                Size_per_car = random.choice(list(["28","54","68","86"]))
                if Size_per_car == "28":
                    with allure.step("选择每车尺码-28"):
                        print("选择每车尺码-28")
                    self.click_element(Generate_quotation_lct.Size_per_car_28)
                elif Size_per_car == "54":
                    with allure.step("选择每车尺码-54"):
                        print("选择每车尺码-54")
                    self.click_element(Generate_quotation_lct.Size_per_car_54)
                elif Size_per_car == "68":
                    with allure.step("选择每车尺码-68"):
                        print("选择每车尺码-68")
                    self.click_element(Generate_quotation_lct.Size_per_car_68)
                elif Size_per_car == "86":
                    with allure.step("选择每车尺码-86"):
                        print("选择每车尺码-86")
                    self.click_element(Generate_quotation_lct.Size_per_car_86)
                with allure.step("选择小数位数"):
                    print("选择小数位数")
                self.click_element(Generate_quotation_lct.Decimal_places)
                Decimal_places = random.choice(list(["0","1","2","3","4"]))
                if Decimal_places == "0":
                    with allure.step("选择小数位数-0"):
                        print("选择小数位数-0")
                    self.click_element(Generate_quotation_lct.Decimal_places_0)
                elif Decimal_places == "1":
                    with allure.step("选择小数位数-1"):
                        print("选择小数位数-1")
                    self.click_element(Generate_quotation_lct.Decimal_places_1)
                elif Decimal_places == "2":
                    with allure.step("选择小数位数-2"):
                        print("选择小数位数-2")
                    self.click_element(Generate_quotation_lct.Decimal_places_2)
                elif Decimal_places == "3":
                    with allure.step("选择小数位数-3"):
                        print("选择小数位数-3")
                    self.click_element(Generate_quotation_lct.Decimal_places_3)
                elif Decimal_places == "4":
                    with allure.step("选择小数位数-4"):
                        print("选择小数位数-4")
                    self.click_element(Generate_quotation_lct.Decimal_places_4)
                time.sleep(2)
                with allure.step("上拉屏幕"):
                    print("上拉屏幕")
                self.swipe(0.5, 0.9, 0.5, 0.2, 1000)
                with allure.step("选择取舍方式"):
                    print("选择取舍方式")
                self.click_element(Generate_quotation_lct.Choice_method)
                Choice_method = random.choice(list(["全收","四舍五入","全舍"]))
                if Choice_method == "全收":
                    with allure.step("选择取舍方式-全收"):
                        print("选择取舍方式-全收")
                    self.click_element(Generate_quotation_lct.Choice_method_Full_collection)
                elif Choice_method == "四舍五入":
                    with allure.step("选择取舍方式-四舍五入"):
                        print("选择取舍方式-四舍五入")
                    self.click_element(Generate_quotation_lct.Choice_method_rounding)
                elif Choice_method == "全舍":
                    with allure.step("选择取舍方式-全舍"):
                        print("选择取舍方式-全舍")
                    self.click_element(Generate_quotation_lct.Choice_method_Whole_house)
                with allure.step("价格小于输入100"):
                    print("价格小于输入100")
                self.input_text("100",Generate_quotation_lct.Price_less_than)
                with allure.step("价格小于-小数位数"):
                    print("价格小于-小数位数")
                self.click_element(Generate_quotation_lct.Price_less_than_decimal_places)
                decimal_places = random.choice(list(["0","1","2","3","4"]))
                if decimal_places == "0":
                    with allure.step("选择价格小于-小数位数0"):
                        print("选择价格小于-小数位数0")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_0)
                elif decimal_places == "1":
                    with allure.step("选择价格小于-小数位数1"):
                        print("选择价格小于-小数位数1")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_1)
                elif decimal_places == "2":
                    with allure.step("选择价格小于-小数位数2"):
                        print("选择价格小于-小数位数1")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_2)
                elif decimal_places == "3":
                    with allure.step("选择价格小于-小数位数3"):
                        print("选择价格小于-小数位数3")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_3)
                elif decimal_places == "4":
                    with allure.step("选择价格小于-小数位数4"):
                        print("选择价格小于-小数位数4")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_4)
                with allure.step("确定生成报价"):
                    print("确定生成报价")
                self.click_element(Generate_quotation_lct.Confirm_to_generate_quotation)
        else:
            with allure.step("选择客户"):
                print("选择客户")
            self.click_element(Generate_quotation_lct.Select_customer)
            if self.wait_eleVisible(Generate_quotation_lct.Customer_I) == True:
                with allure.step("选择客户一"):
                    print("选择客户一")
                self.click_element(Generate_quotation_lct.Customer_I)
            else:
                self.driver.keyevent(4)
                with allure.step("新增客户"):
                    print("新增客户")
                self.click_element(Generate_quotation_lct.customer_management)
                CustomerManagementPage(app_page).Add_customer(app_page)
                CustomerManagementPage(app_page).Click_Back_button()
                with allure.step("选择客户"):
                    print("选择客户")
                self.click_element(Generate_quotation_lct.Select_customer)
                if self.wait_eleVisible(Generate_quotation_lct.Customer_I) == True:
                    with allure.step("选择客户一"):
                        print("选择客户一")
                    self.click_element(Generate_quotation_lct.Customer_I)
                else:
                    self.driver.keyevent(4)
            with allure.step("填写备注"):
                print("填写备注")
            remarks = Random_name.RandomName.RandomRemarks(app_page)
            self.input_text(remarks,Generate_quotation_lct.remarks)
            with allure.step("选择默认方式"):
                print("选择默认方式")
            self.click_element(Generate_quotation_lct.Default_mode)
            Default_mode = random.choice(list(["报出厂价","美元","人民币"]))
            if Default_mode == "报出厂价":
                with allure.step("选择报出厂价"):
                    print("选择报出厂价")
                self.click_element(Generate_quotation_lct.Quoted_factory_price)
            elif Default_mode == "美元":
                with allure.step("选择美元"):
                    print("选择美元")
                self.click_element(Generate_quotation_lct.dollar)
            elif Default_mode == "人民币":
                with allure.step("选择人民币"):
                    print("选择人民币")
                self.click_element(Generate_quotation_lct.RMB)
            Generate_quotation_or_continue_filling = random.choice(list(["生成报价","继续添加"]))
            if Generate_quotation_or_continue_filling == "生成报价":
                with allure.step("生成报价"):
                    print("生成报价")
                self.click_element(Generate_quotation_lct.Confirm_to_generate_quotation)
            elif Generate_quotation_or_continue_filling == "继续添加":
                with allure.step("选择报价方式"):
                    print("选择报价方式")
                self.click_element(Generate_quotation_lct.Quotation_method)
                Quotation_method = random.choice(list(["FOB","FOB SHANTOU","FOB SHENZHEN","出厂价"]))
                if Quotation_method == "FOB":
                    with allure.step("选择报价公式为：FOB"):
                        print("选择报价公式为：FOB")
                    self.click_element(Generate_quotation_lct.FOB)
                elif Quotation_method == "FOB SHANTOU":
                    with allure.step("选择报价公式为：FOB SHANTOU"):
                        print("选择报价公式为：FOB SHANTOU")
                    self.click_element(Generate_quotation_lct.FOB_SHANTOU)
                elif Quotation_method == "FOB SHENZHEN":
                    with allure.step("选择报价公式为：FOB SHENZHEN"):
                        print("选择报价公式为：FOB SHENZHEN")
                    self.click_element(Generate_quotation_lct.FOB_SHENZHEN)
                with allure.step("输入利润:15%"):
                    print("输入利润:15%")
                self.clear_text(Generate_quotation_lct.profit)
                self.input_text("15",Generate_quotation_lct.profit)
                with allure.step("选择币种"):
                    print("选择币种")
                self.click_element(Generate_quotation_lct.currency)
                currency = random.choice(list(["RMB","USD","HKD","EUR"]))
                if currency == "RMB":
                    with allure.step("选择币种-RMB"):
                        print("选择币种-RMB")
                    self.click_element(Generate_quotation_lct.currency_RMB)
                elif currency == "USD":
                    with allure.step("选择币种-USD"):
                        print("选择币种-USD")
                    self.click_element(Generate_quotation_lct.currency_USD)
                elif currency == "HKD":
                    with allure.step("选择币种-HKD"):
                        print("选择币种-HKD")
                    self.click_element(Generate_quotation_lct.currency_HKD)
                elif currency == "EUR":
                    with allure.step("选择币种-EUR"):
                        print("选择币种-EUR")
                    self.click_element(Generate_quotation_lct.currency_EUR)
                with allure.step("输入总费用:100000"):
                    print("输入总费用:100000")
                self.clear_text(Generate_quotation_lct.Total_cost)
                self.input_text("100000",Generate_quotation_lct.Total_cost)
                with allure.step("输入汇率:0.7"):
                    print("输入汇率:0.7")
                self.clear_text(Generate_quotation_lct.exchange_rate)
                self.input_text("0.7",Generate_quotation_lct.exchange_rate)
                with allure.step("选择每车尺码"):
                    print("选择每车尺码")
                self.click_element(Generate_quotation_lct.Size_per_car)
                Size_per_car = random.choice(list(["28","54","68","86"]))
                if Size_per_car == "28":
                    with allure.step("选择每车尺码-28"):
                        print("选择每车尺码-28")
                    self.click_element(Generate_quotation_lct.Size_per_car_28)
                elif Size_per_car == "54":
                    with allure.step("选择每车尺码-54"):
                        print("选择每车尺码-54")
                    self.click_element(Generate_quotation_lct.Size_per_car_54)
                elif Size_per_car == "68":
                    with allure.step("选择每车尺码-68"):
                        print("选择每车尺码-68")
                    self.click_element(Generate_quotation_lct.Size_per_car_68)
                elif Size_per_car == "86":
                    with allure.step("选择每车尺码-86"):
                        print("选择每车尺码-86")
                    self.click_element(Generate_quotation_lct.Size_per_car_86)
                with allure.step("选择小数位数"):
                    print("选择小数位数")
                self.click_element(Generate_quotation_lct.Decimal_places)
                Decimal_places = random.choice(list(["0","1","2","3","4"]))
                if Decimal_places == "0":
                    with allure.step("选择小数位数-0"):
                        print("选择小数位数-0")
                    self.click_element(Generate_quotation_lct.Decimal_places_0)
                elif Decimal_places == "1":
                    with allure.step("选择小数位数-1"):
                        print("选择小数位数-1")
                    self.click_element(Generate_quotation_lct.Decimal_places_1)
                elif Decimal_places == "2":
                    with allure.step("选择小数位数-2"):
                        print("选择小数位数-2")
                    self.click_element(Generate_quotation_lct.Decimal_places_2)
                elif Decimal_places == "3":
                    with allure.step("选择小数位数-3"):
                        print("选择小数位数-3")
                    self.click_element(Generate_quotation_lct.Decimal_places_3)
                elif Decimal_places == "4":
                    with allure.step("选择小数位数-4"):
                        print("选择小数位数-4")
                    self.click_element(Generate_quotation_lct.Decimal_places_4)
                time.sleep(2)
                with allure.step("上拉屏幕"):
                    print("上拉屏幕")
                self.swipe(0.5,0.9,0.5,0.2,1000)
                with allure.step("选择取舍方式"):
                    print("选择取舍方式")
                self.click_element(Generate_quotation_lct.Choice_method)
                Choice_method = random.choice(list(["全收","四舍五入","全舍"]))
                if Choice_method == "全收":
                    with allure.step("选择取舍方式-全收"):
                        print("选择取舍方式-全收")
                    self.click_element(Generate_quotation_lct.Choice_method_Full_collection)
                elif Choice_method == "四舍五入":
                    with allure.step("选择取舍方式-四舍五入"):
                        print("选择取舍方式-四舍五入")
                    self.click_element(Generate_quotation_lct.Choice_method_rounding)
                elif Choice_method == "全舍":
                    with allure.step("选择取舍方式-全舍"):
                        print("选择取舍方式-全舍")
                    self.click_element(Generate_quotation_lct.Choice_method_Whole_house)
                with allure.step("价格小于输入100"):
                    print("价格小于输入100")
                self.input_text("100",Generate_quotation_lct.Price_less_than)
                with allure.step("价格小于-小数位数"):
                    print("价格小于-小数位数")
                self.click_element(Generate_quotation_lct.Price_less_than_decimal_places)
                decimal_places = random.choice(list(["0","1","2","3","4"]))
                if decimal_places == "0":
                    with allure.step("选择价格小于-小数位数0"):
                        print("选择价格小于-小数位数0")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_0)
                elif decimal_places == "1":
                    with allure.step("选择价格小于-小数位数1"):
                        print("选择价格小于-小数位数1")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_1)
                elif decimal_places == "2":
                    with allure.step("选择价格小于-小数位数2"):
                        print("选择价格小于-小数位数1")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_2)
                elif decimal_places == "3":
                    with allure.step("选择价格小于-小数位数3"):
                        print("选择价格小于-小数位数3")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_3)
                elif decimal_places == "4":
                    with allure.step("选择价格小于-小数位数4"):
                        print("选择价格小于-小数位数4")
                    self.click_element(Generate_quotation_lct.Price_less_than_decimal_places_4)
                with allure.step("确定生成报价"):
                    print("确定生成报价")
                self.click_element(Generate_quotation_lct.Confirm_to_generate_quotation)

