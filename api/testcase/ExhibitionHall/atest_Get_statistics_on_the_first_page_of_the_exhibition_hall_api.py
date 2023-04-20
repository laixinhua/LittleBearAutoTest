from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, clear_extract_yaml, write_extract_yaml
from api.testcase.common.atest_login_api import TestLogin


class TestGetStatisticsOnTheFirstPageOfTheExhibitionHall:
    #获取展厅首页统计值
    def test_Get_statistics_on_the_first_page_of_the_exhibition_hall(self):
        # 获取token
        TestLogin().test_Hall_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        commparnyList = read_extract_yaml("JSON")["result"]["commparnyList"]
        companyNumber = commparnyList[0]["companyNumber"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetHallStatisticsCountV2'
        # 请求参数
        data = {
            "hallNumber": companyNumber
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
        exposureTotalCount = JSON["result"]["item"]["exposureTotalCount"]
        productTotalCount = JSON["result"]["item"]["productTotalCount"]
        firmTotalCount = JSON["result"]["item"]["firmTotalCount"]
        clientTotalCount = JSON["result"]["item"]["clientTotalCount"]
        print("曝光总数为：{}\n".format(exposureTotalCount),"产品总数为：{}\n".format(productTotalCount),"厂商总数为：{}\n".format(firmTotalCount),"公司总数为：{}\n".format(clientTotalCount))
        return JSON
