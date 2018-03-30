"""
-------------------------------------------------
   File Name：     dir_config
   Description :
   Author :       zws
   date：          2018/3/21
-------------------------------------------------
   Change Activity:
                   2018/3/21:
-------------------------------------------------
"""
__author__ = 'zws'

import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]

testcase_dir = cur_dir.replace('Common','TestDatas')

htmlreport_dir = cur_dir.replace('Common','HtmlTestReport')

log_dir = cur_dir.replace('Common','Logs')