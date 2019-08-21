#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from functools import reduce

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.common_fun import Common


class SelectView(Common):

    def phone_local(self):  # 手机本地文档
        logging.info('==========phone_local==========')
        self.find_element(By.ID, 'com.yozo.office:id/rl_openinfo_phone').click()

    def cjeck_phone_local(self):
        logging.info('==========cjeck_phone_local==========')
        try:
            self.find_element(By.ID, 'com.yozo.office:id/tv_local_file_path')
        except NoSuchElementException:
            logging.error('open local file fail')
            self.getScreenShot('open local file fail')
            return False
        else:
            logging.info('open local file success')
            return True

    def select_index(self, type):  # 5个主页界面
        # index = ['last', 'alldoc', 'cloud', 'star', 'my']  # office的五个页面组件尾缀
        logging.info('==========select_index_%s==========' % type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_bottommenu_%s' % type).click()
        self.driver.implicitly_wait(10)

    def select_file_type(self, type):  # 文档类型
        logging.info('==========select_file_type==========')
        if type == 'all':
            logging.info('select all files')
            self.driver.find_element(By.ID, 'com.yozo.office:id/rl_all').click()
        else:
            logging.info('select %s files', type)
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filetype_%s' % type).click()
        self.driver.implicitly_wait(10)

    def check_select_file_type(self, type):
        global types
        logging.info('==========check_select_file_type==========')
        # ele_text = (By.XPATH, '//*[@resource-id="com.yozo.office:id/tv_title"]')
        ele_text = '//android.widget.TextView[@resource-id="com.yozo.office:id/tv_title"]'
        attr = 'name'
        eles_attr = self.get_elements_attribute(ele_text, attr)
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
    # eles = ['0045.doc', '00056.pdf', '456.docx', '7897.xls', '45d6.docx']
    # eles_suffix = list(map(lambda x: x[x.index('.') + 1:], eles))
    # print(eles_suffix)
    eles_suffix = ['doc', 'pdf', 'docx', 'xls', 'docx']
    eles1 = reduce(lambda x, i: x if i in x else x + [i], [[], ] + eles_suffix)  # 方法需要理解
    print(eles1)
    def a(x,i):
        return x if i in x else x + [i]

    # print([1, 34, 4] + [3])
    # print(enumerate(eles_suffix))
    # types = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf']
    # print(eles_suffix)
    # exist = [False for suffix in eles_suffix if suffix not in types]
    # if exist:
    #     print('sssss')
    # else:
    #     print('ccccc')
