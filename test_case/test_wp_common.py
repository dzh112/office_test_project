import logging
import time
import unittest
from ddt import ddt, data, unpack

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd


@ddt
class TestWordCommon(StartEnd):

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

    def test_wp_undo_redo(self):
        # 撤销重做
        logging.info('==========test_wp_undo_redo==========')
        gv = GeneralView(self.driver)
        result1, result2 = gv.check_undo_redo_event()

        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')

    def test_wp_zoom_pinch(self):
        # 视图缩放
        logging.info('==========test_zoom==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        ov.zoom()
        time.sleep(10)
        ov.pinch()
        time.sleep(10)

    def test_wp_swipe(self):
        # WORD文档滚屏
        logging.info('==========test_wp_swipe==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wp = WpView(self.driver)
        wp.swipeup()

    def test_wp_export_pdf(self):  # 导出pdf
        logging.info('==========test_export_pdf==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')

        gv = GeneralView(self.driver)
        file_name = 'export_pdf ' + time.strftime("%H%M%S")
        gv.export_pdf(file_name, 'local')

        self.assertTrue(gv.check_export_pdf())

    @data(['wx'], ['qq'], ['ding'], ['mail'])
    @unpack
    def test_wp_share_file(self, way):  # 分享文件
        logging.info('==========test_wp_share_file==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.share_file(way)

    def test_wp_save_newFile(self):  # 新建脚本保存
        logging.info('==========test_wp_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_newFile ' + time.strftime("%H%M%S")
        cv.save_file_icon(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())

    def test_wp_save_existFile(self):  # 已有文件改动保存
        logging.info('==========test_wp_save_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv.switch_write_read()
        self.driver.press_keycode(48)
        cv.save_file_icon()
        self.assertTrue(cv.check_save_file())

    def test_wp_save_as_existFile(self):  # 已有文件另存为
        logging.info('==========test_save_as_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        file_name = 'save_as_existFile ' + time.strftime("%H%M%S")
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    def test_wp_save_as_newFile(self):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_as_newFile ' + time.strftime("%H%M%S")
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())


if __name__ == '__main__':
    unittest.main()
