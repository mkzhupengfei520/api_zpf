#coding:utf-8
import os
import configparser
def get_mailpath(cur_path):
    configpath = os.path.join(cur_path,"config.ini")
    conf = configparser.ConfigParser()
    conf.read(configpath)
    #邮箱配置信息
    smtp_server = conf.get("Mail","smtp_server")
    sender = conf.get('Mail','sender')
    psw = conf.get('Mail','psw')
    receiver = conf.get('Mail','receiver')
    port = conf.get('Mail',"port")

    return {'smtp_server':smtp_server,'sender':sender,
            'psw':psw,'receiver':receiver,'port':port}
