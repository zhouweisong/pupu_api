"""
-------------------------------------------------
   File Name：     test_api
   Description :
   Author :       zws
   date：          2018/3/13
-------------------------------------------------
   Change Activity:
                   2018/3/13:
-------------------------------------------------
"""
__author__ = 'zws'

from Common.DoExcel import DoExcel
from Common import myRequest
import unittest
import ddt
from Common.my_logger import *
import re

# 获取所有的测试数据

excel_path = dir_config.testcase_dir + "/api_info.xlsx"
de = DoExcel(excel_path)
all_case_datas = de.get_caseDatas_all()

global_vars = {}  # 设置一个全局变量

@ddt.ddt
class Test_Api(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        de.modify_phone()
        de.save_excelFile()


    @classmethod
    def tearDownClass(cls):
        pass

    @ddt.data(*all_case_datas)
    def test_api(self, case_data):

        global global_vars

        logging.info('==============开始执行第%d个测试用例============='%case_data['case_id'])

        #动态替换 - 判断请求数据中，是否要替换全局变量的值、全局变量是否存在。
        if len(global_vars) > 0 and case_data["request_data"] is not None:
            for key,value in global_vars.items():
                if case_data["request_data"].find(key) != -1:
                    logging.info('需要在参数中替换全局变量')
                    case_data["request_data"] = case_data["request_data"].replace(key, value)

        res = myRequest.myRequest(case_data["url"], case_data["method"], case_data["request_data"])

        if 'related_exp' in case_data.keys():
            logging.info('需要从响应结果中提取数据：')
            temp = case_data['related_exp'].split("=")

            res_id = re.findall(temp[1], res.text)
            global_vars[temp[0]] = res_id[0]

        logging.info('期望结果是：')
        logging.info(case_data["expected_data"])
        logging.info('实际结果是：')
        logging.info(str(res.text))

        #判断断言选择类型 是全值匹配 还是 包含匹配
        if int(case_data['compare_type']) == 0:
            logging.info('全值匹配模式')
            try:
                self.assertEqual(res.text, case_data["expected_data"])
                logging.info('结果对比成功，测试用例通过')
            except AssertionError:
                logging.exception("结果对比失败")
                raise AssertionError
        else:
            logging.info('部分匹配模式')
            try:
                self.assertIn(case_data["expected_data"], res.text)
                logging.info('结果对比成功，测试用例通过')
            except AssertionError:
                logging.exception("结果对比失败")
                raise AssertionError


if __name__ == '__main__':
    unittest.main()
