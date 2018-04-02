"""
-------------------------------------------------
   File Name：     my_logger
   Description :
   Author :       zws
   date：          2018/3/22
-------------------------------------------------
   Change Activity:
                   2018/3/22:
-------------------------------------------------
"""
__author__ = 'zws'

import logging
from Common import dirConfig
from logging.handlers import RotatingFileHandler
import time

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
logpath = dirConfig.log_dir + '/' + "app_autoTest_" + rq + ".log"

handler_1 = logging.StreamHandler()
handler_1.setLevel(logging.DEBUG)

handler_2 = RotatingFileHandler(logpath, maxBytes=1024*1024*100,backupCount=10)
handler_2.setLevel(logging.DEBUG)

logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.DEBUG,handlers=[handler_1,handler_2])