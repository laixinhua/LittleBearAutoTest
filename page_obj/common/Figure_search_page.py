import time

import allure

from common.basepage import BasePage
from page_lct.common import Album_permissions_lct, Figure_search_lct


class FigureSearchPage(BasePage):
    def Click_Back_button(self):
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow1)
        if self.wait_eleVisible(Album_permissions_lct.allow2) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow2)
        if self.wait_eleVisible(Album_permissions_lct.allow) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow)
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Figure_search_lct.Back_button)

    def Click_album0(self):
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow1)
        if self.wait_eleVisible(Album_permissions_lct.allow2) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow2)
        if self.wait_eleVisible(Album_permissions_lct.allow) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow)
        # allure添加测试步骤
        with allure.step("点击相册"):
            print("点击相册")
        self.click_element(Figure_search_lct.album0)

    def Click_Figure_search(self):
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow1)
        if self.wait_eleVisible(Album_permissions_lct.allow2) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow2)
        if self.wait_eleVisible(Album_permissions_lct.allow) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow)
        # allure添加测试步骤
        with allure.step("点击图搜"):
            print("点击图搜")
        self.click_element(Figure_search_lct.Figure_search)
        if self.wait_eleVisible(Album_permissions_lct.allow3) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow3)
        with allure.step("点击拍照"):
            print("点击拍照")
        self.click_element(Figure_search_lct.photograph)

    def Click_camera_search(self):
        if self.wait_eleVisible(Album_permissions_lct.allow1) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow1)
        if self.wait_eleVisible(Album_permissions_lct.allow2) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow2)
        time.sleep(2)
        if self.wait_eleVisible(Album_permissions_lct.allow3) == True:
            with allure.step("点击允许"):
                print("点击允许")
            self.click_element(Album_permissions_lct.allow3)
        with allure.step("点击拍照"):
            print("点击拍照")
        self.click_element(Figure_search_lct.photograph)








