import pytest
import logging

from page_obj.common.login_page import LoginPage
import allure
from hamcrest import *

#赋值调用
myskip = pytest.mark.skip(reason='已知bug不执行')#跳过方法或用例，不执行被标记的方法或用例
@allure.feature("登录模块")#allure添加模块区分
class TestLogin:
    #@pytest.mark.smoke#标记冒烟测试用例
    @allure.story("手机登录")#allure子模块名称
    @allure.title("点击同意")#allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)#失败重跑
    def test_login_click_agree(self,app_page):
        """点击同意"""  #这是描述
        LoginPage(app_page).click_agree()
        logging.info("开始断言")

    #@myskip
    @allure.story("手机登录")  # allure子模块名称
    @allure.title("点击不同意")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)#失败重跑
    def test_login_click_disagree(self,app_page):
        LoginPage(app_page).click_disagree()
        logging.info("开始断言")

    @allure.story("手机登录")  # allure子模块名称
    @allure.title("查看协议")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_Agreement(self, app_page):
        LoginPage(app_page).View_Agreement()
        logging.info("开始断言")

    @allure.story("手机登录")  # allure子模块名称
    @allure.title("再次查看")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_View_again(self, app_page):
        LoginPage(app_page).View_again()
        logging.info("开始断言")


    @allure.story("手机登录")  # allure子模块名称
    @allure.title("退出应用")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_quit(self, app_page):
        LoginPage(app_page).quit()
        logging.info("开始断言")

    @allure.story("手机登录")  # allure子模块名称
    @allure.title("登录应用")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_login(self, app_page):
        # isTest = False #True 测试环境 False 正式环境
        LoginPage(app_page).login('13538262412',"868385",app_page)
        logging.info("开始断言")
        assert_that("欢迎来到小竹熊", contains_string('欢迎来到小竹熊'),"登录失败，请联系开发查找原因！")


    @allure.story("手机登录")  # allure子模块名称
    @allure.title("验证码登录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_login_with_verification_code(self, app_page):
        #isTest = False #True 测试环境 False 正式环境
        LoginPage(app_page).login_with_verification_code('13538262412',app_page)
        logging.info("开始断言")
        assert "欢迎来到小竹熊" in app_page.page_source


    @allure.story("手机登录")  # allure子模块名称
    @allure.title("微信登录")  # allure用例标题
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 失败重跑
    def test_Wechat_login(self, app_page):
        LoginPage(app_page).click_agree()
        LoginPage(app_page).Wechat_login()


