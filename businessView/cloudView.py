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

    def cloud_login_action(self, username, password):
        logging.info('==========cloud_login_action==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_logo').click()
        self.driver.implicitly_wait(3)
        logging.info('username is:%s' % username)
        self.find_element(*self.username_type).set_text(username)  # 输入手机号

        logging.info('password is:%s' % password)
        self.find_element(*self.password_type).set_text(password)  # 输入密码

        logging.info('click loginBtn')
        self.find_element(*self.loginBtn).click()  # 点击登录按钮
        logging.info('login finished!')

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
