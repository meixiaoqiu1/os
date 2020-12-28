import unittest
from common.pretest import PreTest
from utils.log import Logger
mylogger = Logger().getlog()



class TestHome(unittest.TestCase):

    def test01_saledata(self):
        mylogger.debug('调用销售数据-部门数据查询接口')
        try:
            res=PreTest().simplePost(1)
            result="查询成功"
            self.assertIn(result,res)
        except Exception as error:
            mylogger.error(error)

    def test02_saleTrendData(self):
        mylogger.debug('调用销售数据-部门趋势图接口')
        try:
            res=PreTest().simplePost(2)
            result="查询成功"
            self.assertIn(result,res)
        except Exception as error:
            mylogger.error(error)

    def test03_saleSkuData(self):
        mylogger.debug('调用销售数据-sku明细接口')
        try:
            res=PreTest().simplePost(3)
            result="查询成功"
            self.assertIn(result,res)
        except Exception as error:
            mylogger.error(error)

if __name__=='__main__':
    unittest.main()








