import random

from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, clear_extract_yaml, write_extract_yaml
from api.testcase.common.atest_login_api import TestLogin


class TestLatestSettledManufacturer:
    #查询最新入驻厂商
    def test_Query_Latest_settled_manufacturer(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetCompanyByNewHallPage'
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

    # 通过关键词查询最新入驻厂商
    def test_Query_Latest_settled_manufacturer_with_keyword(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        companyName = "成卓玩具"
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetCompanyByNewHallPage'
        # 请求参数
        data = {
            "hallNumber":companyNumber,
            "companyName":companyName,
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

    #查看最新入驻厂商
    def test_View_the_latest_settled_manufacturers(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetCompanyByNewHallPage'
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
            companyLogo = company_info["companyLogo"]
            companyName = company_info["companyName"]
            companyNumber = company_info["companyNumber"]
            contactsMan = company_info["contactsMan"]
            createdBy = company_info["createdBy"]
            createdOn = company_info["createdOn"]
            deleteBy = company_info["deleteBy"]
            deleteTime = company_info["deleteTime"]
            id = company_info["id"]
            isDelete = company_info["isDelete"]
            modifyBy = company_info["modifyBy"]
            modifyOn = company_info["modifyOn"]
            phoneNumber = company_info["phoneNumber"]
            sumNumber = company_info["sumNumber"]
            #请求地址
            url1 = 'http://api.toysbear.cc/api/CompanyByID'
            url2 = 'http://api.toysbear.cc/productapi/BearProduct/GetSupplierStoreProductPage'
            # 请求参数
            data1 = {
                "CompanyNumber":companyNumber
            }
            # 请求参数
            data2 = {
                "skipCount":"1",
                "SupplierNumber":companyNumber,
                "maxResultCount":"100"
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            print(request_data1.text)
            JSON1 = request_data1.json()
            request_data2 = Request().request("post", url=url2, json=data2, headers=header1)
            print(request_data2.text)
            JSON2 = request_data2.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON1": JSON1})
            write_extract_yaml({"JSON2": JSON2})
            totalCount = JSON2["result"]["item"]["totalCount"]
            if totalCount == 0:
                print("店铺内暂无产品")
            else:
                print("店铺有{}款产品".format(totalCount))
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新入驻厂商暂无数据")
            return JSON

    # 查看最新入驻厂商-店铺关键词查询
    def test_View_the_latest_settled_manufacturers_Store_Search_Products(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetCompanyByNewHallPage'
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
            companyLogo = company_info["companyLogo"]
            companyName = company_info["companyName"]
            companyNumber = company_info["companyNumber"]
            contactsMan = company_info["contactsMan"]
            createdBy = company_info["createdBy"]
            createdOn = company_info["createdOn"]
            deleteBy = company_info["deleteBy"]
            deleteTime = company_info["deleteTime"]
            id = company_info["id"]
            isDelete = company_info["isDelete"]
            modifyBy = company_info["modifyBy"]
            modifyOn = company_info["modifyOn"]
            phoneNumber = company_info["phoneNumber"]
            sumNumber = company_info["sumNumber"]
            # 请求地址
            url1 = 'http://api.toysbear.cc/api/CompanyByID'
            url2 = 'http://api.toysbear.cc/productapi/BearProduct/GetSupplierStoreProductPage'
            # 请求参数
            data1 = {
                "CompanyNumber": companyNumber
            }
            # 请求参数
            data2 = {
                "skipCount": "1",
                "SupplierNumber": companyNumber,
                "maxResultCount": "100"
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            print(request_data1.text)
            JSON1 = request_data1.json()
            request_data2 = Request().request("post", url=url2, json=data2, headers=header1)
            print(request_data2.text)
            JSON2 = request_data2.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON1": JSON1})
            write_extract_yaml({"JSON2": JSON2})
            # 请求地址
            url3 = 'http://api.toysbear.cc/productapi/BearProduct/GetSupplierStoreProductPage'
            # 请求参数
            keyword = "娃娃"
            data3 = {
                "skipCount":"1",
                "maxResultCount":"100",
                "keyWord":keyword,
                "SupplierNumber":companyNumber
            }
            # 请求头
            header3 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data3 = Request().request("post", url=url3, json=data3, headers=header3)
            print(request_data3.text)
            JSON3 = request_data3.json()
            write_extract_yaml({"JSON3": JSON3})
            totalCount = JSON3["result"]["item"]["totalCount"]
            if totalCount == 0:
                print("查询结果为{}".format(totalCount))
            else:
                print("查询结果为{}".format(totalCount))
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新入驻厂商暂无数据")
            return JSON

    # 查看最新入驻厂商-关注店铺
    def test_View_the_latest_settled_manufacturers_Follow_the_store(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetCompanyByNewHallPage'
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
            companyLogo = company_info["companyLogo"]
            companyName = company_info["companyName"]
            companyNumber = company_info["companyNumber"]
            contactsMan = company_info["contactsMan"]
            createdBy = company_info["createdBy"]
            createdOn = company_info["createdOn"]
            deleteBy = company_info["deleteBy"]
            deleteTime = company_info["deleteTime"]
            id = company_info["id"]
            isDelete = company_info["isDelete"]
            modifyBy = company_info["modifyBy"]
            modifyOn = company_info["modifyOn"]
            phoneNumber = company_info["phoneNumber"]
            sumNumber = company_info["sumNumber"]
            # 请求地址
            url1 = 'http://api.toysbear.cc/api/CompanyByID'
            url2 = 'http://api.toysbear.cc/productapi/BearProduct/GetSupplierStoreProductPage'
            # 请求参数
            data1 = {
                "CompanyNumber":companyNumber
            }
            # 请求参数
            data2 = {
                "skipCount": "1",
                "SupplierNumber": companyNumber,
                "maxResultCount": "100"
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            print(request_data1.text)
            JSON1 = request_data1.json()
            request_data2 = Request().request("post", url=url2, json=data2, headers=header1)
            print(request_data2.text)
            JSON2 = request_data2.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON1": JSON1})
            write_extract_yaml({"JSON2": JSON2})
            isFollow = JSON1["result"]["item"]["isFollow"]
            if isFollow == True:
                print("已关注该店铺")
            else:
                # 请求地址
                url3 = 'http://api.toysbear.cc/api/UpdateManuFollow'
                # 请求参数
                data3 = {
                    "IsFollow":"true",
                    "SupplierNumber":companyNumber
                }
                # 请求头
                header3 = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                request_data3 = Request().request("post", url=url3, json=data3, headers=header3)
                print(request_data3.text)
                JSON3 = request_data3.json()
                write_extract_yaml({"JSON3": JSON3})
                code = JSON3["result"]["code"]
                msg = JSON3["result"]["msg"]
                if code == 200 and msg == "sucess":
                    print("成功关注店铺")
                else:
                    print(msg)
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新入驻厂商暂无数据")
            return JSON

    # 查看最新入驻厂商-店铺聊天
    def test_View_the_latest_settled_manufacturers_Shop_chat(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetCompanyByNewHallPage'
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
            companyLogo = company_info["companyLogo"]
            companyName = company_info["companyName"]
            companyNumber = company_info["companyNumber"]
            contactsMan = company_info["contactsMan"]
            createdBy = company_info["createdBy"]
            createdOn = company_info["createdOn"]
            deleteBy = company_info["deleteBy"]
            deleteTime = company_info["deleteTime"]
            id = company_info["id"]
            isDelete = company_info["isDelete"]
            modifyBy = company_info["modifyBy"]
            modifyOn = company_info["modifyOn"]
            phoneNumber = company_info["phoneNumber"]
            sumNumber = company_info["sumNumber"]
            # 请求地址
            url1 = 'http://api.toysbear.cc/api/CompanyByID'
            url2 = 'http://api.toysbear.cc/productapi/BearProduct/GetSupplierStoreProductPage'
            # 请求参数
            #companyNumber = "HS160826687393691"
            data1 = {
                "CompanyNumber": companyNumber
            }
            # 请求参数
            data2 = {
                "skipCount": "1",
                "SupplierNumber": companyNumber,
                "maxResultCount": "100"
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            print(request_data1.text)
            JSON1 = request_data1.json()
            request_data2 = Request().request("post", url=url2, json=data2, headers=header1)
            print(request_data2.text)
            JSON2 = request_data2.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON1": JSON1})
            write_extract_yaml({"JSON2": JSON2})
            chatUserId = JSON1["result"]["item"]["chatUserId"]
            msg = JSON2["result"]["msg"]
            if len(chatUserId) > 0:
                # 请求地址
                url3 = 'http://api.toysbear.cc/im/Message/PermissionValidator'
                # 请求参数
                data3 = {
                    "targetId":chatUserId,
                    "chatType":1
                }
                # 请求头
                header3 = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                request_data3 = Request().request("post", url=url3, json=data3, headers=header3)
                print(request_data3.text)
                JSON3 = request_data3.json()
                write_extract_yaml({"JSON3": JSON3})
                code = JSON3["result"]["code"]
                success = JSON3["success"]
                msg = JSON3["result"]["msg"]
                if code == 200 and success == True:
                    # 请求地址
                    url4 = 'http://api.toysbear.cc/im/Message/PermissionValidator'
                    content = "你好！"
                    # 请求参数
                    data4 = {
                        "targetId":chatUserId,
                        "rongCloudMessageType":"RC:TxtMsg",
                        "chatType":1,
                        "content":content
                    }
                    # 请求头
                    header4 = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data4 = Request().request("post", url=url4, json=data4, headers=header4)
                    print(request_data4.text)
                    JSON4 = request_data4.json()
                    write_extract_yaml({"JSON4": JSON4})
                    code = JSON4["result"]["code"]
                    success = JSON4["success"]
                    msg = JSON4["result"]["msg"]
                    if code == 200 and success == True:
                        print("发送成功，发送内容：{}".format(content))
                    else:
                        print(msg)
                else:
                    print(msg)
            else:
                print(msg)
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新入驻厂商暂无数据")
            return JSON




