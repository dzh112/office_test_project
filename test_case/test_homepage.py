#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from businessView.createView import CreateView
from businessView.searchView import SearchView
from common.myunit import StartEnd


class TestHomePage(StartEnd):

    def test_create_search(self):
        logging.info('==========test_create_search==========')
        cv = CreateView(self.driver)
        file_name = cv.create_file('wp')
        cv.check_create_file()

        sv = SearchView(self.driver)
        sv.search_action(file_name)

        self.assertTrue(sv.check_search_action(file_name))

if __name__ == '__main__':
    unittest.main()