#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from common.common_fun import Common


class CreateView(Common):

    def create_file(self, type, subtype=0):
        file_type = (By.ID, 'com.yozo.office:id/fb_show_menu_%s' % type)
        file_name = 'untitleFile' + subtype.__str__()

        logging.info('==========create_file_%s==========' % type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_main').click()
        self.driver.find_element(file_type).click()
        logging.info('choose a Template')
        self.driver.find_elements(By.ID, 'com.yozo.office:id/iv_gv_image')[subtype].click()
        self.driver.implicitly_wait(3)
        logging.info('saving file')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        # self.driver.implicitly_wait(10)
        # self.driver.keyevent(4)
        # self.driver.keyevent(4)
        return file_name

    def check_create_file(self):
        logging.info('==========check_create_file==========')
        toast_message = "保存成功"
        message = '//*[@text="{' + toast_message + '}"]'
        try:
            self.find_element(By.XPATH, message)
        except NoSuchElementException:
            logging.error('saving Fail!')
            return False
        else:
            logging.error('saving Success!')
            return True
