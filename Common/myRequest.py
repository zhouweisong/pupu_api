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
    #判断data数据是否为空，不为空则转换成字典
    if request_data is not None:
        request_data = eval(request_data)
    if method == "get":
        res = requests.get(url=url,params=request_data,timeout=20)
    elif method == "post":
        res = requests.post(url=url,data=request_data,timeout=20)
    else:
        res = None
    return res
