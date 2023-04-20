import os

#获取config.py当前文件路径
curren_path = os.path.abspath(__file__)
#获取配置文件目录的路径
config_dir = os.path.dirname(curren_path)
#config包的路径
cf_dir = os.path.dirname(config_dir)
#拼接出data的路径
data_dir = os.path.join(cf_dir,'data')
#拼接出测试用例extract.yaml的路径
extract_yaml_dir = os.path.join(data_dir,'extract.yaml')