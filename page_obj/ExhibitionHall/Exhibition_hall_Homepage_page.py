import random
import time

import allure
from common.basepage import BasePage
from page_lct.ExhibitionHall import Exhibition_hall_Homepage_lct


class ExhibitionHallHomepagePage(BasePage):
    def Click_Avatar(self):
        # allure添加测试步骤
        with allure.step("点击头像"):
            print("点击头像")
        self.click_element(Exhibition_hall_Homepage_lct.head_portrait)

    def Click_message(self):
        # allure添加测试步骤
        with allure.step("点击消息"):
            print("点击消息")
        self.click_element(Exhibition_hall_Homepage_lct.news)

    def Click_toy_circle(self):
        # allure添加测试步骤
        with allure.step("点击玩具圈"):
            print("点击玩具圈")
        self.click_element(Exhibition_hall_Homepage_lct.Toy_circle)

    def Click_workbench(self):
        # allure添加测试步骤
        with allure.step("点击工作台"):
            print("点击工作台")
        self.click_element(Exhibition_hall_Homepage_lct.workbench)

    def Click_New_product_area(self):
        # allure添加测试步骤
        with allure.step("点击新品区"):
            print("点击新品区")
        self.click_element(Exhibition_hall_Homepage_lct.New_product_area)
        product_name = self.get_text(Exhibition_hall_Homepage_lct.product_name)
        print(product_name)
        return product_name

    def Click_3D_product(self):
        # allure添加测试步骤
        with allure.step("点击3D产品"):
            print("点击3D产品")
        self.click_element(Exhibition_hall_Homepage_lct.threeD_product)

    def Click_Video_area(self):
        # allure添加测试步骤
        with allure.step("点击视频区"):
            print("点击视频区")
        self.click_element(Exhibition_hall_Homepage_lct.Video_area)

    def Click_Hot_sales_sample_selection(self):
        # allure添加测试步骤
        with allure.step("点击热销择样"):
            print("点击热销择样")
        self.click_element(Exhibition_hall_Homepage_lct.Hot_sales_sample_selection)

    def Click_Total_products(self):
        # allure添加测试步骤
        with allure.step("点击产品总数"):
            print("点击产品总数")
        self.click_element(Exhibition_hall_Homepage_lct.Total_products)

    def Click_Total_number_of_manufacturers(self):
        # allure添加测试步骤
        with allure.step("点击厂商总数"):
            print("点击厂商总数")
        self.click_element(Exhibition_hall_Homepage_lct.Total_number_of_manufacturers)

    def Click_Hot_Products_in_the_Exhibition_Hall_More(self):
        # allure添加测试步骤
        with allure.step("点击展厅热销产品-更多"):
            print("点击展厅热销产品-更多")
        self.click_element(Exhibition_hall_Homepage_lct.Hot_Products_in_the_Exhibition_Hall_More)

    def Randomly_click_the_hot_selling_products_in_the_exhibition_hall(self):
        # allure添加测试步骤
        with allure.step("随机点击展厅热销产品"):
            print("随机点击展厅热销产品")
        random_product = random.choice(["展厅热销产品1","展厅热销产品2","展厅热销产品3","展厅热销产品4"])
        if random_product == "展厅热销产品1":
            with allure.step("点击展厅热销产品1"):
                print("点击展厅热销产品1")
            self.click_element(Exhibition_hall_Homepage_lct.Hot_Products_in_the_Exhibition_Hall_1)
        elif random_product == "展厅热销产品2":
            with allure.step("点击展厅热销产品2"):
                print("点击展厅热销产品2")
            self.click_element(Exhibition_hall_Homepage_lct.Hot_Products_in_the_Exhibition_Hall_2)
        elif random_product == "展厅热销产品3":
            with allure.step("点击展厅热销产品3"):
                print("点击展厅热销产品3")
            self.click_element(Exhibition_hall_Homepage_lct.Hot_Products_in_the_Exhibition_Hall_3)
        elif random_product == "展厅热销产品4":
            with allure.step("点击展厅热销产品4"):
                print("点击展厅热销产品4")
            self.click_element(Exhibition_hall_Homepage_lct.Hot_Products_in_the_Exhibition_Hall_4)
        time.sleep(5)
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5, 0.7, 0.5, 0.2, 1000)

    def Click_Latest_sample_company_more(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.3,1000)
        with allure.step("点击最新择样公司-更多"):
            print("点击最新择样公司-更多")
        self.click_element(Exhibition_hall_Homepage_lct.Latest_sample_company_more)

    def Latest_sample_company_Search(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.3,1000)
        with allure.step("点击最新择样公司-更多"):
            print("点击最新择样公司-更多")
        self.click_element(Exhibition_hall_Homepage_lct.Latest_sample_company_more)
        with allure.step("在请输入关键词中输入-薄荣"):
            print("在请输入关键词中输入-薄荣")
        self.input_text('薄荣',Exhibition_hall_Homepage_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_hall_Homepage_lct.Search_button)


    def Randomly_click_the_latest_sample_company(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5, 0.8, 0.5, 0.3, 1000)
        with allure.step("随机点击最新择样公司"):
            print("随机点击最新择样公司")
        random_company = random.choice(["最新择样公司1","最新择样公司2","最新择样公司3","最新择样公司4"])
        if random_company == "最新择样公司1":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_sample_company_1)
            print("点击最新择样公司1")
        elif random_company == "最新择样公司2":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_sample_company_2)
            print("点击最新择样公司2")
        elif random_company == "最新择样公司3":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_sample_company_3)
            print("点击最新择样公司3")
        elif random_company == "最新择样公司4":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_sample_company_4)
            print("点击最新择样公司4")

    def Click_Latest_settled_manufacturers_more(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.3,1000)
        with allure.step("点击最新入驻厂商-更多"):
            print("点击最新入驻厂商-更多")
        self.click_element(Exhibition_hall_Homepage_lct.Latest_settled_manufacturers_more)

    def Latest_settled_manufacturers_Search(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5,0.8,0.5,0.3,1000)
        with allure.step("点击最新入驻厂商-更多"):
            print("点击最新入驻厂商-更多")
        self.click_element(Exhibition_hall_Homepage_lct.Latest_settled_manufacturers_more)
        with allure.step("在请输入关键词中输入-宝茜玩具厂"):
            print("在请输入关键词中输入-宝茜玩具厂")
        self.input_text('宝茜玩具厂',Exhibition_hall_Homepage_lct.Please_enter_keywords)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_hall_Homepage_lct.Search_button)


    def Randomly_click_the_latest_settled_manufacturer(self):
        # allure添加测试步骤
        with allure.step("上拉屏幕"):
            print("上拉屏幕")
        self.swipe(0.5, 0.8, 0.5, 0.3, 1000)
        with allure.step("随机点击最新入驻厂商"):
            print("随机点击最新入驻厂商")
        random_manufacturer = random.choice(["最新入驻厂商1", "最新入驻厂商2", "最新入驻厂商3", "最新入驻厂商4"])
        if random_manufacturer == "最新入驻厂商1":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_settled_manufacturers1)
            print("点击最新入驻厂商1")
        elif random_manufacturer == "最新入驻厂商2":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_settled_manufacturers2)
            print("点击最新入驻厂商2")
        elif random_manufacturer == "最新入驻厂商3":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_settled_manufacturers3)
            print("点击最新入驻厂商3")
        elif random_manufacturer == "最新入驻厂商4":
            self.click_element(Exhibition_hall_Homepage_lct.Latest_settled_manufacturers4)
            print("点击最新入驻厂商4")