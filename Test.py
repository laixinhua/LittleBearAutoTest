# coding:utf-8
# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'emulator-5554',
#     'platformVersion': '7.1.2',
#     'appPackage': 'com.baidu.yuedu',
#     'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
#     'noReset': 'true',
#     'automationName': 'Uiautomator2'
# }
#
#
# def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
#     '''is toast exist, return True or False
#     :Agrs:
#      - driver - 传driver
#      - text   - 页面上看到的文本内容
#      - timeout - 最大超时时间，默认30s
#      - poll_frequency  - 间隔查询时间，默认0.5s查询一次
#     :Usage:
#      is_toast_exist(driver, "看到的内容")
#     '''
#     try:
#         toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
#         toast_element = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
#         print(type(toast_element))
#         print(toast_element.text)
#         return True
#     except:
#         return False
#
#
# if __name__ == "__main__":
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#     # 等主页面activity出现
#     driver.wait_activity(".base.ui.MainActivity", 10)
#
#     driver.back()  # 点返回
#     driver.keyevent(4)  #点返回
#     # 判断是否存在toast-'再按一次退出'
#     print(is_toast_exist(driver, "再按一次退出"))

# price =  self.find_element(product_lct.Price_range_lowest_price).text
# # 123 光标移至末尾
# self.driver.keyevent(123)
# for i in range(0, len(price)):
#     # 67 退格键
#     self.driver.keyevent(67)
# self.clear_text(product_lct.Price_range_lowest_price)
import time

import requests
import os
from lxml import etree
if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kdongman/'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"}

    response = requests.get(url=url,headers=header)
    page_text = response.text
    selector = etree.HTML(page_text)
    list_li = selector.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in list_li:
        img_src = "https://pic.netbian.com"+li.xpath('./a/img/@src')[0]
        print(img_src)
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        print(img_name)
        img_data = requests.get(url=img_src,headers=header).content
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载完成!')

print(123)



#
#
# import requests
# from lxml import etree
# import os
# if __name__ == '__main__':
#     url = 'https://pic.netbian.com/4kdongman/'
#     #爬取到页面源码数据
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49'
#     }
#     response = requests.get(url=url,headers=headers)
#     #手动设定编码
#     # response.encoding = 'utf-8'
#     # print(response)
#     page_text = response.text
#     # print(page_text)
#     #数据解析：src属性值 alt属性值
#     tree = etree.HTML(page_text)
#     li_list = tree.xpath('//div[@class="slist"]/ul/li')
#
#     # #创建一个文件夹
#     if not os.path.exists('./picLibs'):
#         os.mkdir('./picLibs')
#     for li in li_list:
#         img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
#         img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
#         #通用处理中文乱码解决方案
#         img_name = img_name.encode('iso-8859-1').decode('gbk')
#         # print(img_name,img_src)
#         #请求图片，进行持久化存储
#         img_data = requests.get(url=img_src,headers=headers).content
#         img_path = 'picLibs/'+img_name
#         with open(img_path,'wb') as fp:
#             fp.write(img_data)
#             print(img_name,'下载成功！！')

