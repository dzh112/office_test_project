import logging

from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd


class TestWordInsert(StartEnd):

    def wp_insert_setup(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('插入')

    def test_wp_insert_shape(self):
        logging.info('==========test_wp_insert_shape==========')
        self.wp_insert_setup()
        wv = WpView(self.driver)
        wv.insert_shape()

    def test_wp_insert_table(self):
        logging.info('==========test_wp_insert_table==========')
        self.wp_insert_setup()
        wv = WpView(self.driver)
        wv.insert_table()

    def test_wp_insert_watermark(self):
        logging.info('==========test_wp_insert_watermark==========')
        self.wp_insert_setup()
        wv = WpView(self.driver)
        wv.insert_watermark()


