import allure

from common.basepage import BasePage
from page_lct.common import Album_permissions_lct


class AlbumPermissionsPage(BasePage):
    def click_allow(self):
        #相册权限-允许
        # allure添加测试步骤
        with allure.step("点击允许"):
            print("点击允许")
        self.click_element(Album_permissions_lct.allow)

    def click_refuse(self):
        #相册权限-拒绝
        # allure添加测试步骤
        with allure.step("点击拒绝"):
            print("点击拒绝")
        self.click_element(Album_permissions_lct.refuse)

    def click_allow1(self):
        #拍照权限-允许
        # allure添加测试步骤
        with allure.step("点击允许"):
            print("点击允许")
        self.click_element(Album_permissions_lct.allow1)

    def click_refuse1(self):
        #拍照权限-拒绝
        # allure添加测试步骤
        with allure.step("点击拒绝"):
            print("点击拒绝")
        self.click_element(Album_permissions_lct.refuse1)

    def click_allow2(self):
        # 文件权限-允许
        # allure添加测试步骤
        with allure.step("点击允许"):
            print("点击允许")
        self.click_element(Album_permissions_lct.allow2)

    def click_refuse2(self):
        # 文件权限-拒绝
        # allure添加测试步骤
        with allure.step("点击拒绝"):
            print("点击拒绝")
        self.click_element(Album_permissions_lct.refuse2)

    def click_allow3(self):
        # 录音权限-允许
        # allure添加测试步骤
        with allure.step("点击允许"):
            print("点击允许")
        self.click_element(Album_permissions_lct.allow3)

    def click_refuse3(self):
        # 录音权限-拒绝
        # allure添加测试步骤
        with allure.step("点击拒绝"):
            print("点击拒绝")
        self.click_element(Album_permissions_lct.refuse3)