import logging
import time
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd


class TestWordCheckApprove(StartEnd):

    def wp_check_approve_setup(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('审阅')

    def test_wp_check_approve(self):
        # 修订
        logging.info('==========test_wp_check_approve==========')
        self.wp_check_approve_setup()
        wv = WpView(self.driver)
        wv.check_approve_revision()

    def test_wp_picture_surround(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wp = WpView(self.driver)
        wp.swipeup()
        wp.choose_pic()
        wp.surround()
        time.sleep(10)


