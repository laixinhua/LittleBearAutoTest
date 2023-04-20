import allure

from common.basepage import BasePage
from page_lct.common import Visitor_login_lct


class VisitorLoginPage(BasePage):
    def click_black(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Visitor_login_lct.black)

    def Company_visitor_login(self):
        # allure添加测试步骤
        with allure.step("点击公司"):
            print("点击公司")
        self.click_element(Visitor_login_lct.company)

    def Vendor_visitor_login(self):
        # allure添加测试步骤
        with allure.step("点击厂商"):
            print("点击厂商")
        self.click_element(Visitor_login_lct.manufacturer)

