import time

import allure

from common.basepage import BasePage
from page_lct.company import Operating_instructions_lct


class OperatingInstructionsPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Operating_instructions_lct.Back_button)

    def Click_Play_button(self):
        time.sleep(5)
        # allure添加测试步骤
        with allure.step("点击播放"):
            print("点击播放")
        self.click_element(Operating_instructions_lct.Play_button)