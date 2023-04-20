import random
import time

import allure

from common.basepage import BasePage
from page_lct.common import mail_list_lct, Album_permissions_lct, chat_lct
from page_obj.common.chat_page import ChatPage


class MailListPage(BasePage):
    def Add_friends(self,app_page):
        # allure添加测试步骤
        with allure.step("点击添加好友+"):
            print("点击添加好友+")
        self.click_element(mail_list_lct.Add_friends_add)
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

    def Initiate_group_chat(self):
        # allure添加测试步骤
        with allure.step("点击添加好友+"):
            print("点击添加好友+")
        self.click_element(mail_list_lct.Add_friends_add)
        with allure.step("点击发起群聊"):
            print("点击发起群聊")
        self.click_element(mail_list_lct.Initiate_group_chat)
        time.sleep(2)
        Continue_to_initiate_group_chat = random.choice(["是","否"])#继续群聊
        if Continue_to_initiate_group_chat == "否":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(mail_list_lct.Initiate_group_chat_return)
        elif Continue_to_initiate_group_chat == "是":
            Search_for_friends_or_check_it_directly = random.choice(["搜索好友","直接勾选"])
            if Search_for_friends_or_check_it_directly == "直接勾选":
                with allure.step("勾选好友"):
                    print("勾选好友")
                Friend_list_friend = random.choice([1,2,3,4])
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
                    self.input_text(keyword,mail_list_lct.Please_enter_keywords)
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

    def Friend_request_operation(self,app_page):
        with allure.step("点击新的好友"):
            print("点击新的好友")
        self.click_element(mail_list_lct.New_friends)
        Continue_or_return = random.choice(["返回操作","继续操作"])
        if Continue_or_return == "返回操作":
            with allure.step("点击返回按钮"):
                print("点击返回按钮")
            self.click_element(mail_list_lct.New_friends_return)
        elif Continue_or_return == "继续操作":
            with allure.step("点击好友请求一"):
                print("点击好友请求一")
            self.click_element(mail_list_lct.First_friend)
            title = self.get_text(mail_list_lct.title)
            if title == "个人信息":
                Return_to_operation_or_continue_operation = random.choice(["返回操作","继续操作"])
                if Return_to_operation_or_continue_operation == "返回操作":
                    with allure.step("点击返回"):
                        print("点击返回")
                    self.click_element(mail_list_lct.Personal_information_return)
                elif Return_to_operation_or_continue_operation == "继续操作":
                    Whether_to_report = random.choice(["是","否"])
                    if Whether_to_report == "是":
                        with allure.step("点击举报"):
                            print("点击举报")
                        self.click_element(mail_list_lct.report)
                        Type_of_report = random.choice(["返回操作", "欺诈", "色情", "不实信息", "违法犯罪", "骚扰", "侵权"])
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
                    elif Whether_to_report == "否":
                        Allow_the_other_party_to_view_my_toy_circle = random.choice(["是", "否"])
                        if Allow_the_other_party_to_view_my_toy_circle == "否":
                            with allure.step("不允许对方查看我的玩具圈"):
                                print("不允许对方查看我的玩具圈")
                            self.click_element(mail_list_lct.Allow_the_other_party_to_see_my_toy_circle_Personal_information)
                        elif Allow_the_other_party_to_view_my_toy_circle == "是":
                            Other_operations = random.choice(["发消息","音视频通话","添加好友"])
                            if Other_operations == "发消息":
                                with allure.step("点击发消息"):
                                    print("点击发消息")
                                self.click_element(mail_list_lct.Send_a_message)
                                Operation_content = random.choice(["发送内容","发送表情","发送照片","语音聊天","视频聊天","发送快捷语","添加快捷语","编辑快捷语"])
                                if Operation_content == "发送内容":
                                    ChatPage(app_page).send_content()
                                elif Operation_content == "发送表情":
                                    ChatPage(app_page).Send_emoticons()
                                elif Operation_content == "发送照片":
                                    ChatPage(app_page).Send_photos()
                                elif Operation_content == "语音聊天":
                                    ChatPage(app_page).voice_call()
                                elif Operation_content == "视频聊天":
                                    ChatPage(app_page).Video_call()
                                elif Operation_content == "发送快捷语":
                                    ChatPage(app_page).Shortcut_sending()
                                elif Operation_content == "添加快捷语":
                                    ChatPage(app_page).Add_shortcut()
                                elif Operation_content == "编辑快捷语":
                                    ChatPage(app_page).Edit_shortcut()
                            elif Other_operations == "音视频通话":
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
                            elif Other_operations == "添加好友":
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
            elif title == "好友申请":
                Return_or_continue_processing = random.choice(["返回操作","继续处理"])
                if Return_or_continue_processing == "返回操作":
                    with allure.step("点击返回按钮"):
                        print("点击返回按钮")
                    self.click_element(mail_list_lct.Friend_application_return)
                elif Return_or_continue_processing == "继续处理":
                    Whether_to_fill_in_remarks_and_labels = random.choice(["是","否"])
                    if Whether_to_fill_in_remarks_and_labels == "是":
                        with allure.step("点击备注和标签"):
                            print("点击备注和标签")
                        self.click_element(mail_list_lct.Remarks_and_labels)
                        Return_to_operation_or_fill_in_remarks = random.choice(["填写备注","返回操作"])
                        if Return_to_operation_or_fill_in_remarks == "返回操作":
                            with allure.step("点击返回"):
                                print("点击返回")
                            self.click_element(mail_list_lct.Remarks_return)
                        elif Return_to_operation_or_fill_in_remarks == "填写备注":
                            with allure.step("请填写备注或标签"):
                                print("请填写备注或标签")
                            self.input_text("第一排的大聪明",mail_list_lct.Please_fill_in_remarks_or_labels)
                            with allure.step("点击保存"):
                                print("点击保存")
                            self.click_element(mail_list_lct.preservation)
                    elif Whether_to_fill_in_remarks_and_labels == "否":
                        Allow_the_other_party_to_view_my_toy_circle = random.choice(["是","否"])
                        if Allow_the_other_party_to_view_my_toy_circle == "否":
                            with allure.step("不允许对方查看我的玩具圈"):
                                print("不允许对方查看我的玩具圈")
                            self.click_element(mail_list_lct.Allow_the_other_party_to_see_my_toy_circle_Friend_application)
                        elif Allow_the_other_party_to_view_my_toy_circle == "是":
                            Accept_or_reject = random.choice(["接受","拒绝"])
                            if Accept_or_reject == "接受":
                                with allure.step("点击接受"):
                                    print("点击接受")
                                self.click_element(mail_list_lct.accept)
                            elif Accept_or_reject == "拒绝":
                                with allure.step("点击拒绝"):
                                    print("点击拒绝")
                                self.click_element(mail_list_lct.refuse)

    def View_company_homepage(self):
        with allure.step("查看公司主页"):
            print("查看公司主页")
        self.click_element(mail_list_lct.Company_Logo)

    def Ungrouped_member_query(self):
        with allure.step("点击未分组成员"):
            print("查看公司主页")
        self.click_element(mail_list_lct.Ungrouped_members)
        Continue_searching_or_return_to_operation = random.choice(["返回操作","继续查询"])
        if Continue_searching_or_return_to_operation == "返回操作":
            with allure.step("点击返回按钮"):
                print("点击返回按钮")
            self.click_element(mail_list_lct.Ungrouped_members_Back_button)
        elif Continue_searching_or_return_to_operation == "继续查询":
            Query_Employee = random.choice(["1","2"])
            if Query_Employee == "1":
                Employee_name = self.get_text(mail_list_lct.Ungrouped_members_one)
                with allure.step("输入关键词{}".format(Employee_name)):
                    print("输入关键词{}".format(Employee_name))
                self.input_text(Employee_name,mail_list_lct.Please_enter_keywords)
                with allure.step("点击搜索"):
                    print("点击搜索")
                self.click_element(mail_list_lct.Ungrouped_members_query)

    def Friend_Action(self,app_page):
        with allure.step("点击好友"):
            print("点击好友")
        self.click_element(mail_list_lct.My_friend_first_friend)
        operation = random.choice(["返回操作","修改备注","举报","发消息","音视频通话","删除好友"])#"返回操作","修改备注","举报","发消息","音视频通话","删除好友"
        if operation == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(mail_list_lct.Personal_information_return)
        elif operation == "修改备注":
            with allure.step("点击备注"):
                print("点击备注")
            self.click_element(mail_list_lct.remarks)
            Set_remark_operation = random.choice(["返回操作","设置备注名","设置备注","设置备注名和备注"])
            if Set_remark_operation == "返回操作":
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(mail_list_lct.Set_comment_return)
            elif Set_remark_operation == "设置备注名":
                Remark_Name = self.get_text(mail_list_lct.Remark_Name)
                if len(Remark_Name) > 0:
                    Remark_Name = self.find_element(mail_list_lct.Remark_Name).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(Remark_Name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Remark_Name)
                    with allure.step("输入备注名"):
                        print("输入备注名")
                    self.input_text("有网友回复",mail_list_lct.Remark_Name)
                else:
                    with allure.step("输入备注名"):
                        print("输入备注名")
                    self.input_text("第一排的大聪明",mail_list_lct.Remark_Name)
                with allure.step("点击保存"):
                    print("点击保存")
                self.click_element(mail_list_lct.preservation)
            elif Set_remark_operation == "设置备注":
                Remark = self.get_text(mail_list_lct.Remark)
                if len(Remark) > 0:
                    Remark = self.find_element(mail_list_lct.Remark).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(Remark)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Remark)
                    with allure.step("输入备注"):
                        print("输入备注")
                    self.input_text("极个别", mail_list_lct.Remark)
                else:
                    with allure.step("输入备注"):
                        print("输入备注")
                    self.input_text("少部分", mail_list_lct.Remark)
                with allure.step("点击保存"):
                    print("点击保存")
                self.click_element(mail_list_lct.preservation)
            elif Set_remark_operation == "设置备注名和备注":
                Remark_Name = self.get_text(mail_list_lct.Remark_Name)
                if len(Remark_Name) > 0:
                    Remark_Name = self.find_element(mail_list_lct.Remark_Name).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(Remark_Name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(mail_list_lct.Remark_Name)
                    with allure.step("输入备注名"):
                        print("输入备注名")
                    self.input_text("有网友回复", mail_list_lct.Remark_Name)
                else:
                    with allure.step("输入备注名"):
                        print("输入备注名")
                    self.input_text("第一排的大聪明", mail_list_lct.Remark_Name)
                Remark = self.get_text(mail_list_lct.Remark)
                if len(Remark) > 0:
                    self.clear_text(mail_list_lct.Remark)
                    with allure.step("输入备注"):
                        print("输入备注")
                    self.input_text("极个别", mail_list_lct.Remark)
                else:
                    with allure.step("输入备注"):
                        print("输入备注")
                    self.input_text("少部分", mail_list_lct.Remark)
                with allure.step("点击保存"):
                    print("点击保存")
                self.click_element(mail_list_lct.preservation)
        elif operation == "举报":
            with allure.step("点击举报"):
                print("点击举报")
            self.click_element(mail_list_lct.report)
            Type_of_report = random.choice(["返回操作", "欺诈", "色情", "不实信息", "违法犯罪", "骚扰", "侵权"])
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
        elif operation == "发消息":
            with allure.step("点击发消息"):
                print("点击发消息")
            self.click_element(mail_list_lct.Send_a_message)
            Operation_content = random.choice(["发送内容", "发送表情", "发送照片", "语音聊天", "视频聊天", "发送快捷语", "添加快捷语", "编辑快捷语"])
            if Operation_content == "发送内容":
                ChatPage(app_page).send_content()
            elif Operation_content == "发送表情":
                ChatPage(app_page).Send_emoticons()
            elif Operation_content == "发送照片":
                ChatPage(app_page).Send_photos()
            elif Operation_content == "语音聊天":
                ChatPage(app_page).voice_call()
            elif Operation_content == "视频聊天":
                ChatPage(app_page).Video_call()
            elif Operation_content == "发送快捷语":
                ChatPage(app_page).Shortcut_sending()
            elif Operation_content == "添加快捷语":
                ChatPage(app_page).Add_shortcut()
            elif Operation_content == "编辑快捷语":
                ChatPage(app_page).Edit_shortcut()
        elif operation == "音视频通话":
            with allure.step("点击音视频通话"):
                print("点击音视频通话")
            self.click_element(mail_list_lct.Audio_and_video_call)
            Audio_and_video_call = random.choice(["语音通话", "视频通话"])
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
        elif operation == "删除好友":
            with allure.step("点击删除好友"):
                print("点击删除好友")
            self.click_element(mail_list_lct.Delete_friend)
            Delete_friend_or_not = random.choice(["确定","取消"])
            if Delete_friend_or_not == "确定":
                with allure.step("点击确定"):
                    print("点击确定")
                self.click_element(mail_list_lct.determine)
            elif Delete_friend_or_not == "取消":
                with allure.step("点击取消"):
                    print("点击取消")
                self.click_element(mail_list_lct.cancel)











