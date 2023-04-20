import pytest,os
from selenium import webdriver
from appium import webdriver
import yaml
import logging
from py._xmlgen import html
cur_path = os.path.dirname(os.path.realpath(__file__))
import allure
driver = None

#获取配置文件路径
def ReadPath():
    rootPath = os.path.abspath((os.path.dirname(__file__)))
    path = os.path.join(rootPath, "config/config.yaml")
    return path
#读取yaml文件
def ReadYaml(path):
    with open(path,"r+",encoding="utf-8") as file:
        data = yaml.load(stream=file,Loader=yaml.FullLoader)
        return data

@pytest.fixture()
def app_page():
    logging.info('-----测试开始-----')
    path = ReadPath()
    data = ReadYaml(path)
    global driver
    driver = webdriver.Remote('http://' + str(data['desired_caps']['ip']) + ':' + str(data['desired_caps']['port']) + '/wd/hub',data['desired_caps'])
    yield driver
    logging.info('-----测试结束-----')
    driver.quit()

#通过conftest来实现报告的描述
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1,html.th('Description'))  #html报告中插入一列，列头名为Description

@pytest.mark.optionalhook
def pytest_html_results_table_row(report,cells):
    try:
        cells.insert(1,html.td(report.description))
    except:
        pass

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item,cell):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#
# #错误用例保存截图
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report,'extra',[])
#
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report,'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::","_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:375px;" onclick="window.open(this.src)" align="right"/></div>'%screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    #获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    #仅获取用例call且执行结果是失败的情况，不包含setup和teardown
    if rep.when == "call" and rep.failed:
        #添加allure报告截图
        if hasattr(driver,"get_screenshot_as_png"):
            with allure.step('添加失败截图'):
                allure.attach(driver.get_screenshot_as_png(),"失败截图",allure.attachment_type.PNG)

