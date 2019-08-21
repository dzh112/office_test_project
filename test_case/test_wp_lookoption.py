import time
import unittest
import logging
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wp_lookupView import WpLookUpView
from common.myunit import StartEnd


class TestWordLookOption(StartEnd):

    def test_wp_rotate(self):
        # WORD文档横竖屏切换
        logging.info('==========test_wp_rotate==========')
        self.driver.orientation = 'PORTRAIT'
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        logging.info('==========screen_rotate==========')
        # allowed_values = ['LANDSCAPE', 'PORTRAIT']
        s_wight = ov.get_size()[0]
        print(s_wight)
        self.driver.orientation = 'LANDSCAPE'
        time.sleep(5)
        h_wight = ov.get_size()[1]
        print(h_wight)
        self.assertEqual(h_wight, s_wight, msg='test_wp_rotate fail')
        self.driver.orientation = 'PORTRAIT'

    def test_self_adaption(self):
        # 阅读自适应
        logging.info('==========test_self_adaption==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp_lookup = WpLookUpView(self.driver)
        wp_lookup.self_adaption()
        A_self = ov.exist("//*[@resource-id='com.yozo.office:id/yozo_ui_app_frame_title_container']")
        B_self = ov.exist("//*[@resource-id='com.yozo.office:id/yozo_ui_app_frame_option_container']")
        self.assertFalse(A_self, msg='self_adaption title_container exist!')
        self.assertFalse(B_self, msg='self_adaption option_container exist!')

    def test_wp_undo_redo(self):
        logging.info('==========test_wp_undo_redo==========')

        gv = GeneralView(self.driver)
        result1, result2 = gv.check_undo_redo_event()
        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')

    def test_wp_swipe(self):
        logging.info('==========test_wp_swipe==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp_lookup = WpLookUpView(self.driver)
        time.sleep(3)
        wp_lookup.swipeup()

    def test_wp_find_replace(self):
        logging.info('==========test_wp_find_replace==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp_lookup = WpLookUpView(self.driver)

        wp_lookup.wp_find_replace()

    def test_wp_bookmark(self):
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp_lookup = WpLookUpView(self.driver)
        self.assertTrue(wp_lookup.wp_bookmark(), msg='test_wp_bookmark fail')

    def test_wp_jump(self):
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp_lookup = WpLookUpView(self.driver)
        wp_lookup.wp_jump()


if __name__ == '__main__':
    unittest.main()
