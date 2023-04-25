import os
import yaml
from config import config

#读取extract.yaml文件
def read_extract_yaml(key):
    with open(config.extract_yaml_dir,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

#写入extract.yaml文件
def write_extract_yaml(data):
    with open(config.extract_yaml_dir,mode='a',encoding='utf-8') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)

#清除extract.yaml文件
def clear_extract_yaml():
    with open(config.extract_yaml_dir,mode='w',encoding='utf-8') as f:
        f.truncate()