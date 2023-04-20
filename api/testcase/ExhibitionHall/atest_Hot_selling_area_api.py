import datetime
import random

from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, clear_extract_yaml, write_extract_yaml
from api.testcase.common.atest_login_api import TestLogin


class TestHotSellingArea:
    #展厅首页-展厅热销产品
    def test_Hot_selling_products_in_the_exhibition_hall(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetSellWellProductInfo'
        # 请求参数
        data = {
            "SearchType":"Head",
            "hallNumber":companyNumber,
            "SkipCount":1,
            "MaxResultCount":100
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

    #查询展厅热销产品
    def test_Query_the_hot_products_in_the_exhibition_hall(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        now_date = datetime.datetime.now()
        print(now_date.strftime("%Y-%m-%d %H:%M:%S"))
        month = now_date.month
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetSellWellProductInfo'
        # 请求参数
        data = {
            "SearchType":"Center",
            "skipCount":"1",
            "hallNumber":companyNumber,
            "maxResultCount":"30",
            "Month":month
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

    #关键词查询展厅热销产品
    def test_Query_the_hot_products_in_the_exhibition_hall_with_keywork(self):
        #获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        now_date = datetime.datetime.now()
        print(now_date.strftime("%Y-%m-%d %H:%M:%S"))
        month = now_date.month
        keyword = '娃娃'
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetSellWellProductInfo'
        # 请求参数
        data = {
            "SearchType": "Center",
            "skipCount": "1",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "Month": month,
            "keyWord": keyword
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

    # 查询其他月份的展厅热销产品
    def test_Query_the_hot_selling_products_in_the_exhibition_hall_in_other_months(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        now_date = datetime.datetime.now()
        print(now_date.strftime("%Y-%m-%d %H:%M:%S"))
        now_month = now_date.month
        month = random.randint(1,now_month)
        print(month)
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetSellWellProductInfo'
        # 请求参数
        data = {
            "SearchType": "Center",
            "skipCount": "1",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "Month": month
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

    # 收藏展厅热销产品
    def test_Collect_the_hot_selling_products_in_the_exhibition_hall(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        now_date = datetime.datetime.now()
        print(now_date.strftime("%Y-%m-%d %H:%M:%S"))
        month = now_date.month
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetSellWellProductInfo'
        # 请求参数
        data = {
            "SearchType": "Center",
            "skipCount": "1",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "Month": month
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
        product_info_list = read_extract_yaml("JSON")["result"]["item"]["items"]
        if len(product_info_list) > 0 :
            product_info = random.choice(product_info_list)
            productNumber = product_info["productNumber"]
            # 请求地址
            url2 = 'http://api.toysbear.cc/api/CreateProductCollection'
            # 请求参数
            data = {
                "ProductNumber": productNumber
            }
            # 请求头
            header = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data = Request().request("post", url=url2, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            return JSON
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("热销产品暂无数据")
            return JSON

    # 获取展厅热销广告
    def test_Get_hot_sale_product_ads(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetAdvertisementListV2'
        # 请求参数
        data = {
            "adPosition": "43",
            "adType": "0"
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

    # 热销产品-添加广告访问记录（管理员的广告分析）
    def test_hot_sale_product_add_advertisement_visit_record(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetAdvertisementListV2'
        # 请求参数
        data = {
            "adPosition": "43",
            "adType": "0"
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
        advertisementList = read_extract_yaml("JSON")["result"]["item"]["advertisementList"]
        if len(advertisementList) > 0:
            for i in advertisementList:
                id = i["id"]
                title = i["adTitle"]
                content = i["content"]
                # 请求地址
                url1 = 'http://api.toysbear.cc/api/CreateAdVisitRecord'
                CheckType = random.choice([0, 1])  # 访问类型，0-曝光展现/1-点击跳转
                # 请求参数
                data1 = {
                    "AdIdList": [id],
                    "CheckType": CheckType
                }
                # 请求头
                header = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                if CheckType == 0:
                    print("浏览了热销产品广告，广告名为{}".format(title))
                    # 厂商增加产品记录
                    # 请求地址
                    url2 = 'http://api.toysbear.cc/api/CreateNoticeAdsProductRecord'
                    # 请求参数
                    data2 = {
                        "adid": id,
                        "BusinessType": "3",  # 来源0-全部1-平台数据2-分享站点3-广告分析4-玩具圈5-玩具圈推广
                        "SupplierNumber": content,
                        "OperationType": "13"
                        # 类型0-全部1-文搜浏览2-图搜浏览3-选中4-加购5-收藏6-店铺7-平台择样8-展厅择样9-取资料10-全网推荐11-复制12-点击13-曝光
                    }
                    # 请求头
                    header = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data2 = Request().request("post", url=url2, json=data2, headers=header)
                    JSON = request_data2.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON": JSON})
                    print("厂商增加广告分析-浏览记录")
                else:
                    print("点击了热销产品广告，广告名为{}".format(title))
                    # 请求地址
                    url2 = 'http://api.toysbear.cc/api/CreateNoticeAdsProductRecord'
                    # 请求参数
                    data2 = {
                        "adid": id,
                        "BusinessType": "3",  # 来源0-全部1-平台数据2-分享站点3-广告分析4-玩具圈5-玩具圈推广
                        "SupplierNumber": content,
                        "OperationType": "12"
                        # 类型0-全部1-文搜浏览2-图搜浏览3-选中4-加购5-收藏6-店铺7-平台择样8-展厅择样9-取资料10-全网推荐11-复制12-点击13-曝光
                    }
                    # 请求头
                    header = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data2 = Request().request("post", url=url2, json=data2, headers=header)
                    JSON = request_data2.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON": JSON})
                    print("厂商增加广告分析-点击记录")
                request_data1 = Request().request("post", url=url1, json=data1, headers=header)
                print(request_data1.text)
                JSON = request_data1.json()
                clear_extract_yaml()
                write_extract_yaml({"JSON": JSON})
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("热销产品暂无广告数据")
            return JSON



    # 通过热销产品联系厂商
    def test_Contact_manufacturers_for_Hot_sale_products(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        now_date = datetime.datetime.now()
        print(now_date.strftime("%Y-%m-%d %H:%M:%S"))
        month = now_date.month
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetSellWellProductInfo'
        # 请求参数
        data = {
            "SearchType": "Center",
            "skipCount": "1",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "Month": month
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
        product_info_list = read_extract_yaml("JSON")["result"]["item"]["items"]
        if len(product_info_list) > 0:
            product_info = random.choice(product_info_list)
            supplierChatUserId = product_info["supplierChatUserId"]
            # 请求地址
            url1 = 'http://api.toysbear.cc/im/Message/PermissionValidator'  # 验证是否有发消息的权限
            # 请求参数
            data1 = {
                "targetId": supplierChatUserId,
                "chatType": 1  # 聊天类型(1=单聊,2=群聊)
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            code1 = request_data1.json()["result"]["code"]
            if code1 == 200:
                # 请求地址
                url2 = 'http://api.toysbear.cc/im/Message/SendIdentityMessage'
                # 从产品进入聊天发送一条代表身份的系统消息
                supplierName = product_info["supplierName"]
                # 请求参数
                data2 = {
                    "targetCompanyName": supplierName,
                    "targetChatUserId": supplierChatUserId
                }
                # 请求头
                header2 = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                request_data2 = Request().request("post", url=url2, json=data2, headers=header2)
                code2 = request_data2.json()["result"]["code"]
                if code2 == 200:
                    # 请求地址
                    url3 = 'http://api.toysbear.cc/im/Message/RecordMessageHis'
                    # 记录聊天历史
                    # 请求参数
                    data3 = {
                        "targetId": supplierChatUserId,
                        "chatType": 1,
                        "rongCloudMessageType": "xzx:ProductMessage"
                    }
                    # 请求头
                    header3 = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data3 = Request().request("post", url=url3, json=data3, headers=header3)
                    JSON = request_data3.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON": JSON})
                    return JSON
                else:
                    request_data2 = Request().request("post", url=url2, json=data2, headers=header2)
                    JSON = request_data2.json()
                    msg = JSON["result"]["msg"]
                    clear_extract_yaml()
                    write_extract_yaml({"JSON": JSON})
                    print(msg)
                    return JSON
            else:
                request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
                msg = request_data1.json()["result"]["msg"]
                JSON = request_data1.json()
                clear_extract_yaml()
                write_extract_yaml({"JSON": JSON})
                print(msg)
                return JSON
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("热销产品暂无数据")




