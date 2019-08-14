#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os

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

    filework_pop_del = (By.ID, 'com.yozo.office:id/ll_filework_pop_del')  # 删除
    filework_pop_rename = (By.ID, 'com.yozo.office:id/ll_filework_pop_rename')  # 重命名
    filework_pop_download = (By.ID, 'com.yozo.office:id/ll_filework_pop_download')  # 下载
    filework_pop_copy = (By.ID, 'com.yozo.office:id/ll_filework_pop_copy')  # 复制
    filework_pop_share = (By.ID, 'com.yozo.office:id/ll_filework_pop_share')  # 分享
    filework_pop_info = (By.ID, 'com.yozo.office:id/ll_filework_pop_info')  # 信息
    copy_btn_new_file = (By.ID, 'com.yozo.office:id/btn_new_file')  # 复制文件时，新建文件夹按钮
    copy_new_file_rename = (By.ID, 'com.yozo.office:id/et_newfoldername')  # 新建文件夹重命名
    copy_btn_move_true = (By.ID, 'com.yozo.office:id/btn_move_true')  # 复制到此路径


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

    def cloud_delete_new_folder(self, index):
        delete_folder_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index + 1].text
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index].click()
        self.find_element(*self.filework_pop_del).click()
        self.find_element(*self.btn_true).click()
        return delete_folder_name

    def cloud_rename_folder(self, index):
        rename_folder_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index + 1].text
        logging.info('=======cloud rename folder %s=======' % rename_folder_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index].click()
        self.find_element(*self.filework_pop_rename).click()
        rename = rename_folder_name + '01'
        self.find_element(*self.new_folder_name).send_keys(rename)
        self.find_element(*self.btn_true).click()
        return rename

    def cloud_download_file(self, index):
        download_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======cloud download file %s=======' % download_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_download).click()

    # def cloud_file_copy(self, index):
    #     pass

    def cloud_delete_file(self, index):
        delete_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======cloud delete file%s=======' % delete_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_del).click()
        self.find_element(*self.btn_true).click()
        return delete_file_name

    def cloud_rename_file(self, index):
        rename_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======rename %s=======' % rename_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_rename).click()
        rename = os.path.splitext(rename_file_name)[0] + '01'
        self.find_element(*self.new_folder_name).send_keys(rename)
        self.find_element(*self.btn_true).click()
        return rename + os.path.splitext(rename_file_name)[1]

    def cloud_share_file(self, index):
        share_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======cloud share %s=======' % share_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_share).click()

    def cloud_file_info(self, index):
        info_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======cloud %s info =======' % info_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_info).click()

    def cloud_copy_file(self, index):
        copy_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======cloud_copy_file %s=======' % copy_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_copy).click()
        self.find_element(*self.copy_btn_new_file).click()
        rename = os.path.splitext(copy_file_name)[0] + '01'
        self.find_element(*self.copy_new_file_rename).send_keys(rename)
        self.find_element(*self.btn_true).click()
        self.find_element(By.XPATH,"//*[@resource-id='com.yozo.office:id/tv_title'][@text='%s']" % rename).click()
        self.find_element(*self.copy_btn_move_true).click()

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
            logging.info('Folder not exist!')
            return False
        else:
            logging.info('Folder exist!')
            return True
