import time

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Album_permissions_lct, personal_information_lct, Select_Picture_lct
from page_obj.common.clear_text import ClearTextPage


class PersonalInformationPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(personal_information_lct.Back_button)
        time.sleep(1)

    def Modify_Avatar(self):
        # allure添加测试步骤
        with allure.step("修改头像"):
            print("修改头像")
        self.click_element(personal_information_lct.head_portrait)
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow1)
        if self.wait_eleVisible(Album_permissions_lct.allow) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择单图"):
                print("选择单图")
            self.click_element(Select_Picture_lct.Select_Figure_two)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
            time.sleep(10)
        else:
            with allure.step("选择单图"):
                print("选择单图")
            self.click_element(Select_Picture_lct.Select_single_graph)
            with allure.step("点击完成"):
                print("点击完成")
            self.click_element(Select_Picture_lct.complete)
            time.sleep(1)

    def Modify_Name(self,app_page,new_name):
        # allure添加测试步骤
        with allure.step("点击姓名"):
            print("点击姓名")
        self.click_element(personal_information_lct.full_name)
        with allure.step("修改名称"):
            print("修改名称")
        # name = self.find_element(personal_information_lct.Modify_name).text
        # # 123 光标移至末尾
        # self.driver.keyevent(123)
        # for i in range(0, len(name)):
        #     # 67 退格键
        #     self.driver.keyevent(67)
        #self.clear_text(personal_information_lct.Modify_name)
        ClearTextPage(app_page).clear_text(personal_information_lct.Modify_name)
        self.input_text(new_name, personal_information_lct.Modify_name)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == '取消':
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(personal_information_lct.cancel)
        elif Cancel_or_Confirm == '确定':
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(personal_information_lct.determine)

    def Modify_Gender(self, app_page):
        # allure添加测试步骤
        with allure.step("点击性别"):
            print("点击性别")
        self.click_element(personal_information_lct.Gender)
        Male_or_Female = Random_name.RandomName.RandomGender(app_page)
        if Male_or_Female == '男':
            with allure.step("选择男"):
                print("选择男")
            self.click_element(personal_information_lct.male)
        elif Male_or_Female == '女':
            with allure.step("选择女"):
                print("选择女")
            self.click_element(personal_information_lct.female)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == '取消':
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(personal_information_lct.cancel)
        elif Cancel_or_Confirm == '确定':
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(personal_information_lct.determine)

    def Modify_Birthday(self,app_page):
        # allure添加测试步骤
        with allure.step("点击生日"):
            print("点击生日")
        self.click_element(personal_information_lct.birthday)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == '取消':
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(personal_information_lct.cancel)
        elif Cancel_or_Confirm == '确定':
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(personal_information_lct.determine)


