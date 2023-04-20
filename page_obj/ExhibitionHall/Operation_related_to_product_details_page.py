import allure

from common.basepage import BasePage
from page_lct.ExhibitionHall import product_details_lct
from page_lct.common import Album_permissions_lct, chat_lct, Toy_circle_lct


class OperationRelatedToProductDetailsPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(product_details_lct.Back_button)

    def View_product_pictures(self):
        # allure添加测试步骤
        with allure.step("查看产品图片"):
            print("查看产品图片")
        self.click_element(product_details_lct.Product_pictures)

    def Click_the_Favorites_button(self):
        # allure添加测试步骤
        with allure.step("点击收藏"):
            print("点击收藏")
        self.click_element(product_details_lct.Collection)

    def Click_the_screenshot(self):
        # allure添加测试步骤
        with allure.step("点击截屏"):
            print("点击截屏")
        self.click_element(product_details_lct.Screenshot)
        with allure.step("要允许小竹熊拍摄照片和录制视频吗？-允许"):
            print("要允许小竹熊拍摄照片和录制视频吗？-允许")
        self.click_element(Album_permissions_lct.allow1)
        with allure.step("要允许小竹熊录制音频吗？-允许"):
            print("要允许小竹熊录制音频吗？-允许")
        self.click_element(Album_permissions_lct.allow2)
        with allure.step("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许"):
            print("要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许")
        self.click_element(Album_permissions_lct.allow1)

    def Screenshot_send_to_friends(self):
        self.Click_the_screenshot()
        # allure添加测试步骤
        with allure.step("发送给好友"):
            print("发送给好友")
        self.click_element(product_details_lct.Send_to_friends)
        with allure.step("选择好友"):
            print("选择好友")
        self.click_element(product_details_lct.Friend1)
        with allure.step("点击确定"):
            print("点击确定")
        self.click_element(product_details_lct.determine)
        with allure.step("发送聊天信息"):
            print("发送聊天信息")
        self.input_text("你好！",chat_lct.Content_input_box)
        with allure.step("点击发送"):
            print("点击发送")
        self.click_element(chat_lct.send)

    def Screenshot_release_toy_circle(self):
        self.Click_the_screenshot()
        # allure添加测试步骤
        with allure.step("发布玩具圈"):
            print("发布玩具圈")
        self.click_element(product_details_lct.Release_toy_circle)
        with allure.step("输入发布内容"):
            print("输入发布内容")
        self.input_text("产品图片分享",Toy_circle_lct.Release_content)
        with allure.step("点击发布"):
            print("点击发布")
        self.click_element(Toy_circle_lct.release)

    def Screenshot_Save_Picture(self):
        self.Click_the_screenshot()
        with allure.step("点击保存图片"):
            print("点击保存图片")
        self.click_element(product_details_lct.Save_Picture)

    def Screenshot_Cancel_sending(self):
        self.Click_the_screenshot()
        with allure.step("点击取消"):
            print("点击取消")
        self.click_element(product_details_lct.cancel)

    def Click_Shop(self):
        with allure.step("点击店铺"):
            print("点击店铺")
        self.click_element(product_details_lct.shop)

    def Click_Customer_Service(self):
        with allure.step("点击客服"):
            print("点击客服")
        self.click_element(product_details_lct.customer_service)

    def Send_product_information_to_customer_service(self):
        self.Click_Customer_Service()
        with allure.step("发送产品信息给客服"):
            print("发送产品信息给客服")
        self.click_element(chat_lct.send)
        with allure.step("发送消息"):
            print("发送消息")
        self.input_text("想要了解这个产品的相关情况",chat_lct.Content_input_box)
        with allure.step("点击发送"):
            print("点击发送")
        self.click_element(chat_lct.send)

    def Click_Send(self):
        with allure.step("点击发送"):
            print("点击发送")
        self.click_element(product_details_lct.send_out)









