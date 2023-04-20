import random

from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, clear_extract_yaml, write_extract_yaml
from api.testcase.common.atest_login_api import TestLogin


class TestLatestSampleSelectionCompany:
    #查询最新择样公司
    def test_Query_the_latest_sample_company(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetClientQuoteMainPageByLately'
        # 请求参数
        data = {
            "hallNumber":companyNumber,
            "SkipCount":1,
            "MaxResultCount":20
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url, json=data, headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        return JSON

    # 通过关键词查询最新择样公司
    def test_Query_the_latest_sample_company_with_keyword(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        keyword = "义乌"
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetClientQuoteMainPageByLately'
        # 请求参数
        data = {
            "hallNumber":companyNumber,
            "SkipCount":1,
            "keyWord":keyword,
            "MaxResultCount":20
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url, json=data, headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        return JSON

    #查看最新择样公司
    def test_View_the_latest_sample_company(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetClientQuoteMainPageByLately'
        # 请求参数
        data = {
            "hallNumber": companyNumber,
            "SkipCount": 1,
            "MaxResultCount": 20
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url, json=data, headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        company_info_list = JSON["result"]["item"]["items"]
        if len(company_info_list) > 0:
            company_info = random.choice(company_info_list)
            hallName = company_info["hallName"]
            hallNumber = company_info["hallNumber"]
            happenDate = company_info["happenDate"]
            number = company_info["number"]
            numberCount = company_info["numberCount"]
            salesLogo = company_info["salesLogo"]
            salesName = company_info["salesName"]
            salesNumber = company_info["salesNumber"]
            the_nu = company_info["the_nu"]
            #请求地址
            url1 = 'http://api.toysbear.cc/api/OrgCompanyLableListByID'
            # 请求参数
            data1 = {
                "companyNumber":salesNumber
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post",url=url1,json=data1,headers=header1)
            print(request_data1.text)
            JSON = request_data1.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            code = JSON["result"]["code"]
            if code == 200:
                chatUserId = JSON["result"]["item"]["chatUserId"]
                # 请求地址
                url2 = 'http://api.toysbear.cc/im/Message/PermissionValidator'
                #验证是否有聊天权限
                # 请求参数
                data2 = {
                    "targetId":chatUserId,
                    "chatType":1
                }
                # 请求头
                header2 = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                request_data2 = Request().request("post", url=url2, json=data2, headers=header2)
                print(request_data2.text)
                JSON = request_data2.json()
                clear_extract_yaml()
                write_extract_yaml({"JSON": JSON})
                code1 = JSON["result"]["code"]
                if code1 == 200:
                    # 请求地址
                    url3 = 'http://api.toysbear.cc/im/Message/RecordMessageHis'
                    #记录聊天历史
                    # 请求参数
                    data3 = {
                        "targetId":chatUserId,
                        "rongCloudMessageType":"RC:TxtMsg",
                        "chatType":1,
                        "content":"你好！"
                    }
                    # 请求头
                    header3 = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data3 = Request().request("post", url=url3, json=data3, headers=header3)
                    print(request_data3.text)
                    JSON = request_data3.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON": JSON})
                    return JSON
                else:
                    request_data2 = Request().request("post", url=url2, json=data2, headers=header2)
                    print(request_data2.text)
                    JSON = request_data2.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON": JSON})
                    msg = JSON["result"]["msg"]
                    print(msg)
                    return JSON
            else:
                request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
                print(request_data1.text)
                JSON = request_data1.json()
                clear_extract_yaml()
                write_extract_yaml({"JSON": JSON})
                msg = JSON["result"]["msg"]
                print(msg)
                return JSON

        else:
            request_data = Request().request("post",url=url,json=data,headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新公司择样暂无数据")


