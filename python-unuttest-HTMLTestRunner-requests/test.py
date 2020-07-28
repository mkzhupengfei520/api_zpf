# coding:utf-8
import requests

import unittest
#导入系统命令
import os
#导入时间模板
import time
import xlwt
from HTMLTestReportCN import HTMLTestRunner

class SenbabaTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://market.shixhmit.com/test/getSendTimeForSendGoodsByAdminShopId"

    def test_login(self):
        self.header = {'content-Type': 'application/x-www-form-urlencoded'}
        self.data = {"adminShopId": "383"}
        r = requests.post(self.base_url, self.data, self.header)
        print(r.status_code)
        code = r.status_code
        # 对比返回值
        self.assertEqual(code, 200, '调用成功')

    def test_login1(self):
        self.header = {'content-Type': 'application/x-www-form-urlencoded'}
        self.data = {"adminShopId": ""}
        r1 = requests.post(self.base_url, self.data, self.header)
        print(r1.status_code)
        self.assertEqual(r1.json()["code"], 200, '调用失败')

if __name__ == '__main__':

    #构造测试集
    suite = unittest.TestSuite() #构造测试集
    suite.addTest(SenbabaTest("test_login")) #加入测试集
    suite.addTest(SenbabaTest("test_login1"))#加入测试集
    # 执行测试

    date = time.strftime("%Y%m%d")  # 定义date为日期，time为时间
    time = time.strftime("%Y%m%d-%H%M%S")
    path = 'G:/test/'
    # 判断是否定义的路径目录存在，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    report_path = path + time + "report.html"  # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    report_title = u"测试报告"#注释以及print的信息含中文，则要用unicode形式输出，即引号前加u的形式
    desc = u'接口自动化测试报告详情：'
    with open(report_path, 'wb') as report: #打开报告 W是写入 B是传输二进制
        runner =HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    report.close()#关闭report

