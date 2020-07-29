#coding:utf-8
#数据驱动模块（可以将测试中的变量进行参数化）
import ddt
#用它来做单元测试，它里面封装好了一些校验返回的结果方法和一些用例执行前的初始化操作。
import unittest,json
#从common包中xlrdt这个类中导入Api_Data_read这个方法
from api_test.common.Trequest import Trequest
from api_test.common.xlrdt import Api_Data_read
#自己封装一个断言库
import assertE
#导入日志模板
from api_test.common.logger import Log
#导入读取配置文件的模板
from api_test.case.case4.__init__ import *
@ddt.ddt
class mytest(unittest.TestCase):  #继承unittest.TestCase这个类
    '''第三个接口测试'''
    log = Log()

    def __init__(self,methodName='runTest'):
        super(mytest, self).__init__(methodName)
        self.url = get_url()
        self.url_params = get_urlparams()
        self.headers = get_headers()
    def tearDown(self):

        print(u'单条用例执行完成')

    @classmethod
    def tearDownClass(self):    #需要配合@classmethod装饰器一起使用。（在所有用例前后总共各执行一次。）
        print(u'第三个接口测试完成')

    @classmethod
    def setUpClass(self):        #需要配合@classmethod装饰器一起使用。（在所有用例前后总共各执行一次。）
        print(u'接口测试第三个接口开始调用')
    @ddt.data (*Api_Data_read(r'C:\Users\EDZ\Desktop\ziyuanbao\untitled2\api_test\case\case4\Api_data4.xlsx','Api_data'))
    @ddt.unpack  #如果有unpack，那么[a,b]被分解开，按照用例中的两个参数传递
    def test_api_run(self,value,tovalue):
        '''测试用例'''
        # data 参数
        self.value = value   #参数值
        self.tovalue = int(float(tovalue)) #预期结果
        self.val = assertE.Tassert()

        self.log.info(u'------执行测试用例------')
        self.ret = Trequest(base_url=self.url, url_params=self.url_params, headers=self.headers)
        del value['case_name']
        self.log.info(u'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa：{}'.format(self.value))
        a = self.value
        b = {}
        for (key, value) in a.items(): #将key，value值同时遍历
            b[key] = int(float(value))
        #self.log.info(u'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa：{}'.format(type(b)))
        self.log.info(u'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa：{}'.format(b))
        self.response = self.ret.post(data=json.dumps(b))
        self.tcode = int(float(self.ret.get_code()))#实际结果
        self.log.info(u'请求结果：{}'.format(self.response.text))
        self.log.info(u'------测试用例执行完成，f开始对比结果------')
        self.log.info(u'测试结果比对')
        self.log.info(u'预期结果:{0},实际结果:{1}'.format(int(float(self.tovalue)),self.tcode))
        self.log.info(u'打印参数：{}'.format(json.dumps(b)))
        self.log.info(u'预期message:{0},实际message:{1}'.format('ok',self.ret.get_message()))
        self.log.info(u'预期message code:{0},实际message code:{1}'.format('0',self.ret.get_response_message()))
        try:
            self.val.assert_value_valid(str(self.tcode), str(self.tovalue))
        except AssertionError as f:
            self.log.info(u'本条用例执行失败，详细内容请查阅数据对比')
            raise f


    def runTest(self):
        pass