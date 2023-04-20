from api.common.request_util import Request
from api.common.yaml_util import read_extract_yaml, clear_extract_yaml, write_extract_yaml
from api.testcase.common.atest_login_api import TestLogin


class Test3DProduct:
    #查询展厅3D产品
    def test_Already_settled_in_the_exhibition_room(self):
        # 获取token
        TestLogin().test_Vendor_Role_Login()
        Utoken = read_extract_yaml("JSON")["result"]["accessToken"]
        # 请求地址
        url = 'http://api.toysbear.cc/api/SearchBearProductPageV2'
        # 请求参数
        data = {
            "skipCount":"1",
            "HeatProductSearch":"2",
            "IsUpInset3D":"true",
            "maxResultCount":"30"
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