import allure
import re
from common.basepage import BasePage
from page_lct.common import Business_consultation_push_and_SMS_settings_lct


class GeneralSettingsCompanySettingsPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Business_consultation_push_and_SMS_settings_lct.Back_button)

    def Search_employees(self):
        # allure添加测试步骤
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        text = self.get_text(Business_consultation_push_and_SMS_settings_lct.Employee_information)
        pattern = re.compile(r"\d")#python使用正则表达式需导入re包，r表示原生字符串
        number = re.findall(pattern,text)
        self.click_element(Business_consultation_push_and_SMS_settings_lct.Search_button0)
        with allure.step("输入内容"):
            print("输入内容")
        self.input_text(number, Business_consultation_push_and_SMS_settings_lct.Search_bar)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(Business_consultation_push_and_SMS_settings_lct.Search_button1)

    def Click_All_employees_receive_push_information(self):
        # allure添加测试步骤
        with allure.step("点击全部员工接收推送信息"):
            print("点击全部员工接收推送信息")
        self.click_element(Business_consultation_push_and_SMS_settings_lct.All_employees_receive_push_information)

    def Click_All_employees_receive_SMS(self):
        # allure添加测试步骤
        with allure.step("点击全部员工接收短信"):
            print("点击全部员工接收推送信息")
        self.click_element(Business_consultation_push_and_SMS_settings_lct.All_employees_receive_SMS)


    def Click_Employee_receive_business_consultation(self):
        text = self.get_text(Business_consultation_push_and_SMS_settings_lct.Employee_receive_business_consultation)
        if text == "关闭":
            # allure添加测试步骤
            with allure.step("点击接收业务咨询"):
                print("点击接收业务咨询")
            self.click_element(Business_consultation_push_and_SMS_settings_lct.Employee_receive_business_consultation)
        elif text == "开启":
            # allure添加测试步骤
            with allure.step("点击接收业务咨询"):
                print("点击接收业务咨询")
            self.click_element(Business_consultation_push_and_SMS_settings_lct.Employee_receive_business_consultation1)

    def Click_Employee_receive_push_information(self):
        # allure添加测试步骤
        with allure.step("点击接收推送信息"):
            print("点击接收推送信息")
        self.click_element(Business_consultation_push_and_SMS_settings_lct.Employee_receive_push_information)

    def Click_Employee_receive_SMS(self):
        # allure添加测试步骤
        with allure.step("点击接收短信"):
            print("点击接收短信")
        self.click_element(Business_consultation_push_and_SMS_settings_lct.All_employees_receive_SMS)

