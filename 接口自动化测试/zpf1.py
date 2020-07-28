# coding:utf-8
import requests
# base_url1 = 'http://httpbin.org'

# 参数传递，get请求
# param_data = {'user': 'zxw', 'password': '6666'}
#
# r = requests.get(base_url+'/get', params=param_data)
# print(r.url)
# print(r.status_code)
#post请求
def jk():
    base_url = 'http://market.shixhmit.com/test/getSendTimeForSendGoodsByAdminShopId'

    form_data = {'adminShopId': ''}
    header = {'content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url = base_url, data=form_data, headers=header)
    print(r.text)
    return r.text

if __name__ == "__main__":
   jk()

# form_data = {'user': '51zxw', 'password': '8888'}
# r = requests.post(base_url1+'/post', data=form_data)
# print(r.text)
# print(r.status_code)
# print(r.url)

#请求头制定
#form_data = {'user': '51zxw', 'password': '8888'}
#header = {'user-agent': 'mozilla/3.0'}
#r = requests.post(base_url+'/post', data=form_data, headers=header)
#print(r.text)
#print(r.status_code)

#若请求时有cookie，User-Agent是要加上
