#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common


class CloudView(Common):
    username_type = (By.ID, 'com.yozo.office:id/et_account')
    password_type = (By.ID, 'com.yozo.office:id/et_pwd')
    loginBtn = (By.ID, 'com.yozo.office:id/btn_login')
    new_folder = (By.ID, 'com.yozo.office:id/im_title_bar_menu_newf')  # 新建文件夹
    new_folder_name = (By.ID, 'com.yozo.office:id/et_newfoldername')  # 文件夹名称
    btn_true = (By.ID, 'com.yozo.office:id/btn_true')  # 确认文件名

    def cloud_login_action(self, username, password):
        logging.info('==========cloud_login_action==========')
        self.find_element(By.ID, 'com.yozo.office:id/btn_logo').click()
        self.driver.implicitly_wait(3)
        logging.info('username is:%s' % username)
        self.find_element(*self.username_type).set_text(username)  # 输入手机号

        logging.info('password is:%s' % password)
        self.find_element(*self.password_type).set_text(password)  # 输入密码

        logging.info('click loginBtn')
        self.find_element(*self.loginBtn).click()  # 点击登录按钮
        logging.info('login finished!')

    def cloud_new_folder(self, name):
        self.find_element(*self.new_folder).click()

        self.find_element(*self.new_folder_name).send_keys(name)
        self.find_element(*self.btn_true).click()

    def check_cloud_button(self):
        logging.info('==========check_cloud_button==========')
        try:
            self.find_element(By.ID, 'com.yozo.office:id/btn_logo')
        except NoSuchElementException:
            logging.info('Already login')
            return False
        else:
            logging.info('Not login!')
            return True

    def check_upload_folder(self):
        logging.info('==========check_upload_folder==========')
        try:
            self.find_element(By.XPATH, "//*[@text='自动上传']")
        except NoSuchElementException:
            logging.info('Cloud login fail!')
            return False
        else:
            logging.info('Cloud login success!')
            return True

    def check_folder_name(self, name):
        logging.info('==========check_folder_name==========')
        try:
            self.find_element(By.XPATH, "//*[@text='%s']" % name)
        except NoSuchElementException:
            logging.info('Folder create fail!')
            return False
        else:
            logging.info('Folder create success!')
            return True



