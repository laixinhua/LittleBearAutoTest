import allure

from common.basepage import BasePage
from page_lct.ExhibitionHall import View_unpublished_products_in_the_exhibition_hall_lct


class ViewUnpublishedProductsInTheExhibitionHallPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(View_unpublished_products_in_the_exhibition_hall_lct.Back_button)

    def Click_All_employees_are_allowed_to_see(self):
        # allure添加测试步骤
        with allure.step("点击全部员工允许查看"):
            print("点击全部员工允许查看")
        self.click_element(View_unpublished_products_in_the_exhibition_hall_lct.All_employees_are_allowed_to_see)

    def Click_staff(self):
        # allure添加测试步骤
        with allure.step("点击员工"):
            print("点击员工")
        self.click_element(View_unpublished_products_in_the_exhibition_hall_lct.staff)

