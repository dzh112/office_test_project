#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from businessView.loginView import LoginView
from common.common_fun import Common


class CreateView(Common):

    def create_file(self, type, subtype=0):  # 新建文档

        logging.info('==========create_file_%s==========' % type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_main').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_%s' % type).click()

        logging.info('choose Template %s' % subtype)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/iv_gv_image')[subtype].click()

    def save_file_option(self, file_name='', save_path='', item=1, save='save'):  # 保存、另存为 save=['save','save_as']
        logging.info('==========save_file_option_%s==========' % save)
        self.group_button_click('文件')

        logging.info('choose %s' % save)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_%s' % save).click()  # 点击保存或另存为

        # exist_file = '//*[@resource-id = "com.yozo.office:id/yozo_ui_full_screen_select_path_title"]'
        exist_file = '//*[@resource-id = "com.yozo.office:id/yozo_ui_please_selcet_path_tv"]'
        if self.get_element(exist_file):  # 判断文件是否为新建
            self.save_action(file_name, save_path, item)
        else:
            if save == 'save_as':
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_folder').click()
                self.save_action(file_name, save_path, item)

    def save_file_icon(self, file_name='', save_path='', item=1):  # 点击保存图标
        logging.info('==========save_file_icon==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
        exist_file = '//*[@resource-id = "com.yozo.office:id/yozo_ui_please_selcet_path_tv"]'
        if self.get_element(exist_file):  # 判断文件是否为新建
            self.save_action(file_name, save_path, item)

    def save_action(self, file_name, save_path, item=1):  # 文件名，本地还是云端save_path=['local','cloud']，文件类型item=[1,2]
        logging.info('==========save_action_%s==========' % file_name)
        logging.info('choose save path %s' % save_path)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('whether need login')
        if self.get_toast_message('您尚未登录，请登录'):
            l = LoginView(self.driver)
            l.login_action('13915575564', 'zhang199412')
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('file named %s' % file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(file_name)

        logging.info('choose file type %s' % item)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_type').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/file_type_item%s' % item).click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # save

        # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
        # self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()

    def check_save_file(self):
        logging.info('==========check_create_file==========')
        self.get_toast_message('保存成功')
