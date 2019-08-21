#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from ddt import ddt, data

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from common.myunit import StartEnd

waylist = ['wx', 'qq', 'ding', 'mail']

@ddt
class TestFunc(StartEnd):

    def test_zoom_pinch(self):
        logging.info('==========test_zoom==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')
        ov.Zoom_action()
        ov.Pinch_action()

    def test_read_mode(self): #横屏模式
        logging.info('==========test_read_mode==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.switch_write_read()
        self.assertTrue(gv.check_write_read())

    @data(*waylist)
    def test_share_file(self, way):  # 分享文件
        logging.info('==========test_share_file==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        gv.share_file(way)

    # @unittest.skip('skip test_undo_redo')
    def test_export_pdf(self):  # 导出pdf
        logging.info('==========test_export_pdf==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        file_name = 'export_pdf ' + gv.getTime('%H_%M_%S')
        gv.export_pdf(file_name, 'local')

        self.assertTrue(gv.check_export_pdf())

    @unittest.skip('skip test_undo_redo')
    def test_save_as_existFile(self):  # 已有文件另存为
        logging.info('==========test_save_as_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        ov.open_file('save1.doc')
        file_name = 'save_as_existFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
    def test_save_existFile(self):  # 已有文件改动保存
        logging.info('==========test_save_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        ov.open_file('save1.doc')
        gv.switch_write_read()
        self.driver.press_keycode(48)
        cv.save_file_icon()
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
    def test_save_as_newFile(self):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_as_newFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
    def test_save_newFile(self):  # 新建脚本保存
        logging.info('==========test_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_newFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_icon(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
    def test_rotate(self):
        logging.info('==========test_rotate==========')
        ov = OpenView(self.driver)
        ov.open_file('00555.doc')
        gv = GeneralView(self.driver)
        # gv.screen_rotate('landscape')
        self.assertTrue(gv.check_rotate())
        gv.screen_rotate('portrait')

    @unittest.skip('skip test_undo_redo')
    def test_undo_redo(self):
        logging.info('==========test_undo_redo==========')
        gv = GeneralView(self.driver)
        result1, result2 = gv.check_undo_redo_event()

        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')
