import pytest,time,os
from common import startappium
from common.sendDtb import Message
from common.xiaoding import Xiaoding

cur_path = os.path.dirname(os.path.realpath(__file__))
result_path = cur_path+'/web/autotest/ui/result'
result_port = cur_path+'/web/autotest/ui/result_port'
if not os.path.exists(result_path):os.makedirs(result_path)#如果路径不存在则自动新建路径
if not os.path.exists(result_port):os.makedirs(result_port)
now = time.strftime("%Y-%m-%d-%H-%M-%S")
report_file = 'report/'+now+'_test_result.html'
if __name__ == '__main__':
    #启动appium server
    startappium.appium_start('127.0.0.1',4723)

    #pytest.main(['test_cases/atest_login_api.py',"--html=%s"%(report_file)]) #生成测试报告
    pytest.main(['--alluredir',result_path, #allure生成json、txt文件到指定路径
                 #'test_cases/atest_login_api.py', #指定运行文件
                 #"--html=%s"%(report_file), #生成测试报告
                 '-s', #打印print信息
                 '-vvv', #打印详细信息
                 #'-m','smoke',  #只执行标记smoke的用例
                 '--reruns','1', #失败重跑1次
                 '--reruns-delay','1' #失败重跑间隔1秒
                 ])
    # 将result里的json和txt转换为html测试报告
    os.system("allure generate "+result_path+" -o "+result_port+" --clean") #-o是指向目标生成测试报告的目录 --clean-alluredir：如果已经存在报告，那就先清空，然后再生成新的测试报告
    #关闭appium server
    startappium.appium_close(4723)
    #通过钉钉发送测试报告
    Message().send_text()
    Xiaoding().dingtalk_robot()

