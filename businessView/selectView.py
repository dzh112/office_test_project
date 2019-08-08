#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.common_fun import Common


class SelectView(Common):

    def select_index(self, type):  # 5个主页界面
        # index = ['last', 'alldoc', 'cloud', 'star', 'my']  # office的五个页面组件尾缀
        logging.info('==========select_index_%s==========' % type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_bottommenu_%s' % type).click()
        self.driver.implicitly_wait(10)


    def select_file_type(self, type):
        logging.info('==========select_file_type==========')
        if type == 'all':
            logging.info('select all files')
            self.driver.find_element(By.ID, 'com.yozo.office:id/rl_all').click()
        else:
            logging.info('select %s files', type)
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filetype_%s' % type).click()
        self.driver.implicitly_wait(5)

    def check_select_file_type(self, type):
        global types
        logging.info('==========check_select_file_type==========')
        ele_text = (By.ID, 'com.yozo.office:id/tv_title')
        attr = 'name'
        eles_attr = self.get_elements_attribute(ele_text,attr)
        eles_suffix = list(map(lambda x: x[x.rindex('.') + 1:].lower(), eles_attr))
        if type == 'all':
            types = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf']
        elif type == 'wp':
            types = ['doc', 'docx']
        elif type == 'ss':
            types = ['xls', 'xlsx']
        elif type == 'pg':
            types = ['ppt', 'pptx']
        elif type == 'pdf':
            types = ['pdf']
        if [False for suffix in eles_suffix if suffix not in types]:
            logging.error('filter %s file fail' % type)
            self.getScreenShot('filter %s file fail' % type)
            return False
        else:
            logging.info('filter %s file success' % type)
            return True


if __name__ == '__main__':
    eles = ['0045.doc', '00056.pdf','456.docx','7897.xls']
    eles_suffix = list(map(lambda x: x[x.index('.') + 1:], eles))
    print(enumerate(eles_suffix))
    types = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf']
    # print(eles_suffix)
    # exist = [False for suffix in eles_suffix if suffix not in types]
    # if exist:
    #     print('sssss')
    # else:
    #     print('ccccc')
