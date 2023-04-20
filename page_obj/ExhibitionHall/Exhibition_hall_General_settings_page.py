import allure

from common.basepage import BasePage
from page_lct.ExhibitionHall import Exhibition_Hall_General_settings_lct


class ExhibitionHallGeneralSettingsPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Exhibition_Hall_General_settings_lct.Back_button)

    def Click_Display_showroom_sample_selection_record(self):
        # allure添加测试步骤
        with allure.step("点击显示展厅择样记录"):
            print("点击显示展厅择样记录")
        self.click_element(Exhibition_Hall_General_settings_lct.Display_showroom_sample_selection_record)

    def Click_Show_visit_records(self):
        # allure添加测试步骤
        with allure.step("点击显示来访记录"):
            print("点击显示来访记录")
        self.click_element(Exhibition_Hall_General_settings_lct.Show_visit_records)

    def Click_Business_consultation_push_and_SMS_settings(self):
        # allure添加测试步骤
        with allure.step("点击业务咨询、推送、短信设置"):
            print("点击业务咨询、推送、短信设置")
        self.click_element(Exhibition_Hall_General_settings_lct.Business_consultation_push_and_SMS_settings)

    def Click_View_unpublished_products_in_the_exhibition_hall(self):
        # allure添加测试步骤
        with allure.step("点击查看展厅未公开产品"):
            print("点击查看展厅未公开产品")
        self.click_element(Exhibition_Hall_General_settings_lct.View_unpublished_products_in_the_exhibition_hall)

    def Click_Product_privacy_settings(self):
        # allure添加测试步骤
        with allure.step("点击产品隐私设置"):
            print("点击产品隐私设置")
        self.click_element(Exhibition_Hall_General_settings_lct.Product_privacy_settings)
