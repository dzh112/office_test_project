#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from common.common_fun import Common
from common.tool import get_project_path


class OpenView(Common):

    def open_file(self, file_name):
        logging.info('======test_open_action=====')
        self.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()  # 点击搜索功能
        self.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(file_name)  # 输入搜索内容
        self.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        self.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % file_name).click()  # 打开对应文件
        self.driver.implicitly_wait(10)

    def check_open_status(self, sheet_name):
        logging.info('======test_open_status=====')
        try:
            # 查找指定元素判断是否加载成功
            self.find_element(By.XPATH, "//*[@resource-id='com.yozo.office:id/yozo_ui_option_group_button']").click()
        except NoSuchElementException:
            logging.error('open Fail!')
            self.getScreenShot('open fail' + sheet_name)
            return False
        else:
            logging.info('open success!')
            return True
