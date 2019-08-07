#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from common.common_fun import Common


class SearchView(Common):

    def user_logo(self):
        logging.info('==========user_logo==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()

    def check_user_logo(self):
        logging.info('==========check_user_logo==========')
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/rl_myinfo_name')
        except NoSuchElementException:
            logging.error('user logo click Fail!')
            self.getScreenShot('user logo fail clicking')
            return False
        else:
            logging.info('user logo click Success!')
            return True

    def search_action(self, keyword):
        logging.info('==========search_action==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        logging.info('input keyword %s' % keyword)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(keyword)
        logging.info('searching...')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()

    def check_search_action(self, keyword):
        logging.info('==========check_search_action==========')
        try:
            self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % keyword.lower())
            'com.yozo.office:id/rl_search_type'
            'com.yozo.office:id/list_searchfile'
        except NoSuchElementException:
            logging.error('search Fail!')
            self.getScreenShot('search fail %s' % keyword)
            return False
        else:
            logging.info('search Success!')
            return True


if __name__ == '__main__':
    s = '00001.DOCX'
    print(s.lower())
