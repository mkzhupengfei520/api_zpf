# coding:utf-8
import config.settings
import requests
#choice() 方法返回一个列表，元组或字符串的随机项
from random import choice
from api_test.common.logger import Log
class Trequest(object):
    log = Log()

    # 根据Testcase传入的api地址和接口路径初始化
    def __init__(self, base_url='', url_params=None, headers=''):
        if not url_params:
            url_params = []
        self.url_params = url_params
        self.response = None
        self.base_url = base_url
        self.headers = headers

    # self.headers['Connection'] = 'close'

    def api_url(self):
        if not self.base_url:
            raise RuntimeError("url has been set")
        return self.get_url()

    # url content
    def get_url(self):
        return "{0}{1}".format(self.base_url, self.url_params)

    def post(self, data=None):
        if not data:
            data = {}
            base_params = self.build_base_params()
            custom_params = self.build_custom_params()
            data.update(base_params)
            data.update(custom_params)
        self.log.info(u'本次请求接口详细路径:%s' % self.api_url())
        self.response = requests.post(url=self.api_url(), data=data, headers=self.headers)

        return self.response

    def get(self, data=None):
        if not data:
            data = {}
            base_params = self.build_base_params()
            custom_params = self.build_custom_params()
            data.update(base_params)
            data.update(custom_params)
        self.response = requests.get(url=self.api_url(), data=data, headers=config.settings.HEADERS)
        return self.response

    def get_code(self):
        if self.response:
            return str(self.response.status_code)

    def get_message(self):
        if self.response:
            print("wode ", self.response.json())
            return self.response.json()['data']

    def get_response_message(self):
        if self.response:
            return str(self.response.json()['code'])

    def build_base_params(self):
        return {}

    def build_custom_params(self):
        return {}



if __name__ == '__main__':
      t = Trequest(base_url='http://market.shixhuat.com/',
                 url_params='getSendTimeForSendGoodsByAdminShopId')
      print(t.post())
      print(t.get_code())

