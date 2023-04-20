import random

import pytest as pytest
from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, write_extract_yaml, isTest, clear_extract_yaml


class TestLogin:
    # 获取验证码
    def test_get_verification_code(self):
        # 请求地址
        url1 = 'http://api.toysbear.cc/api/SendSMS'
        url2 = 'https://api.toysbear.net/api/SendSMS'
        # 请求参数
        data = {
            "PhoneNumber": 13538262412,  # phone_number
            "MessageType": "SignIn"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
        }
        # global isTest
        # isTest = True #文件里的全局变量只能当前文件用 若像要跨文件使用全局需将全局变量写到函数里
        if isTest() == True:
            # 调用request并且传参进去
            request_data = Request().request("post", url=url1, json=data, headers=header)
        else:
            request_data = Request().request("post", url=url2, json=data, headers=header)
        # 打印响应结果
        print(request_data.text)
        print("验证码：" + request_data.json()["result"]["object"]["verificationCode"])
        verificationCode = request_data.json()["result"]["object"]["verificationCode"]
        write_extract_yaml({"verificationCode": request_data.json()["result"]["object"]["verificationCode"]})
        return verificationCode

    #获取验证码
    def test_get_verification_code_with_phone_number(self,phone_number):
        #请求地址
        url1 = 'http://api.toysbear.cc/api/SendSMS'
        url2 = 'https://api.toysbear.net/api/SendSMS'
        #请求参数
        data = {
            "PhoneNumber": phone_number,#phone_number
            "MessageType": "SignIn"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
        }
        # global isTest
        # isTest = True #文件里的全局变量只能当前文件用 若像要跨文件使用全局需将全局变量写到函数里
        if isTest() == True:
            # 调用request并且传参进去
            request_data = Request().request("post",url=url1,json=data,headers=header)
        else:
            request_data = Request().request("post",url=url2,json=data,headers=header)
        # 打印响应结果
        print(request_data.text)
        print("验证码："+request_data.json()["result"]["object"]["verificationCode"])
        verificationCode = request_data.json()["result"]["object"]["verificationCode"]
        write_extract_yaml({"verificationCode": request_data.json()["result"]["object"]["verificationCode"]})
        return verificationCode

    #登录
    def test_login(self):
        #获取验证码
        TestLogin().test_get_verification_code()
        #获取token
        token = read_extract_yaml("token")
        print(token)
        #请求地址
        url1 = 'http://api.toysbear.cc/auth/api/Authenticate'
        url2 = 'https://api.toysbear.net/auth/api/Authenticate'
        verificationCode = read_extract_yaml("verificationCode")
        #请求参数
        data = {
            "verificationCode":verificationCode,
            "loginType":"VerificationCode",
            "userAccountOrUserMobile":"13538262412",
            "platForm":"Android",
            "rememberClient":"true"
        }
        #请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": token

        }
        if isTest() == True:
            #调用request并且传参进去
            request_data = Request().request("post",url=url1,json=data,headers=header)
        else:
            # 调用request并且传参进去
            request_data = Request().request("post",url=url2,json=data,headers=header)
        #打印响应结果
        print(request_data.text)
        Utoken = request_data.json()["result"]["accessToken"]
        write_extract_yaml({"accessToken":request_data.json()["result"]["accessToken"]})
        return Utoken

    # 通用验证码登录
    def test_login_Universal_verification_code(self):
        # 获取token
        token = read_extract_yaml("token")
        print(token)
        # 请求地址
        url1 = 'http://api.toysbear.cc/auth/api/Authenticate'
        url2 = 'https://api.toysbear.net/auth/api/Authenticate'
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
        if isTest() == True:
            # 调用request并且传参进去
            request_data = Request().request("post", url=url1, json=data, headers=header)
        else:
            # 调用request并且传参进去
            request_data = Request().request("post", url=url2, json=data, headers=header)
        # 打印响应结果
        print(request_data.text)
        #存放返回数据
        JSON = request_data.json()
        write_extract_yaml({"JSON":JSON})
        # accessToken = request_data.json()["result"]["accessToken"]
        # write_extract_yaml({"accessToken": accessToken})
        # birthday = read_extract_yaml("userInfo")["birthday"]
        # print(birthday)
        return JSON

    #随机角色选择
    def test_Random_Select_Role(self):
        #登录
        TestLogin().test_login_Universal_verification_code()
        # 获取accessToken
        accessToken = read_extract_yaml("JSON")["result"]["accessToken"]
        #请求地址
        url = 'http://api.toysbear.cc/auth/api/UserAffiliAtecompany'
        companylist = read_extract_yaml("JSON")["result"]["commparnyList"]
        UserId = read_extract_yaml("JSON")["result"]["userInfo"]["id"]
        # print(list(enumerate(companylist)))
        # print(list(enumerate(companylist))[1][1]["companyName"])
        # companyType = list(enumerate(companylist))[1][1]["companyType"]

        # rand = random(companylist.len())
        # # companylist[rand][1][""]
        # commparnyId = companylist[rand][1]["commparnyId"]
        # companyNumber = i[1]["companyNumber"]
        # companyName = i[1]["companyName"]
        # companyType = i[1]["companyType"]
        # companyLogo = i[1]["companyLogo"]

        companyinfo = random.choice(list(enumerate(companylist)))
        commparnyId = companyinfo[1]["commparnyId"]
        companyNumber = companyinfo[1]["companyNumber"]
        companyName = companyinfo[1]["companyName"]
        companyType = companyinfo[1]["companyType"]
        companyLogo = companyinfo[1]["companyLogo"]
        #print(a[1]["companyName"])
        # for i in list(enumerate(companylist)):
        #     # print(i)
        #     # print(type(i[1]))
        #     commparnyId = i[1]["commparnyId"]
        #     companyNumber = i[1]["companyNumber"]
        #     companyName = i[1]["companyName"]
        #     companyType = i[1]["companyType"]
        #     companyLogo = i[1]["companyLogo"]

        # print(companyNumber)

        #请求参数
        data = {
            "CompanyNumber": companyNumber,
            "UserId": UserId
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": accessToken
        }
        request_data = Request().request("post", url=url, json=data, headers=header)
        # 打印响应结果
        print(request_data.text)
        clear_extract_yaml()
        JSON = request_data.json()
        write_extract_yaml({"JSON": JSON})
        return JSON

    def test_Company_Role_Login(self):
        #公司角色登录
        TestLogin().test_login_Universal_verification_code()
        #获取accessToken
        accessToken = read_extract_yaml("JSON")["result"]["accessToken"]
        #请求地址
        url = 'http://api.toysbear.cc/auth/api/UserAffiliAtecompany'
        companylist = read_extract_yaml("JSON")["result"]["commparnyList"]
        UserId = read_extract_yaml("JSON")["result"]["userInfo"]["id"]
        for i in companylist:
            print(i)
            companyLogo = i["companyLogo"]
            companyName = i["companyName"]
            companyNumber = i["companyNumber"]
            companyType = i["companyType"]
            unreadCount = i["unreadCount"]
            while companyType == "Sales":
                # 请求参数
                data = {
                    "CompanyNumber": companyNumber,
                    "UserId": UserId
                }
                # 请求头
                header = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": accessToken
                }
                request_data = Request().request("post", url=url, json=data, headers=header)
                # 打印响应结果
                print(request_data.text)
                clear_extract_yaml()
                JSON = request_data.json()
                write_extract_yaml({"JSON": JSON})
                return JSON

    def test_Hall_Role_Login(self):
        #展厅角色登录
        TestLogin().test_login_Universal_verification_code()
        #获取accessToken
        accessToken = read_extract_yaml("JSON")["result"]["accessToken"]
        #请求地址
        url = 'http://api.toysbear.cc/auth/api/UserAffiliAtecompany'
        companylist = read_extract_yaml("JSON")["result"]["commparnyList"]
        UserId = read_extract_yaml("JSON")["result"]["userInfo"]["id"]
        for i in companylist:
            print(i)
            companyLogo = i["companyLogo"]
            companyName = i["companyName"]
            companyNumber = i["companyNumber"]
            companyType = i["companyType"]
            unreadCount = i["unreadCount"]
            while companyType == "Exhibition":
                # 请求参数
                data = {
                    "CompanyNumber": companyNumber,
                    "UserId": UserId
                }
                # 请求头
                header = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": accessToken
                }
                request_data = Request().request("post", url=url, json=data, headers=header)
                # 打印响应结果
                print(request_data.text)
                clear_extract_yaml()
                JSON = request_data.json()
                write_extract_yaml({"JSON": JSON})
                return JSON

    def test_Vendor_Role_Login(self):
        #厂商角色登录
        TestLogin().test_login_Universal_verification_code()
        #获取accessToken
        accessToken = read_extract_yaml("JSON")["result"]["accessToken"]
        #请求地址
        url = 'http://api.toysbear.cc/auth/api/UserAffiliAtecompany'
        companylist = read_extract_yaml("JSON")["result"]["commparnyList"]
        UserId = read_extract_yaml("JSON")["result"]["userInfo"]["id"]
        for i in companylist:
            print(i)
            companyLogo = i["companyLogo"]
            companyName = i["companyName"]
            companyNumber = i["companyNumber"]
            companyType = i["companyType"]
            unreadCount = i["unreadCount"]
            while companyType == "Supplier":
                # 请求参数
                data = {
                    "CompanyNumber": companyNumber,
                    "UserId": UserId
                }
                # 请求头
                header = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": accessToken
                }
                request_data = Request().request("post", url=url, json=data, headers=header)
                # 打印响应结果
                print(request_data.text)
                clear_extract_yaml()
                JSON = request_data.json()
                write_extract_yaml({"JSON": JSON})
                return JSON

    #游客登录
    def test_Visitor_login(self):
        # 获取token
        token = read_extract_yaml("token")
        print(token)
        # 请求地址
        url1 = 'http://api.toysbear.cc/auth/api/TouristLogin'
        url2 = 'https://api.toysbear.net/auth/api/TouristLogin'
        # 请求参数
        data = {
            "platForm":"android",
            "UserAccountOrUserMobile":"00000000-4aea-47b3-0000-00000fae77d5"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": token

        }
        if isTest() == True:
            # 调用request并且传参进去
            request_data = Request().request("post", url=url1, json=data, headers=header)
        else:
            # 调用request并且传参进去
            request_data = Request().request("post", url=url2, json=data, headers=header)
        # 打印响应结果
        print(request_data.text)
        companyName = request_data.json()["result"]["commparnyList"][0]["companyName"]
        #print(companyName)
        write_extract_yaml({"companyName": request_data.json()["result"]["commparnyList"][0]["companyName"]})
        return companyName



