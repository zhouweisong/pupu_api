"""
-------------------------------------------------
   File Name：     myRequest
   Description :
   Author :       zws
   date：          2018/3/13
-------------------------------------------------
   Change Activity:
                   2018/3/13:
-------------------------------------------------
"""
__author__ = 'zws'

import requests


def myRequest(url,method,request_data):
    ua = {"user-agent": "Jiemoapp 1.5.0.15 (Android (26/8.0.0; 480dpi; 1080x1920; HUAWEI; ALP-AL00; HWALP; kirin970))",
          "device-id": "65c049254538bd4f00c857e0d01b8fbb", "device-mac": "1c:15:1f:1f:7b:6d"}
    #判断data数据是否为空，不为空则转换成字典
    if request_data is not None:
        request_data = eval(request_data)
    if method == "get":
        res = requests.get(url=url,params=request_data,timeout=20,headers=ua)
    elif method == "post":
        res = requests.post(url=url,data=request_data,timeout=20,headers =ua)
    else:
        res = None
    return res
