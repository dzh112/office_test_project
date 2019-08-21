#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.webdriver.common.by import By

from common.common_fun import Common


class SSView(Common):

    def hide_sheet(self):  # 隐藏工作表标签
        logging.info('==========hide_sheet==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_back').click()

    def show_sheet(self):  # 展开工作表标签
        logging.info('==========show_sheet==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_ss_sheet_tabbar').click()

    def add_sheet(self):  # 新建工作表
        logging.info('==========add_sheet==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_more').click()

    def rename_sheet(self, index, name):  # 重命名工作表
        logging.info('==========rename_sheet_%s==========' % name)
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index).click()
        if not self.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet"]'):
            self.driver.find_element(By.XPATH,
                                     '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index).click()
        self.driver.find_element(By.ID,'com.yozo.office:id/tv_ss_sheet_rename').click()
        self.driver.find_element(By.ID,'com.yozo.office:id/yozo_office_ss_sheet_rename_text').set_text(name)
        self.driver.find_element(By.ID,'com.yozo.office:id/yozo_office_ss_sheet_rename_ok').click()

    def check_rename_sheet(self, index, name):
        base_ele = self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index)
        text_name = base_ele.find_element(By.ID,'com.yozo.office:id/tv_ss_sheet_name').text
        if text_name == name:
            logging.info('rename success')
            return True
        else:
            logging.error('rename fail')
            self.getScreenShot('rename fail')
            return False
