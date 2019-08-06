#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from businessView.createView import CreateView
from businessView.searchView import SearchView
from common.myunit import StartEnd
from common.tool import rm_file


class TestHomePage(StartEnd):

    def test_create(self):
        rm_file()
        logging.info('==========test_create_search==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        self.assertTrue(cv.check_create_file())

    def test_search(self):
        sv = SearchView(self.driver)
        file_name = 'xxxx'
        sv.search_action(file_name)

        self.assertTrue(sv.check_search_action(file_name))

if __name__ == '__main__':
    unittest.main()