import random

import allure

from common.basepage import BasePage
from page_lct.common import chat_lct, Album_permissions_lct, Select_Picture_lct


class ChatPage(BasePage):
    def send_content(self):
        # allure添加测试步骤
        Return_to_action_or_continue_chatting = random.choice(["返回操作","继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("输入内容"):
                print("输入内容")
            self.input_text("第一排的大聪明",chat_lct.Content_input_box)
            with allure.step("点击发送"):
                print("点击发送")
            self.click_element(chat_lct.send)

    def Send_emoticons(self):
        Return_to_action_or_continue_chatting = random.choice(["返回操作", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击表情"):
                print("点击表情")
            self.click_element(chat_lct.Emoticon_button)
            Random_expression = random.choice([1,2,3])
            if Random_expression == 1:
                with allure.step("点击第一个表情"):
                    print("点击第一个表情")
                self.click_element(chat_lct.First_expression)
                with allure.step("点击发送"):
                    print("点击发送")
                self.click_element(chat_lct.send)
            elif Random_expression == 2:
                with allure.step("点击第二个表情"):
                    print("点击第二个表情")
                self.click_element(chat_lct.Second_expression)
                with allure.step("点击发送"):
                    print("点击发送")
                self.click_element(chat_lct.send)
            elif Random_expression == 3:
                with allure.step("点击第三个表情"):
                    print("点击第三个表情")
                self.click_element(chat_lct.The_third_expression)
                with allure.step("点击发送"):
                    print("点击发送")
                self.click_element(chat_lct.send)

    def Send_photos(self):
        Return_to_action_or_continue_chatting = random.choice(["返回操作", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击更多"):
                print("点击更多")
            self.click_element(chat_lct.add_Button)
            with allure.step("点击照片"):
                print("点击照片")
            self.click_element(chat_lct.picture)
            with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
                print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
            self.click_element(Album_permissions_lct.allow6)
            with allure.step("选择图片一"):
                print("选择图片一")
            self.click_element(Select_Picture_lct.chat_select_picture_one)
            Related_Operations = random.choice(["发送","取消","预览"])
            if Related_Operations == "发送":
                with allure.step("点击发送"):
                    print("点击发送")
                self.click_element(Select_Picture_lct.chat_select_picture_send)
            elif Related_Operations == "取消":
                with allure.step("点击取消"):
                    print("点击取消")
                self.click_element(Select_Picture_lct.chat_select_picture_cancel)
            elif Related_Operations == "预览":
                with allure.step("点击预览"):
                    print("点击预览")
                self.click_element(Select_Picture_lct.chat_select_picture_view)
                Whether_to_send_the_original_picture = random.choice(["是","否"])
                if Whether_to_send_the_original_picture == "是":
                    with allure.step("点击原图"):
                        print("点击原图")
                    self.click_element(Select_Picture_lct.chat_select_picture_Original)
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(Select_Picture_lct.chat_select_picture_send)
                elif Whether_to_send_the_original_picture == "否":
                    with allure.step("点击发送"):
                        print("点击发送")
                    self.click_element(Select_Picture_lct.chat_select_picture_send)

    def voice_call(self):
        Return_to_action_or_continue_chatting = random.choice(["返回操作", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击更多"):
                print("点击更多")
            self.click_element(chat_lct.add_Button)
            with allure.step("点击语音通话"):
                print("点击语音通话")
            self.click_element(chat_lct.voice_call)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow4)
            with allure.step("点击挂断"):
                print("点击挂断")
            self.click_element(Album_permissions_lct.Hang_up)

    def Video_call(self):
        Return_to_action_or_continue_chatting = random.choice(["返回操作", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击更多"):
                print("点击更多")
            self.click_element(chat_lct.add_Button)
            with allure.step("点击视频通话"):
                print("点击视频通话")
            self.click_element(chat_lct.Video_call)
            with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
                print("要允许小竹熊拍摄照片和录制视频吗？-允许")
            self.click_element(Album_permissions_lct.allow1)
            with allure.step("要允许小竹熊录制音频吗？-允许"):
                print("要允许小竹熊录制音频吗？-允许")
            self.click_element(Album_permissions_lct.allow2)
            with allure.step("点击挂断"):
                print("点击挂断")
            self.click_element(Album_permissions_lct.Hang_up)

    def Shortcut_sending(self):
        Return_to_action_or_continue_chatting = random.choice(["返回操作", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击更多"):
                print("点击更多")
            self.click_element(chat_lct.add_Button)
            if self.wait_eleVisible(chat_lct.Shortcut) == True:
                with allure.step("点击快捷语"):
                    print("点击快捷语")
                self.click_element(chat_lct.Shortcut)
                Send_shortcut_randomly = random.choice([1,2,3])
                if Send_shortcut_randomly == 1:
                    with allure.step("点击发送快捷语一"):
                        print("点击发送快捷语一")
                    self.click_element(chat_lct.Shortcut_one)
                elif Send_shortcut_randomly == 2:
                    with allure.step("点击发送快捷语二"):
                        print("点击发送快捷语二")
                    self.click_element(chat_lct.Shortcut_two)
                elif Send_shortcut_randomly == 3:
                    with allure.step("点击发送快捷语三"):
                        print("点击发送快捷语三")
                    self.click_element(chat_lct.Shortcut_three)
            else:
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(chat_lct.Chat_page_return)

    def Add_shortcut(self):
        Return_to_action_or_continue_chatting = random.choice(["返回操作", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击更多"):
                print("点击更多")
            self.click_element(chat_lct.add_Button)
            if self.wait_eleVisible(chat_lct.Shortcut) == True:
                with allure.step("点击快捷语"):
                    print("点击快捷语")
                self.click_element(chat_lct.Shortcut)
                with allure.step("点击快捷语管理"):
                    print("点击快捷语管理")
                self.click_element(chat_lct.Shortcut)
                with allure.step("点击新增"):
                    print("点击新增")
                self.click_element(chat_lct.Shortcut_settings_new)
                with allure.step("输入快捷语"):
                    print("输入快捷语")
                self.input_text("家父张二河",chat_lct.Please_enter_a_quick_reply)
                Whether_to_set_shortcut = random.choice(["不设置","聊天发送或收到产品附带语","聊天发送或收到订单附带语","聊天发送或收到链接附带语","产品附带语和订单附带语","产品附带语和链接附带语","产品附带语和订单附带语和链接附带语","订单附带语和链接附带语"])
                if Whether_to_set_shortcut == "不设置":
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
                elif Whether_to_set_shortcut == "聊天发送或收到产品附带语":
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_send_or_receive_product_collateral)
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
                elif Whether_to_set_shortcut == "聊天发送或收到订单附带语":
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
                elif Whether_to_set_shortcut == "聊天发送或收到链接附带语":
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_send_or_receive_link_Epilogue)
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
                elif Whether_to_set_shortcut == "产品附带语和订单附带语":
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_send_or_receive_product_collateral)
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
                elif Whether_to_set_shortcut == "产品附带语和订单附带语和链接附带语":
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_send_or_receive_product_collateral)
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_send_or_receive_link_Epilogue)
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
                elif Whether_to_set_shortcut == "订单附带语和链接附带语":
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                    with allure.step("特别设置勾选开启"):
                        print("特别设置勾选开启")
                    self.click_element(chat_lct.Chat_send_or_receive_link_Epilogue)
                    with allure.step("点击提交"):
                        print("点击提交")
                    self.click_element(chat_lct.Submit)
            else:
                with allure.step("点击返回"):
                    print("点击返回")
                self.click_element(chat_lct.Chat_page_return)

    def Edit_shortcut(self):
        Return_to_action_or_continue_chatting = random.choice(["继续聊天", "继续聊天"])
        if Return_to_action_or_continue_chatting == "返回操作":
            with allure.step("点击返回"):
                print("点击返回")
            self.click_element(chat_lct.Chat_page_return)
        elif Return_to_action_or_continue_chatting == "继续聊天":
            with allure.step("点击更多"):
                print("点击更多")
            self.click_element(chat_lct.add_Button)
            if self.wait_eleVisible(chat_lct.Shortcut) == True:
                with allure.step("点击快捷语"):
                    print("点击快捷语")
                self.click_element(chat_lct.Shortcut)
                with allure.step("点击快捷语管理"):
                    print("点击快捷语管理")
                self.click_element(chat_lct.Shortcut)
                with allure.step("点击快捷语一"):
                    print("点击快捷语一")
                self.click_element(chat_lct.Shortcut_settings_one)
                operation = random.choice(["返回操作","编辑快捷语","删除快捷语"])
                if operation == "返回操作":
                    with allure.step("点击返回"):
                        print("点击返回")
                    self.click_element(chat_lct.Shortcut_management_return)
                elif operation == "编辑快捷语":
                    with allure.step("清空快捷语"):
                        print("清空快捷语")
                    name = self.find_element(chat_lct.Shortcut_content).text
                    # 123 光标移至末尾
                    self.driver.keyevent(123)
                    for i in range(0, len(name)):
                        # 67 退格键
                        self.driver.keyevent(67)
                    self.clear_text(chat_lct.Shortcut_content)
                    with allure.step("输入快捷语"):
                        print("输入快捷语")
                    self.input_text("宝塔镇河妖",chat_lct.Please_enter_a_quick_reply)
                    Whether_to_set_shortcut = random.choice(
                        ["不设置", "聊天发送或收到产品附带语", "聊天发送或收到订单附带语", "聊天发送或收到链接附带语", "产品附带语和订单附带语", "产品附带语和链接附带语","产品附带语和订单附带语和链接附带语", "订单附带语和链接附带语"])
                    if Whether_to_set_shortcut == "不设置":
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                    elif Whether_to_set_shortcut == "聊天发送或收到产品附带语":
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_send_or_receive_product_collateral)
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                    elif Whether_to_set_shortcut == "聊天发送或收到订单附带语":
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                    elif Whether_to_set_shortcut == "聊天发送或收到链接附带语":
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_send_or_receive_link_Epilogue)
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                    elif Whether_to_set_shortcut == "产品附带语和订单附带语":
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_send_or_receive_product_collateral)
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                    elif Whether_to_set_shortcut == "产品附带语和订单附带语和链接附带语":
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_send_or_receive_product_collateral)
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_send_or_receive_link_Epilogue)
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                    elif Whether_to_set_shortcut == "订单附带语和链接附带语":
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_to_send_or_receive_order_postscript)
                        with allure.step("特别设置勾选开启"):
                            print("特别设置勾选开启")
                        self.click_element(chat_lct.Chat_send_or_receive_link_Epilogue)
                        with allure.step("点击保存"):
                            print("点击保存")
                        self.click_element(chat_lct.preservation)
                elif operation == "删除快捷语":
                    with allure.step("点击删除"):
                        print("点击删除")
                    self.click_element(chat_lct.delete)


