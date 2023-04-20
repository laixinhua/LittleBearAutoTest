from dingtalkchatbot.chatbot import DingtalkChatbot
import datetime

class Xiaoding():
    def __init__(self):
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.url = 'http://localhost:63342/LittleBearAutoTest/web/autotest/ui/result_port/index.html'
        self.mobile = ['13642562621']
        self.text = ('''APP自动化测试报告'''
                     +'''\n\n---\n\n'''
                     +'''<font color=\'#778899\' size=2>项目名称：小竹熊</font>\n\n'''
                     +'''<font color=\'#778899\' size=2>测试报告：[点击查看](%s)</font>\n\n'''
                     +'''<font color=\'#778899\' size=2>相关人员：@%s</font>'''
                     +'''\n\n---\n\n'''
                     +'''播报时间：%s''')%(self.url,self.mobile[0],self.time)
        self.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e4a5b3622e323ee47b9b96a1a495e897a0c4656694b711f11d790ff94d8f7f62'

    def dingtalk_robot(self):
        ddrobot = DingtalkChatbot(self.webhook)
        ret = ddrobot.send_markdown(title='Python自动化',text=self.text,is_at_all=False,at_mobiles=self.mobile)
        print(ret)

if __name__ == '__main__':
    Xiaoding().dingtalk_robot()
