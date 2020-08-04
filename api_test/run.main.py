#coding:utf-8
from api_test.common import function
import os,requests
import configparser,json
from api_test.config import readconfig
from api_test.db_fixture import mysql_db
import pymysql
#读取基础配置
#获得你刚才所引用的模块 所在的绝对路径，__file__为内置属性。
apiconfigpath = os.path.dirname(os.path.realpath(__file__))
#连接两个或更多的路径名，文件名是config.ini
configpath = os.path.join(apiconfigpath,"config.ini")
#获取配置节section成为字典
conf = configparser.ConfigParser()
#读取配置文件config.ini
conf.read(configpath)

#测试用例执行路径获取，测试用例名获取
casePath = conf.get('Api', 'TestApiPath')
caseName = conf.get('Api', 'TestCaseName')
#邮箱获取，邮件发送获取
sendmail = conf.get('Mail', 'sendmail')
tablename = conf.get('mysql','table_name')
cur_path = os.path.dirname(os.path.realpath(__file__))
if __name__ == '__main__':
    Testlist = function.Test_init()  #实例化类对象，然后用类方法
    all_case = Testlist.add_case(cur_path=cur_path,caseName=casePath,rule=caseName)
    Testlist.run_case(cur_path=cur_path,all_case=all_case)
    print(all_case)
    print(casePath)

    sender = readconfig.get_mailpath(cur_path=cur_path) #获取发放邮件使用的邮箱配置
    #调用数据库做数据回滚
    #sql = mysql_db.DB()  #实例化类，然后用类方法

    #sqlde = sql.delete(table_name=tablename)



    if sendmail == 'True':
        print(u'测试完成，准备发送测试报告邮件')
        report_path = os.path.join(cur_path, 'report')
        report_file = Testlist.get_report_file(report_path)
        print(report_file)
        Testlist.send_mail(sender['sender'], sender['psw'], sender['receiver'], sender['smtp_server'], report_file, sender['port'])
    else:
        print(u'测试完成，不发送测试报告邮件')
