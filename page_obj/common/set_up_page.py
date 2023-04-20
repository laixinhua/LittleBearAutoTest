import random

import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import set_up_lct


class SetUpPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(set_up_lct.Back_button)

    def Click_personal_information(self):
        # allure添加测试步骤
        with allure.step("点击个人信息"):
            print("点击个人信息")
        self.click_element(set_up_lct.personal_information)

    def Click_Clear_cache(self,app_page):
        # allure添加测试步骤
        with allure.step("点击清除缓存"):
            print("点击清除缓存")
        self.click_element(set_up_lct.Clear_cache)
        Number_of_checks = random.randint(1,3)
        if Number_of_checks == 1:
            with allure.step("勾选产品浏览记录"):
                print("勾选产品浏览记录")
            self.click_element(set_up_lct.Product_browsing_record)
        elif Number_of_checks == 2:
            with allure.step("勾选IM聊天记录"):
                print("勾选IM聊天记录")
            self.click_element(set_up_lct.IM_Chat)
        elif Number_of_checks == 3:
            with allure.step("全部勾选"):
                print("全部勾选")
            self.click_element(set_up_lct.Product_browsing_record)
            self.click_element(set_up_lct.IM_Chat)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == "取消":
            self.click_element(set_up_lct.Cancel0)
        elif Cancel_or_Confirm == "确定":
            self.click_element(set_up_lct.Confirm0)

    def Click_General_settings(self):
        # allure添加测试步骤
        with allure.step("点击通用设置"):
            print("点击通用设置")
        self.click_element(set_up_lct.General_settings)

    def Click_About_Xiao_zhu_xiong_yun_Technology(self):
        # allure添加测试步骤
        with allure.step("点击关于小竹熊云科技"):
            print("点击关于小竹熊云科技")
        self.click_element(set_up_lct.About_Xiao_zhu_xiong_yun_Technology)
        text = self.get_text(set_up_lct.About_Xiao_zhu_xiong_yun_Technology_Version_detection)
        if text == "当前为最新版本":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(set_up_lct.About_Xiao_zhu_xiong_yun_Technology_Back_button)
        elif text == "发现新版本":
            with allure.step("点击立即升级"):
                print("点击立即升级")
            self.click_element(set_up_lct.About_Xiao_zhu_xiong_yun_Technology_Version_detection)
            Update_or_not = random.choice(["立即升级","关闭弹框"])
            if Update_or_not == "立即升级":
                with allure.step("点击立即升级"):
                    print("点击立即升级")
                self.click_element(set_up_lct.upgrade_now)
            elif Update_or_not == "关闭弹框":
                with allure.step("点击关闭弹框"):
                    print("点击关闭弹框")
                self.click_element(set_up_lct.Cancel_Update)


    def Click_Update_History(self):
        # allure添加测试步骤
        with allure.step("点击更新历史"):
            print("点击更新历史")
        self.click_element(set_up_lct.Update_History)
        text = self.get_text(set_up_lct.About_Xiao_zhu_xiong_yun_Technology_Version_detection)
        if text == "当前为最新版本":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(set_up_lct.Back_button)
        elif text == "发现新版本":
            Update_or_not = random.choice(["是","否"])
            if Update_or_not == "是":
                with allure.step("点击发现新版本"):
                    print("点击发现新版本")
                self.click_element(set_up_lct.Update_History_Version_detection)
            elif Update_or_not == "否":
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(set_up_lct.Update_History_Back_button)

    def Click_contact_us(self):
        # allure添加测试步骤
        with allure.step("点击联系我们"):
            print("点击联系我们")
        self.click_element(set_up_lct.contact_us)

    def Click_Switch_roles(self):
        # allure添加测试步骤
        with allure.step("点击切换角色"):
            print("点击切换角色")
        self.click_element(set_up_lct.Switch_roles)

    def Click_Logout(self,app_page):
        # allure添加测试步骤
        with allure.step("点击退出登录"):
            print("点击退出登录")
        self.click_element(set_up_lct.Logout)
        Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
        if Cancel_or_Confirm == "取消":
            self.click_element(set_up_lct.Cancel1)
        elif Cancel_or_Confirm == "确定":
            self.click_element(set_up_lct.Confirm1)

    def Click_User_service_agreement(self):
        # allure添加测试步骤
        with allure.step("点击用户服务协议"):
            print("点击用户服务协议")
        self.click_element(set_up_lct.User_service_agreement)

    def Click_Privacy_policy(self):
        # allure添加测试步骤
        with allure.step("点击隐私政策"):
            print("点击隐私政策")
        self.click_element(set_up_lct.Privacy_policy)





