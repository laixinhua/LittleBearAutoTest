import time

from common.basepage import BasePage

from page_lct.common import login_lct, Visitor_login_lct, register_lct
import allure
from common.GetVerificationCode import TestGetVerificationCode



class LoginPage(BasePage):
    def click_agree(self):
        #allure添加测试步骤
        with allure.step("点击同意"):
            print("点击同意")
        self.click_element(login_lct.Agree)

    def click_disagree(self):
        # allure添加测试步骤
        with allure.step("点击不同意"):
            print("点击不同意")
        self.click_element(login_lct.Disagree)

    def View_Agreement(self):
        # allure添加测试步骤
        with allure.step("点击不同意"):
            print("点击不同意")
        self.click_element(login_lct.Disagree)
        with allure.step("点击查看协议"):
            print("点击查看协议")
        self.click_element(login_lct.View_agreement)
        time.sleep(2)
        with allure.step("上拉查看协议"):
            print("上拉查看协议")
        self.swipe(0.5,0.5,0.5,0.3,1000)
        time.sleep(2)

    def View_again(self):
        # allure添加测试步骤
        with allure.step("点击不同意"):
            print("点击不同意")
        self.click_element(login_lct.Disagree)
        with allure.step("点击仍不同意"):
            print("点击查看协议")
        self.click_element(login_lct.Still_disagree)
        with allure.step("点击再次查看"):
            print("点击再次查看")
        self.click_element(login_lct.View_again)
        time.sleep(2)
        with allure.step("上拉查看协议"):
            print("上拉查看协议")
        self.swipe(0.5,0.5,0.5,0.3,1000)
        time.sleep(2)



    def quit(self):
        # allure添加测试步骤
        with allure.step("点击不同意"):
            print("点击不同意")
        self.click_element(login_lct.Disagree)
        with allure.step("点击仍不同意"):
            print("点击仍不同意")
        self.click_element(login_lct.Still_disagree)
        with allure.step("点击退出应用"):
            print("点击退出应用")
        self.click_element(login_lct.Exit_application)


    def login(self,phone_number,verification_code,app_page):
        # allure添加测试步骤
        with allure.step("点击同意"):
            print("点击同意")
        self.click_element(login_lct.Agree)
        with allure.step("输入账号：{0}".format(phone_number)):
            print("输入账号：{0}".format(phone_number))
        self.input_text(phone_number, login_lct.Please_enter_your_mobile_number)
        with allure.step("输入验证码：{0}".format(verification_code)):
            print("输入验证码：{0}".format(verification_code))
        self.input_text(verification_code, login_lct.Please_enter_the_verification_code)
        with allure.step("勾选我同意并阅读《用户服务协议》与《隐私政策》"):
            print("勾选我同意并阅读《用户服务协议》与《隐私政策》")
        self.click_element(login_lct.Tick_button)
        with allure.step("点击登录"):
            print("点击登录")
        self.click_element(login_lct.login)
        return app_page.page_source

    def login_with_verification_code(self,phone_number,app_page):
        # allure添加测试步骤
        with allure.step("点击同意"):
            print("点击同意")
        self.click_element(login_lct.Agree)
        with allure.step("输入账号：{0}".format(phone_number)):
            print("输入账号：{0}".format(phone_number))
        self.input_text(phone_number, login_lct.Please_enter_your_mobile_number)
        with allure.step("点击获取验证码"):
            print("点击获取验证码")
        self.click_element(login_lct.Get_verification_code)
        time.sleep(5)
        name = self.find_element(login_lct.Default_verification_code).text
        self.click_element(login_lct.Default_verification_code)
        # 123 光标移至末尾
        self.driver.keyevent(123)
        for i in range(0, len(name)):
            # 67 退格键
            self.driver.keyevent(67)
        self.clear_text(login_lct.Default_verification_code)
        self.input_text(TestGetVerificationCode().test_LoginAdministrator(),login_lct.Please_enter_the_verification_code)
        with allure.step("勾选我同意并阅读《用户服务协议》与《隐私政策》"):
            print("勾选我同意并阅读《用户服务协议》与《隐私政策》")
        self.click_element(login_lct.Tick_button)
        with allure.step("点击登录"):
            print("点击登录")
        self.click_element(login_lct.login)
        return app_page.page_source


    def Visitor_login(self,app_page):
        # allure添加测试步骤
        with allure.step("勾选我同意并阅读《用户服务协议》与《隐私政策》"):
            print("勾选我同意并阅读《用户服务协议》与《隐私政策》")
        self.click_element(login_lct.Tick_button)
        with allure.step("点击游客登录"):
            print("点击游客登录")
        self.click_element(login_lct.Visitor_login)

    def Company_visitor_login(self):
        # allure添加测试步骤
        with allure.step("点击贸易公司"):
            print("点击贸易公司")
        self.click_element(Visitor_login_lct.company)

    def Vendor_visitor_login(self):
        # allure添加测试步骤
        with allure.step("点击供应商"):
            print("点击供应商")
        self.click_element(Visitor_login_lct.manufacturer)


    def Wechat_login(self):
        # allure添加测试步骤
        with allure.step("勾选我同意并阅读《用户服务协议》与《隐私政策》"):
            print("勾选我同意并阅读《用户服务协议》与《隐私政策》")
        self.click_element(login_lct.Tick_button)
        with allure.step("点击微信登录"):
            print("点击微信登录")
        self.click_element(login_lct.Wechat_login)
        time.sleep(5)







