import time
import unittest
import logging
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView

from common.myunit import StartEnd


class TestWordLookOption(StartEnd):



    def test_wp_self_adaption(self):
        # 阅读自适应
        logging.info('==========test_wp_self_adaption==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp_lookup = WpView(self.driver)
        wp_lookup.self_adaption()
        A_self = ov.exist("//*[@resource-id='com.yozo.office:id/yozo_ui_app_frame_title_container']")
        B_self = ov.exist("//*[@resource-id='com.yozo.office:id/yozo_ui_app_frame_option_container']")
        self.assertFalse(A_self, msg='self_adaption title_container exist!')
        self.assertFalse(B_self, msg='self_adaption option_container exist!')



    def test_wp_find_replace(self):
        logging.info('==========test_wp_find_replace==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('查看')
        wp_lookup = WpView(self.driver)

        wp_lookup.wp_find_replace()

    def test_wp_bookmark(self):
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('查看')
        wp_lookup = WpView(self.driver)
        self.assertTrue(wp_lookup.wp_bookmark(), msg='test_wp_bookmark fail')

    def test_wp_jump(self):
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('查看')
        wp_lookup = WpView(self.driver)
        wp_lookup.wp_jump()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
