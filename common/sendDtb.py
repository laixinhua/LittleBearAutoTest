from dingtalkchatbot.chatbot import DingtalkChatbot

class Message():

    def messge(self):
        report_url = 'http://localhost:63342/LittleBearAutoTest/web/autotest/ui/result_port/index.html'
        msg = 'APP自动化测试脚本执行完成，测试结果请查看测试报告，测试报告地址为：{0}'.format(report_url)
        return msg

    def send_text(self):
        #WebHook地址
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e4a5b3622e323ee47b9b96a1a495e897a0c4656694b711f11d790ff94d8f7f62'
        #初始化机器人小钉
        xiaoding = DingtalkChatbot(webhook)
        at_mobiles = ['13642562621']#艾特钉钉群成员账号
        msg = self.messge()
        xiaoding.send_text(msg=msg,is_at_all=False,at_mobiles=at_mobiles)

if __name__ == '__main__':
    Message().send_text()


