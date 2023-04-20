import random
import time
import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Album_permissions_lct, register_lct, Select_Picture_lct, Crop_lct
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class RegisterPage(BasePage):
    def click_black(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(register_lct.Back_button)
        time.sleep(5)

    def click_skip(self):
        # allure添加测试步骤
        with allure.step("点击跳过"):
            print("点击跳过")
        self.click_element(register_lct.skip)
        time.sleep(5)

    def click_login(self):
        # allure添加测试步骤
        with allure.step("点击登录"):
            print("点击登录")
        self.click_element(register_lct.login)
        time.sleep(5)

    def Upload_company_logo(self):
        # allure添加测试步骤
        with allure.step("点击上传公司logo"):
            print("点击上传公司logo")
        self.click_element(register_lct.Upload_company_logo)
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
            with allure.step("点击使用"):
                print("点击使用")
            self.click_element(Select_Picture_lct.complete)
            time.sleep(1)
        else:
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击使用"):
                print("点击使用")
            self.click_element(Select_Picture_lct.complete)
            time.sleep(1)


    def Fill_in_the_company_name(self,compyany_name):
        # allure添加测试步骤
        with allure.step("填写公司名称"):
            print("填写公司名称")
        self.input_text(compyany_name, register_lct.corporate_name)
        time.sleep(1)

    def Fill_in_contact(self,customer_name):
        # allure添加测试步骤
        with allure.step("填写联系人"):
            print("填写联系人")
        self.input_text(customer_name, register_lct.contacts)
        time.sleep(1)

    def Fill_in_the_mobile_phone_number(self,phone_number):
        # allure添加测试步骤
        with allure.step("填写手机号码"):
            print("填写手机号码")
        self.input_text(phone_number, register_lct.phone_number)
        time.sleep(1)

    def Fill_in_Telephone_landline(self,Telephone_landline):
        # allure添加测试步骤
        with allure.step("填写电话座机"):
            print("填写电话座机")
        self.input_text(Telephone_landline, register_lct.Telephone_landline)
        time.sleep(1)

    def Fill_in_QQNumber(self,QQnumber):
        # allure添加测试步骤
        with allure.step("填写QQ号码"):
            print("填写QQ号码")
        self.input_text(QQnumber, register_lct.QQ_number)
        time.sleep(1)

    def Fill_in_Address(self,address):
        # allure添加测试步骤
        with allure.step("填写联系地址"):
            print("填写联系地址")
        self.input_text(address,register_lct.Contact_address)
        time.sleep(1)

    def visitor_swipe(self):
        with allure.step("上滑屏幕"):
            print("上滑屏幕")
        self.swipe(0.5,0.5,0.5,0.2,1000)

    def Upload_business_license(self):
        # allure添加测试步骤
        with allure.step("点击上传营业执照"):
            print("点击上传营业执照")
        self.click_element(register_lct.Business_license)
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
            with allure.step("点击使用"):
                print("点击使用")
            self.click_element(Select_Picture_lct.complete)
            time.sleep(1)
        else:
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击使用"):
                print("点击使用")
            self.click_element(Select_Picture_lct.complete)
            time.sleep(1)

    def Visitor_registration(self):
        # allure添加测试步骤
        with allure.step("点击提交申请"):
            print("点击提交申请")
        self.click_element(register_lct.Submit_application)
        time.sleep(1)











