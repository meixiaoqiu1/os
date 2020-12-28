import unittest
#from HTMLTestRunnerChinese import HTMLTestRunner
from utils.HTMLTestRunner import HTMLTestRunner
#from utils.sendEmail import SendEmail
from utils.sendEmailNew import SendEmail
import time

def whole_tests():
    test_dir = "..\\testcase"
    test_report = "..\\testReports\\"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    #HTMLTestRunner
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例情况：')

    runner.run(discover)
    fp.close()

    #发送邮件
    S= SendEmail(
        username='shemeiqiong@126.com',
        passwd='TSVSWNMMIHUDHUYY',
        recv=['xiaomeiqiu111@126.com'],
        title='接口自动化测试报告',
        content='报告详见附件',
        #ssl=True
    )
    S.send_email(S.new_report(test_report))  # 发送测试报告

if __name__=='__main__':
    whole_tests()

