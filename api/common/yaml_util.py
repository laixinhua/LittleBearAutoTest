import os
import yaml
from api.config import config
from api.common.request_util import Request

#读取extract.yaml文件
def read_extract_yaml(key):
    with open(config.extract_yaml_dir,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

#写入extract.yaml文件
def write_extract_yaml(data):
    with open(config.extract_yaml_dir,mode='a',encoding='utf-8') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)

#清除extract.yaml文件
def clear_extract_yaml():
    with open(config.extract_yaml_dir,mode='w',encoding='utf-8') as f:
        f.truncate()

#定义全局变量-是否测试环境
def isTest():
    global isTest
    isTest = True
    return isTest

def gettoken():
    # 请求地址
    url1 = 'http://api.toysbear.cc/auth/api/GetToken'
    url2 = 'https://api.toysbear.net/auth/api/GetToken'
    # 请求参数
    data = {
        "PlatForm": "android",
        "CompanyNum": "LittleBearWeb"
    }
    # 请求头
    header = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    # global isTest
    # isTest = True
    if isTest() == True:
        # 调用request并且传参进去
        request_data = Request().request("post",url=url1, json=data, headers=header)
    else:
        # 调用request并且传参进去
        request_data = Request().request("post",url=url2, json=data, headers=header)
    # 打印响应结果
    print(request_data.json())
    print(request_data.json()["result"]["item"])
    write_extract_yaml({"token": request_data.json()["result"]["item"]})


def writetoken():
    # 获取token
    token = read_extract_yaml("token")
    print(token)
    # 请求地址
    url = 'http://api.toysbear.cc/auth/api/Authenticate'
    # 请求参数
    data = {
        "verificationCode": "868385",
        "loginType": "VerificationCode",
        "userAccountOrUserMobile": "13538262412",
        "platForm": "Android",
        "rememberClient": "true"
    }
    # 请求头
    header = {
        "Content-Type": "application/json; charset=UTF-8",
        "Utoken": token
    }
    # 调用request并且传参进去
    request_data = Request().request("post", url=url, json=data, headers=header)
    # 打印响应结果
    print(request_data.text)
    Utoken = request_data.json()["result"]["accessToken"]
    write_extract_yaml({"accessToken": request_data.json()["result"]["accessToken"]})
    return Utoken