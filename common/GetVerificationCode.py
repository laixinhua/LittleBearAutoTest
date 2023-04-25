import datetime
import time
import pytest
import re

from common.request_util import Request
from common.yaml_util import read_extract_yaml, write_extract_yaml


class TestGetVerificationCode:
    def test_LoginAdministrator(self):
        global VerificationCode
        # 请求地址
        url = 'https://api.toysbear.cc/api/getAdminSMSList'
        # 请求参数
        data = {
            "pageIndex":1,
            "pageSize":10,
            "startTime":datetime.datetime.now().strftime("%Y-%m-%d")+"T00:00:00",
            "endTime":datetime.datetime.now().strftime("%Y-%m-%d")+"T23:59:59",
            "operatType":1
        }
        print(data)
        # 请求头
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "Encryption": "123456",
            "Utoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJMaXR0bGVCZWFyIiwianRpIjoiNDIyNDg2ZjYtMzk5Zi00ZTI3LTliNmYtMmJiM2JkNDE2N2E2IiwiaWF0IjoxNjgyMzI1ODMyLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiMTM0MjMwNzY2NDgiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zeXN0ZW0iOiJQQyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjFkYTc3NjNhLTBmYWEtNDNkNi05MTE5LTgzNTAzYzA1MzMzMCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NwbiI6ImFkM2ZmY2YzLWI5NmUtNGZiNC04NDhjLTU2NTY3YzJiYzg1NiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2Fub255bW91cyI6IkhTMDAyMTM3OCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFkbWluIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiIiwiSXNNYXN0ZXIiOiJGYWxzZSIsIkNoYXRVc2VySWQiOiIxZGE3NzYzYS0wZmFhLTQzZDYtOTExOS04MzUwM2MwNTMzMzAiLCJDaGF0VXNlclRva2VuIjoibktydVFMc1pkUDdkYXFuVTZnRFI5L3Z2QW54YTJpUEdUNEZnTmthaE5pM1hJQjJFSUZxZVBoR1A5R2tLTzhIUkhNaTM0Y3hhcm5IejJGNDJYdk9Bdnc9PUBwbTV5LmNuLnJvbmduYXYuY29tO3BtNXkuY24ucm9uZ2NmZy5jb20iLCJMb2dpblR5cGUiOiIiLCJuYmYiOjE2ODIzMjU4MzIsImV4cCI6MTY4MjQxMjIzMiwiaXNzIjoiTGl0dGxlQmVhciIsImF1ZCI6IkxpdHRsZUJlYXIifQ.0Qk6CUIEdtjxbY97Olvn33Nl4ZnD7xAYRMwXHXUPLbM"
        }
        # 调用request并且传参进去
        request_data = Request().request("post", url, json=data, headers=header)
        time.sleep(2)
        # 打印响应结果
        print(request_data.json())
        # print(request_data.json()["result"]["accessToken"])
        #write_extract_yaml({"accessToken": request_data.json()["result"]["accessToken"]})
        for i in range(len(request_data.json()["result"]["item"]["items"])):
            if "13642562621" in  request_data.json()["result"]["item"]["items"][i]["phoneNumber"]:
                #print(request_data.json()["result"]["item"]["items"][i]["phoneNumber"])
                content = request_data.json()["result"]["item"]["items"][i]["content"]
                #print(content)
                vc = r'您的验证码是：\d+'
                verificationcodecontent = re.findall(vc,content)
                #print(verificationcodecontent)
                fvc = r'\d+'
                verificationcode = re.findall(fvc,str(verificationcodecontent))
                #print(verificationcode[0])
                VerificationCode = verificationcode[0]
                print(VerificationCode)
                return VerificationCode

            else:
                print("号码不存在")

        #print(dict(a))
        # if "phoneNumber" in request_data.json()["result"]["item"]["items"][0]:
        #     print("号码存在")
        # else:
        #     print("号码不存在")
if __name__ == '__main__':
    pytest.main()

