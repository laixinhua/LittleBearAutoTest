import random
import time

import allure

from common.Random_name import RandomName
from common.basepage import BasePage
from page_lct.common import Toy_circle_lct, Album_permissions_lct, Select_Picture_lct


class ToyCirclePage(BasePage):
    def Release_toy_circle(self):
        # allure添加测试步骤
        with allure.step("点击发布"):
            print("点击发布")
        self.click_element(Toy_circle_lct.Release_toy_circle)
        Notice = RandomName().RandomNotice()
        if Notice == "普通公告":
            if self.wait_eleVisible(Toy_circle_lct.General_announcement) == True:
                with allure.step("点击普通公告"):
                    print("点击普通公告")
                self.click_element(Toy_circle_lct.General_announcement)
            else:
                print("数据加载中")
        elif Notice == "采购公告":
            if self.wait_eleVisible(Toy_circle_lct.Procurement_announcement) == True:
                with allure.step("点击采购公告"):
                    print("点击采购公告")
                self.click_element(Toy_circle_lct.Procurement_announcement)
            elif self.wait_eleVisible(Toy_circle_lct.Supply_announcement) ==True:
                with allure.step("点击供应公告"):
                    print("点击供应公告")
                self.click_element(Toy_circle_lct.Supply_announcement)
        elif Notice == "供应公告":
            if self.wait_eleVisible(Toy_circle_lct.Supply_announcement) == True:
                with allure.step("点击供应公告"):
                    print("点击供应公告")
                self.click_element(Toy_circle_lct.Supply_announcement)
            elif self.wait_eleVisible(Toy_circle_lct.Procurement_announcement) == True:
                with allure.step("点击采购公告"):
                    print("点击采购公告")
                self.click_element(Toy_circle_lct.Procurement_announcement)
        with allure.step("输入内容"):
            print("输入内容")
        Content = RandomName().RandomToyCircleContent()
        self.input_text(Content,Toy_circle_lct.Release_content)
        Whether_to_release_toy_circles_with_pictures = random.choice(["是","否"])
        if Whether_to_release_toy_circles_with_pictures == "否":
            Whether_to_show_it_to_others = random.choice(["是", "否"])
            if Whether_to_show_it_to_others == "是":
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)
            elif Whether_to_show_it_to_others == "否":
                with allure.step("点击不给谁看"):
                    print("点击不给谁看")
                self.click_element(Toy_circle_lct.Who_can_watch_it)
                The_selected_friend_is_not_visible = random.choice(["所有供应商", "所有供应商和所有展厅", "所有供应商和所有公司", "所有供应商和所有展厅和所有公司", "所有展厅", "所有展厅和所有公司", "所有公司"])
                if The_selected_friend_is_not_visible == "所有供应商":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有供应商和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有展厅":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有展厅和所有公司":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有公司":
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(Toy_circle_lct.determine)
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)
        elif Whether_to_release_toy_circles_with_pictures == "是":
            with allure.step("点击添加图片"):
                print("点击添加图片")
            self.click_element(Toy_circle_lct.Publish_pictures)
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊拍制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)
            with allure.step("选择图片"):
                print("选择图片")
            self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_two)
            with allure.step("点击使用"):
                print("点击使用")
            self.click_element(Select_Picture_lct.use)
            Whether_to_show_it_to_others = random.choice(["是","否"])
            if Whether_to_show_it_to_others == "是":
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)
            elif Whether_to_show_it_to_others == "否":
                with allure.step("点击不给谁看"):
                    print("点击不给谁看")
                self.click_element(Toy_circle_lct.Who_can_watch_it)
                The_selected_friend_is_not_visible = random.choice(["所有供应商","所有供应商和所有展厅","所有供应商和所有公司","所有供应商和所有展厅和所有公司","所有展厅","所有展厅和所有公司","所有公司"])
                if The_selected_friend_is_not_visible == "所有供应商":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有供应商和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有展厅":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有展厅和所有公司":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有公司":
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(Toy_circle_lct.determine)
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)

    def Release_toy_circle_picture(self):
        # allure添加测试步骤
        with allure.step("点击发布"):
            print("点击发布")
        self.click_element(Toy_circle_lct.Release_toy_circle)
        Notice = RandomName().RandomNotice()
        if Notice == "普通公告":
            if self.wait_eleVisible(Toy_circle_lct.General_announcement) == True:
                with allure.step("点击普通公告"):
                    print("点击普通公告")
                self.click_element(Toy_circle_lct.General_announcement)
            else:
                print("数据加载中")
        elif Notice == "采购公告":
            if self.wait_eleVisible(Toy_circle_lct.Procurement_announcement) == True:
                with allure.step("点击采购公告"):
                    print("点击采购公告")
                self.click_element(Toy_circle_lct.Procurement_announcement)
            elif self.wait_eleVisible(Toy_circle_lct.Supply_announcement) ==True:
                with allure.step("点击供应公告"):
                    print("点击供应公告")
                self.click_element(Toy_circle_lct.Supply_announcement)
        elif Notice == "供应公告":
            if self.wait_eleVisible(Toy_circle_lct.Supply_announcement) == True:
                with allure.step("点击供应公告"):
                    print("点击供应公告")
                self.click_element(Toy_circle_lct.Supply_announcement)
            elif self.wait_eleVisible(Toy_circle_lct.Procurement_announcement) == True:
                with allure.step("点击采购公告"):
                    print("点击采购公告")
                self.click_element(Toy_circle_lct.Procurement_announcement)
        with allure.step("输入内容"):
            print("输入内容")
        Content = RandomName().RandomToyCircleContent()
        self.input_text(Content,Toy_circle_lct.Release_content)
        Whether_to_release_toy_circles_with_pictures = random.choice(["是","否"])
        if Whether_to_release_toy_circles_with_pictures == "否":
            Whether_to_show_it_to_others = random.choice(["是", "否"])
            if Whether_to_show_it_to_others == "是":
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)
            elif Whether_to_show_it_to_others == "否":
                with allure.step("点击不给谁看"):
                    print("点击不给谁看")
                self.click_element(Toy_circle_lct.Who_can_watch_it)
                The_selected_friend_is_not_visible = random.choice(
                        ["所有供应商", "所有供应商和所有展厅", "所有供应商和所有公司", "所有供应商和所有展厅和所有公司", "所有展厅", "所有展厅和所有公司", "所有公司"])
                if The_selected_friend_is_not_visible == "所有供应商":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有供应商和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有展厅":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有展厅和所有公司":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有公司":
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(Toy_circle_lct.determine)
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)
        elif Whether_to_release_toy_circles_with_pictures == "是":
            with allure.step("点击添加图片"):
                print("点击添加图片")
            self.click_element(Toy_circle_lct.Publish_pictures)
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊拍制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow)
            Number_of_pictures = random.randint(1,9)
            if Number_of_pictures == 1:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_two)
            elif Number_of_pictures == 2:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
            elif Number_of_pictures == 3:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
            elif Number_of_pictures == 4:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_six)
            elif Number_of_pictures == 5:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_six)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_seven)
            elif Number_of_pictures == 6:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_six)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_seven)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_eight)
            elif Number_of_pictures == 7:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_six)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_seven)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_eight)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_nine)
            elif Number_of_pictures == 8:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_six)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_seven)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_eight)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_nine)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_ten)
            elif Number_of_pictures == 9:
                with allure.step("选择图片"):
                    print("选择图片")
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_three)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_four)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_five)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_six)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_seven)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_eight)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_nine)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_ten)
                self.click_element(Select_Picture_lct.Toy_circle_Select_Figure_eleven)
            with allure.step("点击使用"):
                print("点击使用")
            self.click_element(Select_Picture_lct.use)
            Whether_to_show_it_to_others = random.choice(["是", "否"])
            if Whether_to_show_it_to_others == "是":
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)
            elif Whether_to_show_it_to_others == "否":
                with allure.step("点击不给谁看"):
                    print("点击不给谁看")
                self.click_element(Toy_circle_lct.Who_can_watch_it)
                The_selected_friend_is_not_visible = random.choice(
                        ["所有供应商", "所有供应商和所有展厅", "所有供应商和所有公司", "所有供应商和所有展厅和所有公司", "所有展厅", "所有展厅和所有公司", "所有公司"])
                if The_selected_friend_is_not_visible == "所有供应商":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有供应商和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有供应商和所有展厅和所有公司":
                    with allure.step("勾选所有供应商"):
                        print("勾选所有供应商")
                    self.click_element(Toy_circle_lct.All_suppliers)
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有展厅":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                elif The_selected_friend_is_not_visible == "所有展厅和所有公司":
                    with allure.step("勾选所有展厅"):
                        print("勾选所有展厅")
                    self.click_element(Toy_circle_lct.All_exhibition_halls)
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                elif The_selected_friend_is_not_visible == "所有公司":
                    with allure.step("勾选所有公司"):
                        print("勾选所有公司")
                    self.click_element(Toy_circle_lct.All_companies)
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(Toy_circle_lct.determine)
                with allure.step("点击发布"):
                    print("点击发布")
                self.click_element(Toy_circle_lct.release)
                time.sleep(10)

    def View_toy_circle_or_information(self):
        View_toy_circle_or_information = random.choice(["玩具圈","资讯"])
        if View_toy_circle_or_information == "玩具圈":
            # allure添加测试步骤
            with allure.step("点击玩具圈"):
                print("点击玩具圈")
            self.click_element(Toy_circle_lct.Toy_circle)
            Type_of_toy_circle = random.choice(["全部","普通","采购","供应","分享"])
            if Type_of_toy_circle == "全部":
                with allure.step("点击全部"):
                    print("点击全部")
                self.click_element(Toy_circle_lct.Toy_circle_all)
            elif Type_of_toy_circle == "普通":
                with allure.step("点击普通"):
                    print("点击普通")
                self.click_element(Toy_circle_lct.Toy_circle_ordinary)
            elif Type_of_toy_circle == "采购":
                with allure.step("点击采购"):
                    print("点击采购")
                self.click_element(Toy_circle_lct.Toy_circle_purchase)
            elif Type_of_toy_circle == "供应":
                with allure.step("点击供应"):
                    print("点击供应")
                self.click_element(Toy_circle_lct.Toy_circle_supply)
            elif Type_of_toy_circle == "分享":
                with allure.step("点击分享"):
                    print("点击分享")
                self.click_element(Toy_circle_lct.Toy_circle_share)
        elif View_toy_circle_or_information == "资讯":
            with allure.step("点击资讯"):
                print("点击资讯")
            self.click_element(Toy_circle_lct.real_time_info)
            Information_type = random.choice(["全部","玩具资讯","行业资讯","平台资讯"])
            if Information_type == "全部":
                with allure.step("点击全部"):
                    print("点击全部")
                self.click_element(Toy_circle_lct.Information_all)
                with allure.step("点击资讯广告"):
                    print("点击资讯广告")
                self.click_element(Toy_circle_lct.real_time_info_ad)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
                with allure.step("点击第一个资讯图片"):
                    print("点击第一个资讯图片")
                self.click_element(Toy_circle_lct.Infographic)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
            elif Information_type == "玩具资讯":
                with allure.step("点击玩具资讯"):
                    print("点击玩具资讯")
                self.click_element(Toy_circle_lct.Toy_information)
                with allure.step("点击资讯广告"):
                    print("点击资讯广告")
                self.click_element(Toy_circle_lct.real_time_info_ad)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
                with allure.step("点击第一个资讯图片"):
                    print("点击第一个资讯图片")
                self.click_element(Toy_circle_lct.Infographic)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
            elif Information_type == "行业资讯":
                with allure.step("点击行业资讯"):
                    print("点击行业资讯")
                self.click_element(Toy_circle_lct.Industry_information)
                with allure.step("点击资讯广告"):
                    print("点击资讯广告")
                self.click_element(Toy_circle_lct.real_time_info_ad)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
                with allure.step("点击第一个资讯图片"):
                    print("点击第一个资讯图片")
                self.click_element(Toy_circle_lct.Infographic)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
            elif Information_type == "平台资讯":
                with allure.step("点击平台资讯"):
                    print("点击平台资讯")
                self.click_element(Toy_circle_lct.Platform_information)
                with allure.step("点击资讯广告"):
                    print("点击资讯广告")
                self.click_element(Toy_circle_lct.real_time_info_ad)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)
                with allure.step("点击第一个资讯图片"):
                    print("点击第一个资讯图片")
                self.click_element(Toy_circle_lct.Infographic)
                time.sleep(2)
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(Toy_circle_lct.back_button)




