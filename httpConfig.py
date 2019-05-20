#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'lisa'
_version_="20190116"

import requests
import json
import configparser
import time

# 配置类
class httpConfig:
    '''配置要测试接口服务器的ip、端口、域名等信息，封装http请求方法，http头设置'''

    def __init__(self):
        config = configparser.ConfigParser()

        # 从配置文件中读取接口服务器IP、域名，端口
        config.read("config.ini")
        self.host = config['HTTP']['host']
        self.headers = {'Content-Type': 'application/json'}                # http 头
        self.globals = {
            'false': 0,
            'true': 0,
            'null': 0
        }

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    # 封装HTTP GET请求方法
    def get(self, path):
        url = self.host  + path
        #print (url)
        try:
            #print url
            # 设置重连次数
            requests.adapters.DEFAULT_RETRIES = 3
            # 设置连接活跃状态为False
            s = requests.session()
            s.keep_alive = False
            response = s.get(url,verify = False,headers=self.headers)
            return response

        except Exception as e:
            #print('%s' % e)
            return {}

    # 封装HTTP POST请求方法
    def post(self, path, data=""):
        url =self.host + path
        #print(url)
        #print (data)
        try:
            # # 设置重连次数
            # requests.adapters.DEFAULT_RETRIES = 3
            # # 设置连接活跃状态为False
            # s = requests.session()
            # s.keep_alive = False
            # print ("@@@")
            # response = s.post(url,data=data,verify = False,headers=self.headers)
            # #data = eval(response.text, self.globals)
            # print("###")
            #data = response.text.decode("utf-8")

            # t2 = time.time()
            # print (t2-t1)
            response = requests.post(url, data=data, verify=False, headers=self.headers)
            #print (response.text)
            return json.loads(response.text)

        except Exception as e:
            #print('%s' % e)
            return {}

    # 封装HTTP xxx请求方法
    # 自由扩展