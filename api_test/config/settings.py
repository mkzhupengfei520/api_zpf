#coding:utf-8

#Config file

ENV= 'test'

APP_ID = ''

APP_SECRET = ''

APP_VERSION = ''

HEADERS = {'test':'test','testa':'testa','testb':'testb'}

# test url config
def demo():
    return {'headers':{'test':'test','testa':'testa','testb':'testb'},
            'base_url':'192.168.1.1/api/localhost',
            'url_params':'user/create/new_account',
            }

