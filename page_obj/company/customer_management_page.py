import random

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.company import customer_management_lct


class CustomerManagementPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(customer_management_lct.Back_button)

    def Add_customer(self,app_page):
        # allure添加测试步骤
        with allure.step("点击新增客户"):
            print("点击新增客户")
        self.click_element(customer_management_lct.New_customers)
        with allure.step("输入客户名称"):
            print("输入客户名称")
        customer_name = Random_name.RandomName.RandomNames(app_page)
        self.input_text(customer_name,customer_management_lct.name)
        with allure.step("输入电话"):
            print("输入电话")
        phone_number = Random_name.RandomName.RandomPhoneNumber(app_page)
        self.input_text(phone_number,customer_management_lct.Telephone)
        with allure.step("输入邮箱"):
            print("输入邮箱")
        Email = Random_name.RandomName.RandomEmail(app_page)
        self.input_text(Email,customer_management_lct.mailbox)
        with allure.step("输入备注"):
            print("输入备注")
        remarks = Random_name.RandomName.RandomRemarks(app_page)
        self.input_text(remarks,customer_management_lct.remarks)
        with allure.step("点击新增"):
            print("点击新增")
        self.click_element(customer_management_lct.Add_button)

    def edit_customer(self,app_page):
        if self.wait_eleVisible(customer_management_lct.Enter_edit) == True:
            with allure.step("进入编辑"):
                print("进入编辑")
            self.click_element(customer_management_lct.Enter_edit)
            with allure.step("点击编辑"):
                print("点击编辑")
            self.click_element(customer_management_lct.Add_button)
            with allure.step("清空名字"):
                print("清空名字")
            self.clear_text(customer_management_lct.name)
            with allure.step("输入名字"):
                print("输入名字")
            customer_name = Random_name.RandomName.RandomNames(app_page)
            self.input_text(customer_name,customer_management_lct.name)
            with allure.step("清空电话"):
                print("清空电话")
            self.clear_text(customer_management_lct.Telephone)
            with allure.step("输入电话"):
                print("输入电话")
            phone_number = Random_name.RandomName.RandomPhoneNumber(app_page)
            self.input_text(phone_number, customer_management_lct.Telephone)
            with allure.step("清空邮箱"):
                print("清空邮箱")
            self.clear_text(customer_management_lct.mailbox)
            with allure.step("输入邮箱"):
                print("输入邮箱")
            Email = Random_name.RandomName.RandomEmail(app_page)
            self.input_text(Email, customer_management_lct.mailbox)
            with allure.step("清空备注"):
                print("清空备注")
            self.clear_text(customer_management_lct.remarks)
            with allure.step("输入备注"):
                print("输入备注")
            remarks = random.choice(list(["华东大客户", "华南大客户", "华西大客户", "华北大客户"]))
            self.input_text(remarks, customer_management_lct.remarks)
            with allure.step("点击保存"):
                print("点击保存")
            self.click_element(customer_management_lct.Add_button)
        else:
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(customer_management_lct.Back_button)


    def delete_customer(self,app_page):
        if self.wait_eleVisible(customer_management_lct.delete) == True:
            with allure.step("点击删除"):
                print("点击删除")
            self.click_element(customer_management_lct.delete)
            Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
            if Cancel_or_Confirm == "确定":
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(customer_management_lct.determine)
            elif Cancel_or_Confirm == "取消":
                with allure.step("点击取消"):
                    print("点击取消")
                self.click_element(customer_management_lct.cancel)

    def Search_customer_name(self,app_page):
        with allure.step("搜索栏输入客户名称"):
            print("搜索栏输入客户名称")
        customer_name = Random_name.RandomName.RandomNames(app_page)
        self.input_text(customer_name,customer_management_lct.Please_enter_a_keyword)
        with allure.step("点击搜索"):
            print("点击搜索")
        self.click_element(customer_management_lct.Search_button)

