from api.common.request_util import Request
from api.common.yaml_util import write_extract_yaml
import pytest
class TestGetToken:
    # 获取token
    def test_get_token(self):
        # 请求地址
        url = 'http://api.toysbear.cc/api/GetToken'
        # 请求参数
        data = {
            "PlatForm": "android",
            "CompanyNum": "LittleBearWeb"
        }
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8"
        }
        # 调用request并且传参进去
        request_data = Request().request("post", url, json=data, headers=header)
        # 打印响应结果
        print(request_data.json())
        print(request_data.json()["result"]["item"])
        write_extract_yaml({"token": request_data.json()["result"]["item"]})
if __name__ == '__main__':
    pytest.main(['-s'])