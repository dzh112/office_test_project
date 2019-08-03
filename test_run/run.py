import HTMLTestRunner
import unittest
# from  BSTestRunner import BSTestRunner
import time,logging
import sys
path='D:\\yozo_test_project\\'
sys.path.append(path)

test_dir='../test_case'
report_dir='../reports'

# suite = unittest.TestSuite()  # 创建测试套件
# 找到某个目录下所有的以test开头的Python文件里面的测试用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_save_as.py')
# for case in all_cases:
#     suite.addTests(case)  # 把所有的测试用例添加进来
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'Mobile_Office_Report.html'
fp = open(r'%s' % report_name, "wb")
# discover = unittest.defaultTestLoader.discover("", pattern="Run.py", top_level_dir=None)
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='YOZO_Mobile_Office_Report', description='yozo Android app test report')
# logging.info('start run test case...')
# runner.run(suite)
# fp.close()
with open(r'%s'%report_name,'wb') as f:
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='YOZO_Mobile_Office_Report',description='yozo Android app test report')
    logging.info('start run test case...')
    runner.run(discover)

# discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')
# now=time.strftime('%Y-%m-%d %H_%M_%S')
# report_name=report_dir+'/'+now+' test_report.html'
#
# with open(report_name,'wb') as f:
#     runner=BSTestRunner(stream=f,title='Kyb Test Report',description='kyb Android app test report')
#     logging.info('start run test case...')
#     runner.run(discover)