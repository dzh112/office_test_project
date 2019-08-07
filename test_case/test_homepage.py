#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from businessView.createView import CreateView
from businessView.searchView import SearchView
from common.myunit import StartEnd
from common.tool import rm_file


class TestHomePage(StartEnd):

    @unittest.skip('skip test_user_log')
    def test_user_log(self):
        logging.info('==========test_user_log==========')
        sv = SearchView(self.driver)
        sv.user_logo()
        self.assertTrue(sv.check_user_logo())

    @unittest.skip('skip test_create')
    def test_create(self):
        rm_file()
        logging.info('==========test_create_search==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        self.assertTrue(cv.check_create_file())

    @unittest.skip('skip test_search')
    def test_search(self):
        logging.info('==========test_search==========')
        sv = SearchView(self.driver)
        file_name = '00045.docx'
        sv.search_action(file_name)
        self.assertTrue(sv.check_search_action(file_name))


if __name__ == '__main__':
    unittest.main()
