import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Select_role_lct


class RolePage(BasePage):
    def Select_the_role_of_the_exhibition_hall(self):
        # allure添加测试步骤
        with allure.step("选择展厅角色"):
            print("选择展厅角色")
        self.click_element(Select_role_lct.Exhibition_hall_role)
        with allure.step("点击登录按钮"):
            print("点击登录按钮")
        self.click_element(Select_role_lct.Login_button)
        time.sleep(10)

    def Select_company_role(self):
        # allure添加测试步骤
        with allure.step("选择公司角色"):
            print("选择公司角色")
        self.click_element(Select_role_lct.Company_role)
        with allure.step("点击登录按钮"):
            print("点击登录按钮")
        self.click_element(Select_role_lct.Login_button)
        time.sleep(10)

    def Select_vendor_role(self):
        # allure添加测试步骤
        with allure.step("选择厂商角色"):
            print("选择厂商角色")
        self.click_element(Select_role_lct.Vendor_role)
        with allure.step("点击登录按钮"):
            print("点击登录按钮")
        self.click_element(Select_role_lct.Login_button)
        time.sleep(10)

    def Random_Select_role(self,app_page):
        Role = Random_name.RandomName.RandomRole(app_page)
        if Role == "展厅":
            with allure.step("选择展厅角色"):
                print("选择展厅角色")
            self.click_element(Select_role_lct.Exhibition_hall_role)
            with allure.step("点击登录按钮"):
                print("点击登录按钮")
            self.click_element(Select_role_lct.Login_button)
            time.sleep(10)
        elif Role == "公司":
            with allure.step("选择公司角色"):
                print("选择公司角色")
            self.click_element(Select_role_lct.Company_role)
            with allure.step("点击登录按钮"):
                print("点击登录按钮")
            self.click_element(Select_role_lct.Login_button)
            time.sleep(10)
        elif Role == "厂商":
            with allure.step("选择厂商角色"):
                print("选择厂商角色")
            self.click_element(Select_role_lct.Vendor_role)
            with allure.step("点击登录按钮"):
                print("点击登录按钮")
            self.click_element(Select_role_lct.Login_button)
            time.sleep(10)
        return Role

