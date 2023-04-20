import random

from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, write_extract_yaml, clear_extract_yaml
from api.testcase.common.atest_login_api import TestLogin


class TestNewProductArea:
    #查询展厅新品区
    def test_Query_the_new_product_area_of_the_exhibition_hall(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        #请求地址
        url = 'http://api.toysbear.cc/api/GetProductsByTypePageV2'
        #请求参数
        data = {
            "skipCount": "1",
            "typeId": "2",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "parentCode": "all"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post",url=url,json=data,headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        return JSON

    #展厅最新产品关键词查询
    def test_Search_for_the_latest_products_in_the_exhibition_hall_with_keywork(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetProductsByTypePageV2'
        # 请求参数
        data = {
            "skipCount":"1",
            "typeId":"2",
            "hallNumber":companyNumber,
            "maxResultCount":"30",
            "parentCode":"all",
            "keyWord":"娃娃"
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

    #展厅最新产品排序操作
    def test_Sorting_the_latest_products_in_the_exhibition_hall(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        SortOrder = random.randint(1,3)#排序方式 1-价格排序,2-时间排序,3-热度排序
        SortType = random.randint(1,2)#排序类型 1-降序 2-升序
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetProductsByTypePageV2'
        # 请求参数
        data = {
            "SortOrder":SortOrder,
            "skipCount":"1",
            "typeId":"2",
            "hallNumber":companyNumber,
            "maxResultCount":"30",
            "parentCode":"all",
            "SortType":SortType
        }
        if SortOrder == 1 and SortType == 1:
            print("价格降序")
        elif SortOrder == 1 and SortType == 2:
            print("价格升序")
        elif SortOrder == 2 and SortType == 1:
            print("时间降序")
        elif SortOrder == 2 and SortType == 2:
            print("时间升序")
        elif SortOrder == 3 and SortType == 1:
            print("热度降序")
        else:
            print("热度升序")
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

    # 收藏展厅最新产品
    def test_Collect_the_latest_products_in_the_exhibition_hall(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url1 = 'http://api.toysbear.cc/api/GetProductsByTypePageV2'
        # 请求参数
        data = {
            "skipCount": "1",
            "typeId": "2",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "parentCode": "all"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url1, json=data, headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        product_info_list = read_extract_yaml("JSON")["result"]["item"]["items"]
        if len(product_info_list) > 0:
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
            request_data = Request().request("post", url=url1, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新产品暂无数据")
            return JSON

    # 最新产品添加产品浏览足迹
    def test_the_latest_products_Add_Product_Footprint(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url1 = 'http://api.toysbear.cc/api/GetProductsByTypePageV2'
        # 请求参数
        data = {
            "skipCount": "1",
            "typeId": "2",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "parentCode": "all"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url1, json=data, headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        product_info_list = read_extract_yaml("JSON")["result"]["item"]["items"]
        if len(product_info_list) > 0:
            product_info = random.choice(product_info_list)
            productNumber = product_info["productNumber"]
            # 请求地址
            url2 = 'http://api.toysbear.cc/api/CreateProductRecord'
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
            request_data = Request().request("post", url=url1, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新产品暂无数据")
            return JSON

    #获取最新产品广告
    def test_Get_the_latest_product_ads(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetAdvertisementListV2'
        # 请求参数
        data = {
            "adPosition":"40",
            "adType":"0"
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

    #最新产品-添加广告访问记录（管理员的广告分析）
    def test_latest_product_add_advertisement_visit_record(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetAdvertisementListV2'
        # 请求参数
        data = {
            "adPosition": "40",
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
                CheckType = random.choice([0,1])#访问类型，0-曝光展现/1-点击跳转
                # 请求参数
                data1 = {
                    "AdIdList":[id],
                    "CheckType":CheckType
                }
                # 请求头
                header = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                if CheckType == 0:
                    print("浏览了3D广告，广告名为{}".format(title))
                    #厂商增加产品记录
                    # 请求地址
                    url2 = 'http://api.toysbear.cc/api/CreateNoticeAdsProductRecord'
                    # 请求参数
                    data2 = {
                        "adid":id,
                        "BusinessType":"3",#来源0-全部1-平台数据2-分享站点3-广告分析4-玩具圈5-玩具圈推广
                        "SupplierNumber":content,
                        "OperationType":"13"#类型0-全部1-文搜浏览2-图搜浏览3-选中4-加购5-收藏6-店铺7-平台择样8-展厅择样9-取资料10-全网推荐11-复制12-点击13-曝光
                    }
                    # 请求头
                    header = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data2 = Request().request("post", url=url2, json=data2, headers=header)
                    JSON = request_data2.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON":JSON})
                    print("厂商增加广告分析-浏览记录")
                else:
                    print("点击了3D广告，广告名为{}".format(title))
                    # 请求地址
                    url2 = 'http://api.toysbear.cc/api/CreateNoticeAdsProductRecord'
                    # 请求参数
                    data2 = {
                        "adid": id,
                        "BusinessType": "3",#来源0-全部1-平台数据2-分享站点3-广告分析4-玩具圈5-玩具圈推广
                        "SupplierNumber": content,
                        "OperationType": "12"#类型0-全部1-文搜浏览2-图搜浏览3-选中4-加购5-收藏6-店铺7-平台择样8-展厅择样9-取资料10-全网推荐11-复制12-点击13-曝光
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
                write_extract_yaml({"JSON":JSON})
                return JSON
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新产品暂无广告数据")
            return JSON


    #展厅24小时新品查询
    def test_24hour_new_product_query_in_the_exhibition_hall(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/productapi/products/GetProductsByNewDaysPage'
        # 请求参数
        data = {
             "skipCount": "1",
             "hallNumber": companyNumber,
             "maxResultCount": "30"
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

    # 展厅24小时新品关键词查询
    def test_24hour_new_product_query_in_the_exhibition_hall_with_keywork(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/productapi/products/GetProductsByNewDaysPage'
        # 请求参数
        data = {
            "skipCount":"1",
            "hallNumber":companyNumber,
            "maxResultCount":"30",
            "keyWord":"娃娃"
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

    # 展厅24小时新品排序操作
    def test_24_hour_sorting_of_new_products_in_the_exhibition_hall(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        SortOrder = random.randint(1, 3)  # 排序方式 1-价格排序,2-时间排序,3-热度排序
        SortType = random.randint(1, 2)  # 排序类型 1-降序 2-升序
        # 请求地址
        url = 'http://api.toysbear.cc/productapi/products/GetProductsByNewDaysPage'
        # 请求参数
        data = {
            "SortOrder":SortOrder,
            "skipCount":"1",
            "hallNumber":companyNumber,
            "maxResultCount":"30",
            "SortType":SortType
        }
        if SortOrder == 1 and SortType == 1:
            print("价格降序")
        elif SortOrder == 1 and SortType == 2:
            print("价格升序")
        elif SortOrder == 2 and SortType == 1:
            print("时间降序")
        elif SortOrder == 2 and SortType == 2:
            print("时间升序")
        elif SortOrder == 3 and SortType == 1:
            print("热度降序")
        else:
            print("热度升序")
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

    #收藏展厅24小时新品
    def test_Collect_24_hour_new_products_in_the_exhibition_hall(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url1 = 'http://api.toysbear.cc/productapi/products/GetProductsByNewDaysPage'
        # 请求参数
        data = {
            "skipCount": "1",
            "typeId": "2",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "parentCode": "all"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url1, json=data, headers=header)
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
            request_data = Request().request("post", url=url1, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("24小时新品暂无数据")
            return JSON

    #24小时新品添加产品浏览足迹
    def test_24_hour_new_products_Add_Product_Footprint(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url1 = 'http://api.toysbear.cc/productapi/products/GetProductsByNewDaysPage'
        # 请求参数
        data = {
            "skipCount": "1",
             "hallNumber": companyNumber,
             "maxResultCount": "30"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Utoken": Utoken
        }
        request_data = Request().request("post", url=url1, json=data, headers=header)
        print(request_data.text)
        JSON = request_data.json()
        clear_extract_yaml()
        write_extract_yaml({"JSON": JSON})
        product_info_list = read_extract_yaml("JSON")["result"]["item"]["items"]
        if len(product_info_list) > 0 :
            product_info = random.choice(product_info_list)
            productNumber = product_info["productNumber"]
            # 请求地址
            url2 = 'http://api.toysbear.cc/api/CreateProductRecord'
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
            request_data = Request().request("post", url=url1, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("24小时新品暂无数据")
            return JSON

    #获取24小时新品广告
    def test_Get_24_hour_new_product_ads(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetAdvertisementListV2'
        # 请求参数
        data = {
            "adPosition":"58",
            "adType":"0"
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

    #24小时新品-添加广告访问记录（管理员的广告分析）
    def test_24_huor_new_product_add_advertisement_visit_record(self):
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetAdvertisementListV2'
        # 请求参数
        data = {
            "adPosition": "58",
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
                CheckType = random.choice([0,1])#访问类型，0-曝光展现/1-点击跳转
                # 请求参数
                data1 = {
                    "AdIdList":[id],
                    "CheckType":CheckType
                }
                # 请求头
                header = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                if CheckType == 0:
                    print("浏览了3D广告，广告名为{}".format(title))
                    #厂商增加产品记录
                    # 请求地址
                    url2 = 'http://api.toysbear.cc/api/CreateNoticeAdsProductRecord'
                    # 请求参数
                    data2 = {
                        "adid":id,
                        "BusinessType":"3",#来源0-全部1-平台数据2-分享站点3-广告分析4-玩具圈5-玩具圈推广
                        "SupplierNumber":content,
                        "OperationType":"13"#类型0-全部1-文搜浏览2-图搜浏览3-选中4-加购5-收藏6-店铺7-平台择样8-展厅择样9-取资料10-全网推荐11-复制12-点击13-曝光
                    }
                    # 请求头
                    header = {
                        "Content-Type": "application/json; charset=UTF-8",
                        "Utoken": Utoken
                    }
                    request_data2 = Request().request("post", url=url2, json=data2, headers=header)
                    JSON = request_data2.json()
                    clear_extract_yaml()
                    write_extract_yaml({"JSON":JSON})
                    print("厂商增加广告分析-浏览记录")
                else:
                    print("点击了3D广告，广告名为{}".format(title))
                    # 请求地址
                    url2 = 'http://api.toysbear.cc/api/CreateNoticeAdsProductRecord'
                    # 请求参数
                    data2 = {
                        "adid": id,
                        "BusinessType": "3",#来源0-全部1-平台数据2-分享站点3-广告分析4-玩具圈5-玩具圈推广
                        "SupplierNumber": content,
                        "OperationType": "12"#类型0-全部1-文搜浏览2-图搜浏览3-选中4-加购5-收藏6-店铺7-平台择样8-展厅择样9-取资料10-全网推荐11-复制12-点击13-曝光
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
                write_extract_yaml({"JSON":JSON})
        else:
            request_data = Request().request("post", url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("24小时新品暂无广告数据")
            return JSON

    #通过最新产品联系厂商
    def test_Contact_manufacturers_for_the_latest_products(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetProductsByTypePageV2'
        # 请求参数
        data = {
            "skipCount": "1",
            "typeId": "2",
            "hallNumber": companyNumber,
            "maxResultCount": "30",
            "parentCode": "all"
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
            #请求地址
            url1 = 'http://api.toysbear.cc/im/Message/PermissionValidator'#验证是否有发消息的权限
            # 请求参数
            data1 = {
                "targetId":supplierChatUserId,
                "chatType":1#聊天类型(1=单聊,2=群聊)
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            code1 = request_data1.json()["result"]["code"]
            if code1 == 200:
                #请求地址
                url2 = 'http://api.toysbear.cc/im/Message/SendIdentityMessage'
                #从产品进入聊天发送一条代表身份的系统消息
                supplierName = product_info["supplierName"]
                #请求参数
                data2 = {
                    "targetCompanyName":supplierName,
                    "targetChatUserId":supplierChatUserId
                }
                # 请求头
                header2 = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                request_data2 = Request().request("post", url=url2, json=data2,headers=header2)
                code2 = request_data2.json()["result"]["code"]
                if code2 == 200:
                    # 请求地址
                    url3 = 'http://api.toysbear.cc/im/Message/RecordMessageHis'
                    #记录聊天历史
                    # 请求参数
                    data3 = {
                        "targetId":supplierChatUserId,
                        "chatType":1,
                        "rongCloudMessageType":"xzx:ProductMessage"
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
                    write_extract_yaml({"JSON":JSON})
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
            request_data = Request().request("post",url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("最新产品暂无数据")

    #通过24小时新品联系厂商
    def test_Contact_manufacturers_for_24_hour_new_products(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/productapi/products/GetProductsByNewDaysPage'
        # 请求参数
        data = {
            "skipCount": "1",
            "hallNumber": companyNumber,
            "maxResultCount": "30"
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
            #请求地址
            url1 = 'http://api.toysbear.cc/im/Message/PermissionValidator'#验证是否有发消息的权限
            # 请求参数
            data1 = {
                "targetId":supplierChatUserId,
                "chatType":1#聊天类型(1=单聊,2=群聊)
            }
            # 请求头
            header1 = {
                "Content-Type": "application/json; charset=UTF-8",
                "Utoken": Utoken
            }
            request_data1 = Request().request("post", url=url1, json=data1, headers=header1)
            code1 = request_data1.json()["result"]["code"]
            if code1 == 200:
                #请求地址
                url2 = 'http://api.toysbear.cc/im/Message/SendIdentityMessage'
                #从产品进入聊天发送一条代表身份的系统消息
                supplierName = product_info["supplierName"]
                #请求参数
                data2 = {
                    "targetCompanyName":supplierName,
                    "targetChatUserId":supplierChatUserId
                }
                # 请求头
                header2 = {
                    "Content-Type": "application/json; charset=UTF-8",
                    "Utoken": Utoken
                }
                request_data2 = Request().request("post", url=url2, json=data2,headers=header2)
                code2 = request_data2.json()["result"]["code"]
                if code2 == 200:
                    # 请求地址
                    url3 = 'http://api.toysbear.cc/im/Message/RecordMessageHis'
                    #记录聊天历史
                    # 请求参数
                    data3 = {
                        "targetId":supplierChatUserId,
                        "chatType":1,
                        "rongCloudMessageType":"xzx:ProductMessage"
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
                    write_extract_yaml({"JSON":JSON})
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
            request_data = Request().request("post",url=url, json=data, headers=header)
            print(request_data.text)
            JSON = request_data.json()
            clear_extract_yaml()
            write_extract_yaml({"JSON": JSON})
            print("24小时新品暂无数据")



