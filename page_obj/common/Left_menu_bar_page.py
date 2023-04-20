import allure

from common.basepage import BasePage
from page_lct.common import Left_menu_bar_lct


class LeftMenuBarPage(BasePage):
    def Click_head_portrait(self):
        # allure添加测试步骤
        with allure.step("点击头像"):
            print("点击头像")
        self.click_element(Left_menu_bar_lct.head_portrait)

    def Click_Switch_roles(self):
        # allure添加测试步骤
        with allure.step("点击切换角色"):
            print("点击角色")
        self.click_element(Left_menu_bar_lct.Switch_roles)

    def Click_Toy_Circle_Collection(self):
        # allure添加测试步骤
        with allure.step("点击玩具圈收藏"):
            print("点击玩具圈收藏")
        self.click_element(Left_menu_bar_lct.Toy_Circle_Collection)

    def Click_set_up(self):
        # allure添加测试步骤
        with allure.step("点击设置"):
            print("点击设置")
        self.click_element(Left_menu_bar_lct.set_up)