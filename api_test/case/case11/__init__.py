#coding:utf-8
import os
#读取配置文件的包
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(cur_path, "cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath)
#读取接口配置
def get_headers():

    return eval(str(conf.get('Api_path','headers')))

def get_url():
    return conf.get('Api_path','base_url')


def get_urlparams():
    return conf.get('Api_path','url_params')

if __name__ == '__main__':
    a = get_headers()
    print(type(a))
    b = str(a)
    print(b)