# -*-coding:utf-8-*-

from object.test.login_test import *
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *

suite = unittest.TestSuite()
suite.addTest(TestLogin('test_login_page'))

f = open(report_file, 'wb')
HTMLTestRunner(stream=f, title="login_page_test", description="测试报告").run(suite)
f.close()
