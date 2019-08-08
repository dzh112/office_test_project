#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.webdriver.common.by import By

from common.common_fun import Common


class SortView(Common):

    def sort(self, type='time', sort='down'):
        # type =  ['type','name','size','time'] #可选择的排序类型
        # sort = ['up','down']  #升序还是降序
        logging.info('==========sort==========')
        self.driver.find_elements(By.ID, 'com.yozo.office:id/im_title_bar_menu_shot').click()
        logging.info('sorted by %s' % type)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/rl_sort_%s' % type).click()
        logging.info('sort with %s' % sort)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/btn_sort_%s' % sort).click()
        logging.info('sort finish')
        self.driver.implicitly_wait(5)

    def check_sort(self, filetype='all', type='time', sort='down'):
        logging.info('==========check_sort==========')
        if filetype == 'all' and type == 'type':
            type_sort = [['doc','docx'],['xls','xlsx'],['ppt','pptx'],['pdf']]
            if sort == 'down':
                ele_id = (By.ID, 'com.yozo.office:id/tv_title')
                attr = 'name'
                ele_text = self.get_elements_attribute(ele_id,attr)
                ele_suffix = list(map(lambda x: x[x.rindex('.') + 1:].lower(), ele_text))


