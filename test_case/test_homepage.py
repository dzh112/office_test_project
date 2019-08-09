#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from ddt import ddt, data

from businessView.createView import CreateView
from businessView.iconView import IconView
from businessView.loginView import LoginView
from businessView.searchView import SearchView
from businessView.selectView import SelectView
from businessView.sortView import SortView
from common.myunit import StartEnd
from common.tool import rm_file

# filetypes = ['all','wp','ss','pg','pdf']
filetypes = ['all']
@ddt
class TestHomePage(StartEnd):
    csv_file = '../data/account.csv'

    def test_sort(self):
        logging.info('======test_sort=====')
        slv = SelectView(self.driver)
        slv.select_index('alldoc')
        stv = SortView(self.driver)
        type,sort = 'type','up'
        stv.sort(type,sort)
        self.assertTrue(stv.check_sort(type,sort))

    @unittest.skip('skip test_file_type')
    @data(*filetypes)
    def test_file_type(self,f):
        logging.info('======test_file_type=====')
        slv = SelectView(self.driver)
        slv.select_index('alldoc')

        slv.select_file_type(f)
        self.assertTrue(slv.check_select_file_type(f))

    @unittest.skip('skip test_info_file')
    def test_info_file(self):
        logging.info('======test_info_file=====')
        iv = IconView(self.driver)
        iv.info_file()

        self.assertTrue(iv.check_info_file())

    @unittest.skip('skip test_share_file')
    def test_share_file(self):
        logging.info('======test_share_file=====')
        iv = IconView(self.driver)
        iv.share_file()

        self.assertTrue(iv.check_share_file())

    @unittest.skip('skip test_delete_file')
    def test_delete_file(self):
        logging.info('======test_delete_file=====')
        iv = IconView(self.driver)
        type = 'last'
        iv.select_index(type)
        file_name = iv.delete_file(type)

        self.assertTrue(iv.check_delete_file(type,file_name))

    @unittest.skip('skip test_mark_star')
    def test_mark_star(self):
        logging.info('======test_mark_star=====')
        iv = IconView(self.driver)
        file_name = iv.mark_remove_star()

        self.assertTrue(iv.check_mark_star(file_name))

    @unittest.skip('skip test_upload')
    def test_upload(self):
        logging.info('======test_upload=====')
        iv = IconView(self.driver)
        iv.upload()

        self.assertTrue(iv.check_upload())

    @unittest.skip('skip test_login_13915575564')
    def test_login(self):
        logging.info('======test_login=====')
        sv = SearchView(self.driver)
        sv.user_logo()
        l = LoginView(self.driver)
        if l.check_login_status():
            l.logout_action()
        data = l.get_csv_data(self.csv_file, 4)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_login_status())

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
