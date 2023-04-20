import subprocess
import os
import platform
import time
import logging
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs/autotest/appium_log')
if not os.path.exists(log_path):os.makedirs(log_path) #判断路径是否存在，不存在则新建路径

platform_type = platform.system()

def appium_start(host,port):
    '''
    启动appium server
    :param host:
    :param port:
    :return:
    '''
    # #指定bp端口号
    # bootstrap_port = str(port+1)
    # if platform_type == 'Darwin': #mac
    #     cmd = 'appium -a'+host+'-p'+str(port)+'-bp'+str(bootstrap_port)
    #     subprocess.Popen(cmd,shell=True,stdout=open(log_path+"/"+str(port)+'.log','a'),stderr=subprocess.STDOUT)

    bootstrap_port = str(port + 1)
    # 把在cmd弹窗输入的命令，直接写到这里
    # cmd = 'start /b appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
    # 去掉 “/b”，即可以打开cmd弹窗运行
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    # 打印输入的cmd命令，及时间
    #print("%s at %s " % (cmd, time.ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open(log_path + "/" + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)






def appium_close(port):
    '''
    关闭appium server
    :param port:
    :return:
    '''
    p = os.popen(f'lsof -i tcp:{port}')
    p0 = p.read()
    if p0.strip()!='':
        p1 = int(p0.split('\n')[1].split()[1]) #获取进程号
        os.popen(f'kill {p1}') #结束进程
        with open(log_path+"/"+str(port)+'.log','a') as ft:
            ft.write("关闭appium server"+str(port))

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    appium_start(host,port)
    appium_close(port)
