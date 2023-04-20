import allure

from common import Random_name
from common.basepage import BasePage
from page_lct.common import Toy_Circle_Collection_lct


class ToyCircleCollectionPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Toy_Circle_Collection_lct.Back_button)

    def Click_Delete_button(self,app_page):
        if self.wait_eleVisible(Toy_Circle_Collection_lct.Delete_button) == True:
            # allure添加测试步骤
            with allure.step("点击删除"):
                print("点击删除")
            self.click_element(Toy_Circle_Collection_lct.Delete_button)
            Cancel_or_Confirm = Random_name.RandomName.RandomCancelorConfirm(app_page)
            if Cancel_or_Confirm == "取消":
                self.click_element(Toy_Circle_Collection_lct.cancel)
            elif Cancel_or_Confirm == "确定":
                self.click_element(Toy_Circle_Collection_lct.determine)
        else:
            self.click_element(Toy_Circle_Collection_lct.Back_button)





