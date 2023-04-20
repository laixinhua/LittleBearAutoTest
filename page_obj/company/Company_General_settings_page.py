import allure

from common.basepage import BasePage
from page_lct.company import Company_General_settings_lct


class CompanyGeneralSettingsPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Company_General_settings_lct.Back_button)

    def Click_Business_consultation_push_and_SMS_settings(self):
        # allure添加测试步骤
        with allure.step("点击业务咨询、推送、短信设置"):
            print("点击业务咨询、推送、短信设置")
        self.click_element(Company_General_settings_lct.Business_consultation_push_and_SMS_settings)

    def Click_Product_privacy_settings(self):
        # allure添加测试步骤
        with allure.step("点击产品隐私设置"):
            print("点击产品隐私设置")
        self.click_element(Company_General_settings_lct.Product_privacy_settings)