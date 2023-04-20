import pytest

from api.common.yaml_util import clear_extract_yaml,gettoken,writetoken
@pytest.fixture(scope="session",autouse=True)
def get_token():
    gettoken()
    print("获取临时token")
@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    clear_extract_yaml()
    print("清除extract.yaml文件的内容")