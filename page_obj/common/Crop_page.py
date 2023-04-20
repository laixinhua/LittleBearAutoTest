import random

import allure

from common.basepage import BasePage
from page_lct.common import Select_Picture_lct


class CropPage(BasePage):

    def Click_Rotate_button(self):
        # allure添加测试步骤
        with allure.step("点击旋转"):
            print("点击旋转")
        self.click_element(Select_Picture_lct.rotate)
        with allure.step("点击裁剪"):
            print("点击裁剪")
        self.click_element(Select_Picture_lct.complete)

    def Click_Crop_button(self):
        # allure添加测试步骤
        with allure.step("点击裁剪"):
            print("点击裁剪")
        self.click_element(Select_Picture_lct.complete)
