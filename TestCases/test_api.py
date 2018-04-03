"""
-------------------------------------------------
   File Name：     test_api
   Description :
   Author :       zws
   date：          2017/8/13
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
from Common.myLogger import *
import re
from Common.verifyCode_40005 import verify_code_40005

# 获取所有的测试数据

excel_path = dirConfig.testcase_dir + "/api_info.xlsx"
de = DoExcel(excel_path)
all_case_datas = de.get_caseDatas_all()

global_vars = {}  # 设置一个全局变量

@ddt.ddt
class Test_Api(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        de.modify_phone()
        de.save_excelFile()
        verify_code_40005()

    @classmethod
    def tearDownClass(cls):
        pass

    @ddt.data(*all_case_datas)
    def test_api(self, case_data):
        ua = {"user-agent":"Jiemoapp 1.5.0.15 (Android (26/8.0.0; 480dpi; 1080x1920; HUAWEI; ALP-AL00; HWALP; kirin970))",
              "device-id":"65c049254538bd4f00c857e0d01b8fbb","device-mac":"1c:15:1f:1f:7b:6d"}

        global global_vars

        logging.info('==============开始执行第%d个测试用例============='%case_data['case_id'])


        #动态替换 - 判断请求数据中，是否要替换全局变量的值、全局变量是否存在。
        if len(global_vars) > 0 and case_data["request_data"] is not None:
            for key,value in global_vars.items():
                if case_data["request_data"].find(key) != -1:
                    logging.info('需要在参数中替换全局变量')
                    case_data["request_data"] = case_data["request_data"].replace(key, value)
                    logging.debug(case_data["request_data"])
                if case_data["expected_data"].find(key) != -1:
                    case_data["expected_data"] = case_data["expected_data"].replace(key, value)


        res = myRequest.myRequest(case_data["url"], case_data["method"], case_data["request_data"])
        logging.debug(case_data["request_data"])
        logging.debug(res.text)

        if 'related_exp' in case_data.keys():
            logging.info('需要从响应结果中提取数据：')
            temp = case_data['related_exp'].split("=")

            res_id = re.findall(temp[1], res.text)
            logging.debug('========================related_exp==============================')
            logging.debug(res_id)
            global_vars[temp[0]] = res_id[0]
            logging.debug('用户的票 是 ：')
            logging.debug(global_vars[temp[0]])

        if 'related_exp1' in case_data.keys():
            logging.info('需要从响应结果中提取数据：')
            temp = case_data['related_exp1'].split("=")

            res_id = re.findall(temp[1], res.text)
            logging.debug('========================related_exp1==============================')
            logging.debug(res_id)
            global_vars[temp[0]] = res_id[0]
            logging.debug('用户的id 是 ：')
            logging.debug(global_vars[temp[0]])

        # # 动态替换 - 判断请求数据中，是否要替换全局变量的值、全局变量是否存在。
        # if len(global_vars) > 0 and case_data["request_data"] is not None:
        #     for key, value in global_vars.items():
        #         if case_data["request_data"].find(key) != -1:
        #             logging.info('需要在参数中替换全局变量')
        #             case_data["request_data"] = case_data["request_data"].replace(key, value)
        #             logging.debug(case_data["request_data"])




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
