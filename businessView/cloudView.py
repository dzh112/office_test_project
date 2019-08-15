#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
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

    def cloud_create_file_wp(self):
        logging.info('==========create_file_wp==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_main').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_wp').click()
        logging.info('choose Template 0')
        self.driver.find_elements(By.ID, 'com.yozo.office:id/iv_gv_image')[0].click()
        self.driver.implicitly_wait(3)
        logging.info('saving cloud file')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_cloud').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text('wp0')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()

    def cloud_download_file(self, index):
        download_file_name = self.find_elements(By.ID, 'com.yozo.office:id/tv_title')[index].text
        logging.info('=======cloud download file %s=======' % download_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_download).click()
        self.driver.implicitly_wait(10)

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
        rename = os.path.splitext(copy_file_name)[0] + '01'
        logging.info('=======cloud_copy_file %s=======' % copy_file_name)
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[index - 1].click()
        self.find_element(*self.filework_pop_copy).click()
        if not self.exist("//*[@resource-id='com.yozo.office:id/tv_title'][@text='%s']" % rename):
            self.find_element(*self.copy_btn_new_file).click()
            self.find_element(*self.copy_new_file_rename).send_keys(rename)
            self.find_element(*self.btn_true).click()
        self.find_element(By.XPATH, "//*[@resource-id='com.yozo.office:id/tv_title'][@text='%s']" % rename).click()
        self.find_element(*self.copy_btn_move_true).click()
