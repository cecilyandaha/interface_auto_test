#coding=utf-8
import json


class InterfaceBitasset:
    def __init__(self,http):
        self.http = http

    def login(self,dataMap):
        path="/proxy/login"
        dataJson={}
        afsRequest={}
        afsRequest["scene"]=  "string"
        afsRequest["sessionId"] =  "string"
        afsRequest["sig"] =  "string"
        afsRequest["token"] =  "string"
        dataJson["afsRequest"]=afsRequest
        dataJson["areacode"] = ""
        dataJson["ip"] = ""
        dataJson["loginName"] = dataMap["loginName"]
        dataJson["passWord"] = dataMap["passWord"]
        return self.http.post(path,json.dumps(dataJson))

    def userInfo(self):
        path="/proxy/users/userInfo"
        return self.http.get(path)








