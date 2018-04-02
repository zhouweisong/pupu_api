"""
-------------------------------------------------
   File Name：     verifyCode_40005
   Description :
   Author :       zws
   date：          2018/3/30
-------------------------------------------------
   Change Activity:
                   2018/3/30:
-------------------------------------------------
"""
__author__ = 'zws'

import requests
from Common.myLogger import *

api = 'http://api798.impupu.com/api/verify'
parameter = {"mobile":"13801111155","register":"true"}

def verify_code_40005():
    for i in range(0,10):
        requests.post(url=api,params=parameter)
        logging.debug(requests.post(url=api,params=parameter).text)
