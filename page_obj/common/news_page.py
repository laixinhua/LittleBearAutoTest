import random
import time

import allure

from common.Random_name import RandomName
from common.basepage import BasePage
from page_lct.common import news_lct, mail_list_lct, Album_permissions_lct, chat_lct
from page_obj.common.chat_page import ChatPage


class NewsPage(BasePage):
    def Click_Address_Book(self):
        # allure添加测试步骤
        with allure.step("点击通讯录"):
            print("点击通讯录")
        self.click_element(news_lct.mail_list)

    def Click_to_add_friends(self):
        # allure添加测试步骤
        with allure.step("点击添加好友"):
            print("点击添加好友")
        self.click_element(news_lct.Add_friends)

    def Message_page_to_add_friends(self,app_page):
        self.Click_to_add_friends()
        with allure.step("点击添加好友"):
            print("点击添加好友")
        self.click_element(mail_list_lct.Add_friends)
        with allure.step("点击添加好友"):
            print("点击添加好友")
        self.click_element(mail_list_lct.Add_friends)
        Continue_to_add_friends = random.choice(["是","否"])#是否继续添加好友
        if Continue_to_add_friends == "否":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(mail_list_lct.Add_friend_return)
        elif Continue_to_add_friends == "是":
            Search_by_phone_number_or_address_book = random.choice(["手机号搜索","手机联系人"])
            if Search_by_phone_number_or_address_book == "手机号搜索":
                with allure.step("请输入关键词"):
                    print("请输入关键词")
                self.click_element(mail_list_lct.Please_enter_keywords)
                with allure.step("输入手机号：13642562621"):
                    print("输入手机号：13642562621")
                self.input_text("13642562621",mail_list_lct.Please_enter_keywords)
                with allure.step("点击搜索按钮"):
                    print("点击搜索按钮")
                self.click_element(mail_list_lct.Search_button)
                Add_friend_or_cancel_operation = random.choice(["添加好友","取消操作","查看搜索结果"])
                if Add_friend_or_cancel_operation == "添加好友":
                    with allure.step("点击+添加"):
                        print("点击+添加")
                    self.click_element(mail_list_lct.add)
                    Modify_personal_name = random.choice(["是","否","返回操作"])
                    if Modify_personal_name == "是":
                        with allure.step("修改个人名称"):
                            print("修改个人名称")
                        name = self.find_element(mail_list_lct.send_content).text
                        # 123 光标移至末尾
                        self.driver.keyevent(123)
                        for i in range(0, len(name)):
                            # 67 退格键
                            self.driver.keyevent(67)
                        self.clear_text(mail_list_lct.send_content)
                        with allure.step("重新输入"):
                            print("重新输入")
                        self.input_text("我是大逼逗",mail_list_lct.send_content)
                        Repair_remarks = random.choice(["是","否"])
                        if Repair_remarks == "是":
                            with allure.step("输入备注"):
                                print("输入备注")
                            self.input_text("钢筋混泥土", mail_list_lct.Add_friend_Comment_name)
                            with allure.step("点击发送"):
                                print("点击发送")
                            self.click_element(mail_list_lct.send_out)
                        elif Repair_remarks == "否":
                            with allure.step("点击发送"):
                                print("点击发送")
                            self.click_element(mail_list_lct.send_out)
                    elif Modify_personal_name == "否":
                        Repair_remarks = random.choice(["是", "否"])
                        if Repair_remarks == "是":
                            with allure.step("输入备注"):
                                print("输入备注")
                            self.input_text("钢筋混泥土", mail_list_lct.Add_friend_Comment_name)
                            with allure.step("点击发送"):
                                print("点击发送")
                            self.click_element(mail_list_lct.send_out)
                        elif Repair_remarks == "否":
                            with allure.step("点击发送"):
                                print("点击发送")
                            self.click_element(mail_list_lct.send_out)
                    elif Modify_personal_name == "返回操作":
                        with allure.step("点击返回"):
                            print("点击返回")
                        self.click_element(mail_list_lct.Friend_verification_return)
                elif Add_friend_or_cancel_operation == "取消操作":
                    with allure.step("点击取消"):
                        print("点击取消")
                    self.click_element(mail_list_lct.cancel)
                elif Add_friend_or_cancel_operation == "查看搜索结果":
                    with allure.step("查看搜索结果"):
                        print("查看搜索结果")
                    self.click_element(mail_list_lct.Click_search_results)
                    Personal_information_page_operation = random.choice(["返回操作","举报","不允许对方看我的玩具圈","发消息","音视频通话","添加好友"])#"返回操作","举报","不允许对方看我的玩具圈","发消息","音视频通话","添加好友"
                    if Personal_information_page_operation == "返回操作":
                        with allure.step("点击返回"):
                            print("点击返回")
                        self.click_element(mail_list_lct.Personal_information_return)
                    elif Personal_information_page_operation == "举报":
                        with allure.step("点击举报"):
                            print("点击举报")
                        self.click_element(mail_list_lct.report)
                        Type_of_report = random.choice(["返回操作","欺诈","色情","不实信息","违法犯罪","骚扰","侵权"])
                        if Type_of_report == "返回操作":
                            with allure.step("点击返回"):
                                print("点击返回")
                            self.click_element(mail_list_lct.report_return)
                        elif Type_of_report == "欺诈":
                            with allure.step("点击欺诈"):
                                print("点击欺诈")
                            self.click_element(mail_list_lct.cheat)
                        elif Type_of_report == "色情":
                            with allure.step("点击色情"):
                                print("点击色情")
                            self.click_element(mail_list_lct.pornographic)
                        elif Type_of_report == "不实信息":
                            with allure.step("点击不实信息"):
                                print("点击不实信息")
                            self.click_element(mail_list_lct.False_information)
                        elif Type_of_report == "违法犯罪":
                            with allure.step("点击违法犯罪"):
                                print("点击违法犯罪")
                            self.click_element(mail_list_lct.Illegal_crime)
                        elif Type_of_report == "骚扰":
                            with allure.step("点击骚扰"):
                                print("点击骚扰")
                            self.click_element(mail_list_lct.harass)
                        elif Type_of_report == "侵权":
                            with allure.step("点击侵权"):
                                print("点击侵权")
                            self.click_element(mail_list_lct.tort)
                    elif Personal_information_page_operation == "不允许对方看我的玩具圈":
                        with allure.step("不允许对方看我的玩具圈"):
                            print("不允许对方看我的玩具圈")
                        self.click_element(mail_list_lct.Allow_the_other_party_to_see_my_toy_circle_Personal_information)
                    elif Personal_information_page_operation == "发消息":
                        with allure.step("点击发消息"):
                            print("点击发消息")
                        self.click_element(mail_list_lct.Send_a_message)
                        #ChatPage(app_page).send_content()
                        ChatPage(app_page).Send_emoticons()
                    elif Personal_information_page_operation == "音视频通话":
                        with allure.step("点击音视频通话"):
                            print("点击音视频通话")
                        self.click_element(mail_list_lct.Audio_and_video_call)
                        Audio_and_video_call = random.choice(["语音通话","视频通话"])
                        if Audio_and_video_call == "语音通话":
                            with allure.step("点击语音通话"):
                                print("点击语音通话")
                            self.click_element(mail_list_lct.voice_call)
                            with allure.step("要允许小竹熊录制音频吗？-允许"):
                                print("要允许小竹熊录制音频吗？-允许")
                            self.click_element(Album_permissions_lct.allow4)
                            time.sleep(2)
                        elif Audio_and_video_call == "视频通话":
                            with allure.step("点击视频通话"):
                                print("点击视频通话")
                            self.click_element(mail_list_lct.Video_call)
                            with allure.step("要允许小竹熊录制音频吗？-允许"):
                                print("要允许小竹熊录制音频吗？-允许")
                            self.click_element(Album_permissions_lct.allow2)
                            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
                            self.click_element(Album_permissions_lct.allow1)
                            time.sleep(2)
                    elif Personal_information_page_operation == "添加好友":
                        with allure.step("点击添加好友"):
                            print("点击添加好友")
                        self.click_element(mail_list_lct.Add_friends)
                        Modify_personal_name = random.choice(["是", "否", "返回操作"])
                        if Modify_personal_name == "是":
                            with allure.step("修改个人名称"):
                                print("修改个人名称")
                            name = self.find_element(mail_list_lct.send_content).text
                            # 123 光标移至末尾
                            self.driver.keyevent(123)
                            for i in range(0, len(name)):
                                # 67 退格键
                                self.driver.keyevent(67)
                            self.clear_text(mail_list_lct.send_content)
                            with allure.step("重新输入"):
                                print("重新输入")
                            self.input_text("我是大逼逗", mail_list_lct.send_content)
                            Repair_remarks = random.choice(["是", "否"])
                            if Repair_remarks == "是":
                                with allure.step("输入备注"):
                                    print("输入备注")
                                self.input_text("钢筋混泥土", mail_list_lct.Add_friend_Comment_name)
                                with allure.step("点击发送"):
                                    print("点击发送")
                                self.click_element(mail_list_lct.send_out)
                            elif Repair_remarks == "否":
                                with allure.step("点击发送"):
                                    print("点击发送")
                                self.click_element(mail_list_lct.send_out)
                        elif Modify_personal_name == "否":
                            Repair_remarks = random.choice(["是", "否"])
                            if Repair_remarks == "是":
                                with allure.step("输入备注"):
                                    print("输入备注")
                                self.input_text("钢筋混泥土", mail_list_lct.Add_friend_Comment_name)
                                with allure.step("点击发送"):
                                    print("点击发送")
                                self.click_element(mail_list_lct.send_out)
                            elif Repair_remarks == "否":
                                with allure.step("点击发送"):
                                    print("点击发送")
                                self.click_element(mail_list_lct.send_out)
                        elif Modify_personal_name == "返回操作":
                            with allure.step("点击返回"):
                                print("点击返回")
                            self.click_element(mail_list_lct.Friend_verification_return)
            elif Search_by_phone_number_or_address_book == "手机联系人":
                with allure.step("点击手机联系人"):
                    print("点击手机联系人")
                self.click_element(mail_list_lct.Mobile_contact)
                with allure.step("要允许小竹熊访问您的通讯录吗？-允许"):
                    print("要允许小竹熊访问您的通讯录吗？-允许")
                self.click_element(Album_permissions_lct.allow3)
                with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                    print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
                self.click_element(Album_permissions_lct.allow)
                time.sleep(2)
                Continue = random.choice(["是","否"])
                if Continue == "是":
                    with allure.step("请输入关键词"):
                        print("请输入关键词")
                    self.click_element(mail_list_lct.Please_enter_keywords)
                    with allure.step("输入手机号：13642562621"):
                        print("输入手机号：13642562621")
                    self.input_text("13642562621",mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索按钮"):
                        print("点击搜索按钮")
                    self.click_element(mail_list_lct.Mobile_phone_contacts_Search)
                elif Continue == "否":
                    with allure.step("点击返回"):
                        print("点击返回")
                    self.click_element(mail_list_lct.Mobile_phone_contacts_return)

    def Message_page_launches_group_chat(self):
        self.Click_to_add_friends()
        with allure.step("点击发起群聊"):
            print("点击发起群聊")
        self.click_element(mail_list_lct.Initiate_group_chat)
        time.sleep(2)
        Continue_to_initiate_group_chat = random.choice(["是", "否"])  # 继续群聊
        if Continue_to_initiate_group_chat == "否":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(mail_list_lct.Initiate_group_chat_return)
        elif Continue_to_initiate_group_chat == "是":
            Search_for_friends_or_check_it_directly = random.choice(["搜索好友", "直接勾选"])
            if Search_for_friends_or_check_it_directly == "直接勾选":
                with allure.step("勾选好友"):
                    print("勾选好友")
                Friend_list_friend = random.choice([1, 2, 3, 4])
                if Friend_list_friend == 1:
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                elif Friend_list_friend == 2:
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    self.click_element(mail_list_lct.Friend_list_friend2)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                    with allure.step("输入聊天消息"):
                        print("输入聊天消息")
                    self.input_text("你们好！", chat_lct.Content_input_box)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(chat_lct.send)
                elif Friend_list_friend == 3:
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    self.click_element(mail_list_lct.Friend_list_friend2)
                    self.click_element(mail_list_lct.Friend_list_friend3)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                    with allure.step("输入聊天消息"):
                        print("输入聊天消息")
                    self.input_text("你们好！", chat_lct.Content_input_box)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(chat_lct.send)
                elif Friend_list_friend == 4:
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    self.click_element(mail_list_lct.Friend_list_friend2)
                    self.click_element(mail_list_lct.Friend_list_friend3)
                    self.click_element(mail_list_lct.Friend_list_friend4)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                    with allure.step("输入聊天消息"):
                        print("输入聊天消息")
                    self.input_text("你们好！", chat_lct.Content_input_box)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(chat_lct.send)
            elif Search_for_friends_or_check_it_directly == "搜索好友":
                with allure.step("请输入关键词"):
                    print("请输入关键词")
                self.click_element(mail_list_lct.Please_enter_keywords)
                with allure.step("请输入关键词"):
                    print("请输入关键词")
                Friend_list_friend = random.choice([1, 2, 3, 4])
                if Friend_list_friend == 1:
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword = self.get_text(mail_list_lct.Friend_list_friend1_name)
                    self.input_text(keyword, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                elif Friend_list_friend == 2:
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword1 = self.get_text(mail_list_lct.Friend_list_friend1_name)
                    self.input_text(keyword1, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("清空好友名称"):
                        print("清空好友名称")
                    name = self.find_element(mail_list_lct.Search_bar_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Search_bar_content)
                    with allure.step("点击搜索加载所有好友"):
                        print("点击搜索加载所有好友")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword2 = self.get_text(mail_list_lct.Friend_list_friend2_name)
                    self.input_text(keyword2, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                    with allure.step("输入聊天消息"):
                        print("输入聊天消息")
                    self.input_text("你们好！", chat_lct.Content_input_box)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(chat_lct.send)
                elif Friend_list_friend == 3:
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword1 = self.get_text(mail_list_lct.Friend_list_friend1_name)
                    self.input_text(keyword1, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("清空好友名称"):
                        print("清空好友名称")
                    name = self.find_element(mail_list_lct.Search_bar_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Search_bar_content)
                    with allure.step("点击搜索加载所有好友"):
                        print("点击搜索加载所有好友")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword2 = self.get_text(mail_list_lct.Friend_list_friend2_name)
                    self.input_text(keyword2, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("清空好友名称"):
                        print("清空好友名称")
                    name = self.find_element(mail_list_lct.Search_bar_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Search_bar_content)
                    with allure.step("点击搜索加载所有好友"):
                        print("点击搜索加载所有好友")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword3 = self.get_text(mail_list_lct.Friend_list_friend3_name)
                    self.input_text(keyword3, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                    with allure.step("输入聊天消息"):
                        print("输入聊天消息")
                    self.input_text("你们好！", chat_lct.Content_input_box)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(chat_lct.send)
                elif Friend_list_friend == 4:
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword1 = self.get_text(mail_list_lct.Friend_list_friend1_name)
                    self.input_text(keyword1, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("清空好友名称"):
                        print("清空好友名称")
                    name = self.find_element(mail_list_lct.Search_bar_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Search_bar_content)
                    with allure.step("点击搜索加载所有好友"):
                        print("点击搜索加载所有好友")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword2 = self.get_text(mail_list_lct.Friend_list_friend2_name)
                    self.input_text(keyword2, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("清空好友名称"):
                        print("清空好友名称")
                    name = self.find_element(mail_list_lct.Search_bar_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Search_bar_content)
                    with allure.step("点击搜索加载所有好友"):
                        print("点击搜索加载所有好友")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword3 = self.get_text(mail_list_lct.Friend_list_friend3_name)
                    self.input_text(keyword3, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("清空好友名称"):
                        print("清空好友名称")
                    name = self.find_element(mail_list_lct.Search_bar_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Search_bar_content)
                    with allure.step("点击搜索加载所有好友"):
                        print("点击搜索加载所有好友")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("输入好友名称"):
                        print("输入好友名称")
                    keyword4 = self.get_text(mail_list_lct.Friend_list_friend4_name)
                    self.input_text(keyword4, mail_list_lct.Please_enter_keywords)
                    with allure.step("点击搜索"):
                        print("点击搜索")
                    self.click_element(mail_list_lct.Search_bar_content_search)
                    with allure.step("勾选好友"):
                        print("勾选好友")
                    self.click_element(mail_list_lct.Friend_list_friend1)
                    with allure.step("点击完成"):
                        print("点击完成")
                    self.click_element(mail_list_lct.complete)
                    with allure.step("输入聊天消息"):
                        print("输入聊天消息")
                    self.input_text("你们好！", chat_lct.Content_input_box)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(chat_lct.send)

    def Click_System_messages(self):
        # allure添加测试步骤
        with allure.step("点击系统消息"):
            print("点击系统消息")
        self.click_element(news_lct.System_messages)

    def System_message_page_return(self):
        self.Click_System_messages()
        with allure.step("点击返回按钮"):
            print("点击返回按钮")
        self.click_element(news_lct.System_message_return_button)

    def Click_All_on_the_system_message_page(self):
        self.Click_System_messages()
        with allure.step("点击全部"):
            print("点击全部")
        self.click_element(news_lct.whole)

    def System_message_page_click_unread(self):
        self.Click_System_messages()
        with allure.step("点击未读"):
            print("点击未读")
        self.click_element(news_lct.Unread)

    def Click_Read_on_the_system_message_page(self):
        self.Click_System_messages()
        with allure.step("点击已读"):
            print("点击已读")
        self.click_element(news_lct.Read)

    def One_click_on_the_system_message_page_to_read(self):
        self.Click_System_messages()
        with allure.step("点击一键已读"):
            print("点击一键已读")
        self.click_element(news_lct.One_button_read)
        Cancel_or_Confirm = RandomName().RandomCancelorConfirm()
        if Cancel_or_Confirm == "取消":
            with allure.step("点击取消"):
                print("点击取消")
            self.click_element(news_lct.Cancel)
        elif Cancel_or_Confirm == "确定":
            with allure.step("点击确定"):
                print("点击确定")
            self.click_element(news_lct.Confirm)

    def View_system_messages(self):
        self.Click_System_messages()
        with allure.step("查看系统消息"):
            print("查看系统消息")
        self.click_element(news_lct.System_message_1)

    def Delete_System_Message(self):
        self.Click_System_messages()
        with allure.step("点击..."):
            print("点击...")
        self.click_element(news_lct.More_system_messages)
        with allure.step("删除系统消息"):
            print("删除系统消息")
        self.click_element(news_lct.removal_message)

    def Click_RFQ_Message(self):
        # allure添加测试步骤
        with allure.step("点击询价消息"):
            print("点击询价消息")
        self.click_element(news_lct.RFQ_Message)

    def Click_Replenishment_message(self):
        # allure添加测试步骤
        with allure.step("点击补样消息"):
            print("点击补样消息")
        self.click_element(news_lct.Replenishment_message)

    def Click_Notification_Message(self):
        # allure添加测试步骤
        with allure.step("点击通知消息"):
            print("点击通知消息")
        self.click_element(news_lct.Notification_Message)

    def Click_Sample_borrowing_message(self):
        # allure添加测试步骤
        with allure.step("点击借样消息"):
            print("点击借样消息")
        self.click_element(news_lct.Sample_borrowing_message)

    def Click_Negotiation_news(self):
        # allure添加测试步骤
        with allure.step("点击洽谈消息"):
            print("点击洽谈消息")
        self.click_element(news_lct.Negotiation_news)

    def Click_Retrieval_message(self):
        # allure添加测试步骤
        with allure.step("点击取单消息"):
            print("点击取单消息")
        self.click_element(news_lct.Retrieval_message)

    def Click_Purchase_Message(self):
        # allure添加测试步骤
        with allure.step("点击采购消息"):
            print("点击采购消息")
        self.click_element(news_lct.Purchase_Message)

    def Click_Chat_Message(self):
        # allure添加测试步骤
        Whether_here_is_a_message = self.wait_eleVisible(news_lct.Chat_messages)
        if Whether_here_is_a_message == True:
            with allure.step("点击聊天消息"):
                print("点击聊天消息")
            self.click_element(news_lct.Chat_messages)
            if self.wait_eleVisible(chat_lct.Content_input_box) == True:
                with allure.step("输入内容"):
                    print("输入内容")
                self.input_text("Hello!",chat_lct.Content_input_box)
                with allure.step("点击发送"):
                    print("点击发送")
                self.click_element(chat_lct.send)
            else:
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(news_lct.Return_of_information_about_entering_the_exhibition_hall)
        else:
            self.driver.keyevent(4)






