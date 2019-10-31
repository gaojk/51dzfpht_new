#coding=utf-8
import requests
import json
import sys
import os
from yhdzfpTestNew.Util.handle_ini import get_ini
base_path = os.getcwd()
sys.path.append(base_path)


class BaseRequest:
    def send_post(self, url, data, header=None):
        '''发送post请求'''
        res = requests.post(url=url, data=data, headers=header).text
        return res

    def send_get(self, url, data, header=None):
        '''发送get请求'''
        res = requests.get(url=url, params=data, headers=header).text
        return res

    def run_main(self, method, url, data, header=None):
        '''执行方法，传递method、url、data、header参数'''
        base_url = get_ini.get_ini_value('host_51dzfpht_new')
        #请求地址拼接：url = base_url + url
        if 'http' not in url:
            url = base_url + url
        if method == 'get':
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res

send_request = BaseRequest()
