"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       zws
   date：          2018/3/21
-------------------------------------------------
   Change Activity:
                   2018/3/21:
-------------------------------------------------
"""
__author__ = 'zws'

from Common.HTMLTestRunnerNew import HTMLTestRunner
import unittest
from TestCases import test_api
from Common import dir_config
import time

s = unittest.TestSuite()
ul =unittest.TestLoader()
s.addTest(ul.loadTestsFromModule(test_api))

now = time.strftime('%Y_%m_%d_%H_%M_%S')
html_report_path =dir_config.htmlreport_dir+'/'+now+'.html'

fp = open(html_report_path,'wb')

runner = HTMLTestRunner(fp,title='API 测试报告')
runner.run(s)
