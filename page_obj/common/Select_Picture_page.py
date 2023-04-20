import allure

from common.basepage import BasePage
from page_lct.common import Select_Picture_lct


class SelectPicturePage(BasePage):
    def Select_single_graph(self):
        # allure添加测试步骤
        with allure.step("选择单图"):
            print("选择单图")
        self.click_element(Select_Picture_lct.Select_Figure_two)
        with allure.step("点击完成"):
            print("点击完成")
        self.click_element(Select_Picture_lct.complete)

    def Select_Figure_two(self):
        # allure添加测试步骤
        with allure.step("选择图二"):
            print("选择图二")
        self.click_element(Select_Picture_lct.Select_Figure_two)
        with allure.step("点击完成"):
            print("点击完成")
        self.click_element(Select_Picture_lct.complete)
