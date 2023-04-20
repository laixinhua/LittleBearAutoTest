import allure

from common.basepage import BasePage
from page_lct.manufacturer import Manufacturer_Homepage_lct


class ManufacturerHomepagePage(BasePage):
    def Click_Avatar(self):
        # allure添加测试步骤
        with allure.step("点击头像"):
            print("点击头像")
        self.click_element(Manufacturer_Homepage_lct.head_portrait)

    def Click_message(self):
        # allure添加测试步骤
        with allure.step("点击消息"):
            print("点击消息")
        self.click_element(Manufacturer_Homepage_lct.news)

    def Click_toy_circle(self):
        # allure添加测试步骤
        with allure.step("点击玩具圈"):
            print("点击玩具圈")
        self.click_element(Manufacturer_Homepage_lct.Toy_circle)

    def Click_workbench(self):
        # allure添加测试步骤
        with allure.step("点击工作台"):
            print("点击工作台")
        self.click_element(Manufacturer_Homepage_lct.workbench)