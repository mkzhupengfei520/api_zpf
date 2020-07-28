import os
import sys
import unittest
import requests
import time
import HTMLTestRunner

sys.path.append('G:test/testbaidu.py')
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))


class MyTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def test_case1(self):
        self.r = requests.get("https://www.baidu.com")
        self.r.status_code = 200
        self.r.encoding = 'utf-8'
        self.r.text

        # r.json()
        assert self.r.status_code == 200
        assert "百度一下" in self.r.text
        print("通过")

    def test_case2(self):
        assert 11 == 200

    def tearDown(self):
        #  self.driver.quit()
        print("tearDown")


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()  # 构造测试集
    suite.addTest(MyTest("test_case1"))  # 加入测试用例
    suite.addTest(MyTest("test_case2"))

    # 执行测试
    date = time.strftime("%Y%m%d")  # 定义date为日期，time为时间
    time = time.strftime("%Y%m%d-%H%M%S")
    path = "./report/api/"
    # 判断是否定义的路径目录存在，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    report_path = path + time + "report.html"  # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本

    report_title = u"测试报告"
    desc = u'接口自动化测试报告详情：'

    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    # 关闭report，脚本结束
    report.close()

