import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from common.logger import Log
import datetime


class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.logger = Log()


    # 滑动（上下左右滑动）开始的x坐标，开始的y坐标，结束的x坐标，结束的y坐标，延迟毫秒秒数
    def swipe(self,start_x, start_y, end_x, end_y, duration=0):
        # 获取屏幕的尺寸
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        self.driver.swipe(start_x=x * start_x, start_y=y * start_y, end_x=x * end_x, end_y=y * end_y,duration=duration)

    #等待元素可见
    def wait_eleVisible(self,locator,by=MobileBy.XPATH,wait=1,requence=0.5):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver,wait,requence).until(EC.visibility_of_element_located((by,locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            self.logger.info("等待元素可见：{0},起始时间：{1},等待时长：{2}".format(locator,start,wait_times))
            return True
        except Exception as e:
            self.logger.error("等待元素可见异常{0}".format(e))
            return False

    #等待元素存在
    def wait_elePrences(self,locator,by=MobileBy.XPATH,wait=1,requence=0.5):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver,wait,requence).until(EC.visibility_of_element_located((by,locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            self.logger.info("等待元素可见：{0},起始时间：{1},等待时长：{2}".format(locator,start,wait_times))
        except Exception as e:
            self.logger.error("查看元素可见异常{0}".format(e))

    #查找元素
    def find_element(self,locator,by=MobileBy.XPATH):
        self.logger.info("开始查找元素：{0}={1}".format(by,locator))
        try:
            return self.driver.find_element(by,locator)
        except Exception as e:
            self.logger.error("元素查找不到{0}".format(e))

    # 清空输入框
    def clear_text(self,locator,by=MobileBy.XPATH):
        self.logger.info("开始查找元素：{0}={1}".format(by, locator))
        try:
            text = self.find_element(by,locator).text
            # 123 光标移至末尾
            self.driver.keyevent(123)
            for i in range(0, len(text)):
                # 67 退格键
                self.driver.keyevent(67)
        except Exception as e:
            self.logger.error("元素查找不到{0}".format(e))

    #智能查找元素
    def find_element_wait_and_focus(self,locator,wait_ele,by=MobileBy.XPATH,wait=30,requence=0.5,index=None):
        #查找元素
        self.logger.info("开始查找元素：{0}={1}".format(by,locator))
        #等待元素
        if wait_ele == 'visibility':
            self.wait_eleVisible(locator,by,wait,requence)
        else:
            self.wait_elePrences(locator,by,wait,requence)
        try:
            return self.driver.find_element(by,locator)
        except Exception as e:
            self.logger.error("元素查找不到{0}".format(e))
            raise

    #查找多个元素
    def find_elements(self,locator,by=MobileBy.XPATH):
        self.logger.info("开始查找符合表达式的所有元素：{0}={1}".format(by,locator))
        try:
            return self.driver.find_elements(by,locator)
        except Exception as e:
            self.logger.error("元素查找不到{0}".format(e))
            raise

    #元素的点击操作
    def click_element(self,locator,wait_ele='visibility',by=MobileBy.XPATH,wait=30,requence=0.5,index=None):
        ele = self.find_element_wait_and_focus(locator,wait_ele,by,wait,requence,index)
        try:
            self.logger.info("对元素{0}进行点击操作".format(locator))
            ele.click()
        except Exception as e:
            self.logger.error("元素点击操作失败{0}".format(e))
            raise

    #元素的输入操作
    def input_text(self,value,locator,by=MobileBy.XPATH,wait=30,requence=0.5,wait_ele="visibility",index=None):
        ele = self.find_element_wait_and_focus(locator,wait_ele,by,wait,requence,index)
        try:
            self.logger.info("在元素：{0}={1}中输入内容：{2}".format(by,locator,value))
            ele.clear()
            ele.send_keys(value)
        except Exception as e:
            self.logger.error("元素输入操作失败{0}".format(e))
            raise

    #获取元素的属性值
    def get_element_attribute(self,attr_name,locator,by=MobileBy.XPATH,wait=30,requence=0.5,wait_ele="visibility",index=None):
        ele = self.find_element_wait_and_focus(locator,wait_ele,by,wait,requence,index)
        try:
            self.logger.info("获取元素{0}={1}的属性值：{2}".format(by,locator,attr_name))
            return ele.get_attribute(attr_name)
        except Exception as e:
            self.logger.error("获取元素属性失败{0}".format(e))
            raise

    #获取元素的文本内容
    def get_text(self,locator,by=MobileBy.XPATH,wait=30,requence=0.5,wait_ele="visibility",index=None):
        ele = self.find_element_wait_and_focus(locator,wait_ele,by,wait,requence,index)
        try:
            self.logger.info("获取元素{0}={1}的文本内容".format(by,locator))
            return ele.text
        except Exception as e:
            self.logger.error("获取元素文本失败{0}".format(e))
            raise

    #确定要操作的元素 - 查找多个和查找单个。确定元素操作对象
    def _get_element(self,locator,by,index=None):
        if index is not None:
            #在查找到多个元素的基础上，随机选择其中的一个
            import random
            eles = self.find_elements(locator,by)
            if index == -1 or index < 0:
                pos = random.randint(0,len(eles)-1)
                return eles[pos]
            else:
                return eles[index]
        else:
            return self.find_elements(locator,by)

    #封装toast判断
    def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - text   - 页面上看到的文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            print("未检测到toast弹框信息")
            return False

    #获取屏幕高度和宽度
    def get_screen_size(self):
        x = self.driver.get_window_size()['width']  # 获取屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取屏幕高度
        return (x, y)

    def swipeLeft(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1)
        print('向左滑动')

    def swipeRight(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1)
        print('向右滑动')

    def swipeUp(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2)
        print('向上滑动')

    def swipeDown(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2)
        print('向下滑动')





