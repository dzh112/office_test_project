#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from common.myunit import StartEnd


class TestFunc(StartEnd):

    def test_save1(self):
        logging.info('==========test_save1==========')
        ov = OpenView(self.driver)
        ov.open_file('saveIcon.docx')
        cv = CreateView(self.driver)
        cv.operate_sample()
        cv.save_file_icon()

    def test_save(self):
        logging.info('==========test_save==========')
        cv = CreateView(self.driver)
        cv.create_file('wp',0)
        cv.save_file_icon('saveIcon','local',2)
        self.assertTrue(cv.check_save_file())

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
        result1,result2 = gv.check_undo_redo_event()

        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')
