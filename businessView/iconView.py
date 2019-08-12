#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from businessView.loginView import LoginView
from businessView.searchView import SearchView
from common.common_fun import Common


class IconView(Common):
    csv_file = '../data/account.csv'

    def multi_select(self):  # 多选
        logging.info('==========multi_select==========')
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        # file_name = ele.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        ele.find_element(By.ID, 'com.yozo.office:id/lay_more').click()  #
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_allcheck').click()  # 点击多选
        logging.info('select all')
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()  # 点击全选

    def multi_select_del(self, type):
        logging.info('===========delete choosed==========')
        time.sleep(2)
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        file_name = ele.find_element(By.XPATH,
                                     '//android.widget.TextView[@resource-id="com.yozo.office:id/tv_title"]').text
        ele.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_check_bottom_del').click()
        if type == 'alldoc':
            self.find_element(By.ID, 'com.yozo.office:id/btn_true').click()  # 点击确定
            return file_name

    def check_multi_select(self):
        logging.info('==========check_multi_select==========')
        num_str = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        if int(num_str) > 0:
            logging.info('multi select suceess')
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()  # 取消全选
            return True
        else:
            logging.error("multi select fail")
            self.getScreenShot("multi select fail")
            return False

    def info_file(self):  # 信息
        logging.info('==========info_file==========')
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[0].click()  # 点击右侧的icon
        self.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_info').click()  # 点击信息

    def check_info_file(self):
        logging.info('==========check_info_file==========')
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc')
        except NoSuchElementException:
            logging.error('info fail')
            self.getScreenShot('info fail')
            return False
        else:
            logging.info('info success')
            return True

    def share_file(self):  # 分享
        logging.info('==========share_file==========')
        self.find_elements(By.ID, 'com.yozo.office:id/lay_more')[0].click()  # 点击右侧的icon
        self.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_share').click()  # 点击分享

    def check_share_file(self):
        logging.info('==========check_share_file==========')
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_share')
        except NoSuchElementException:
            logging.error('share fail')
            self.getScreenShot('share fail')
            return False
        else:
            logging.info('share success')
            return True

    def delete_file(self, type):  # 删除
        logging.info('==========delete_file==========')
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        file_name = ele.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        ele.find_element(By.ID, 'com.yozo.office:id/lay_more').click()  #
        self.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_del').click()  # 点击删除
        if type == 'alldoc':
            self.find_element(By.ID, 'com.yozo.office:id/btn_true').click()  # 点击确定
            return file_name

    def check_delete_file(self, type, file_name):
        logging.info('==========check_delete_file==========')
        if type == 'last':
            return self.get_toast_message('此操作只是将文件从最近列表中删除')
        else:
            sv = SearchView(self.driver)
            sv.search_action(file_name)
            if sv.check_search_action(file_name):
                logging.error('delete fail')
                self.getScreenShot('delete fail')
                return False
            else:
                logging.info('delete success')
                return True

    def mark_remove_star(self):  # 标星
        logging.info('==========mark_remove_star==========')
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        file_name = ele.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        # file_time = ele.find_element(By.ID, 'com.yozo.office:id/tv_time').text #组合名称和时间查找标星，暂时先仅时间
        ele.find_element(By.ID, 'com.yozo.office:id/lay_more').click()  # 点击右侧的icon
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_star').click()  # 点击标星
        return file_name

    def check_mark_star(self, file_name):
        logging.info('==========check_mark_star==========')
        try:
            ele = self.driver.find_element(By.XPATH, '//*[@text="%s"]/..' % file_name)
            ele.find_element(By.ID, 'com.yozo.office:id/iv_star')
        except NoSuchElementException:
            logging.error('file without star')
            self.getScreenShot('file without star')
            return False
        else:
            logging.info("file with star")
            return True

    def upload(self):  # 上传云文档
        logging.info('==========upload==========')
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        ele.find_element(By.ID, 'com.yozo.office:id/lay_more').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_upcloud').click()  # 点击上传
        logging.info('checking having already logined in')
        if self.get_toast_message('请先登录账号'):
            self.find_element(By.ID, 'com.yozo.office:id/ll_bottommenu_my').click()
            logging.info('try login in')
            l = LoginView(self.driver)
            data = l.get_csv_data(self.csv_file, 4)
            l.login_action(data[0], data[1])
            if l.check_login_status():
                self.find_element(By.ID, 'com.yozo.office:id/ll_bottommenu_last').click()
                ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
                ele.find_element(By.ID, 'com.yozo.office:id/lay_more').click()
                self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_upcloud').click()  # 点击上传
            else:
                logging.info('login fail in upload')
                raise
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()

    def check_upload(self):
        logging.info('==========check_upload==========')
        return self.get_toast_message('上传成功')
