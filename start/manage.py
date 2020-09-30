import  unittest,os,sys
from package.HTMLTestRunner import HTMLTestRunner
from config.file import report_html
from config.log import Logger

path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
case_path=path+'/case/'
# print('case_path',case_path)
# log = Logger(__name__) # 日子

reporttitle='CMDB自动化测试报告'  #测试报告title
description='CMDB测试结果如下：'  #测试报告描述


def create_report():
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*test.py',top_level_dir=None)
    for test_case in discover:
        test_suit.addTest(test_case)
    re_open = report_html()
    # runner=BSTestRunner.BSTestRunner(stream=re_open,title=reporttitle,description=description)
    runner=HTMLTestRunner(stream=re_open,verbosity=1,title=reporttitle,description=description)
    runner.run(test_suit)
    re_open.close()
    # Logger.log().logger.info(sys._getframe().f_code.co_name)
    # Logger()

if __name__ == '__main__':
    create_report()
