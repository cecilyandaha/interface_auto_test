#coding=utf-8
import json


class interface:
    def __init__(self,http):
        self.http = http

    {
        "afsRequest": {
            "scene": "string",
            "sessionId": "string",
            "sig": "string",
            "token": "string"
        },
        "areacode": "",
        "ip": "",
        "loginName": "13610000001",
        "passWord": "a123456"
    }
    def login(self,dataList):
        path="/proxy/login "
        dataJson={}
        afsRequest={}
        afsRequest["scene"]=  "string"
        afsRequest["sessionId"] =  "string"
        afsRequest["sig"] =  "string"
        afsRequest["token"] =  "string"
        dataJson["afsRequest"]=afsRequest
        dataJson["areacode"] = ""
        dataJson["ip"] = ""
        dataJson["loginName"] = dataList[0]
        dataJson["passWord"] = dataList[1]
        return self.http.post(path,json.dumps(dataJson))




