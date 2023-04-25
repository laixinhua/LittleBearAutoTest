import pytest

from common.yaml_util import clear_extract_yaml

@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    clear_extract_yaml()
    print("清除extract.yaml文件的内容")