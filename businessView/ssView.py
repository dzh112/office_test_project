#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.webdriver.common.by import By

from common.common_fun import Common


class SSView(Common):

    def cell_num_style(self):
        logging.info('==========cell_num_style==========')
        num_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_number_format"]/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, num_index).click()
        eles = self.driver.find_elements(By.XPATH,
                                        '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
        for i in eles:
            i.click()
        self.swipe_ele('//*[@text="时间"]', '//*[@text="常规"]')
        eles = self.driver.find_elements(By.XPATH,
                                        '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
        for i in eles:
            i.click()

    def cell_border(self):
        logging.info('==========cell_border==========')
        border_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_border"]/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, border_index).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_color').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_style').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def cell_align(self, horizontal='左对齐', vertical='垂直居中'):
        logging.info('==========cell_align: %s_%s==========' % (horizontal, vertical))
        align_dict = {'左对齐': '0', '水平居中': '1', '右对齐': '2', '上对齐': '3', '垂直居中': '4', '下对齐': '5'}
        style_index1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_align"]/android.widget.FrameLayout[@index="%s"]' % \
                       align_dict[horizontal]
        style_index2 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_align"]/android.widget.FrameLayout[@index="%s"]' % \
                       align_dict[vertical]
        self.driver.find_element(By.XPATH, style_index1).click()
        self.driver.find_element(By.XPATH, style_index2).click()

    def cell_color(self):  # 单元格填充色
        logging.info('==========cell_color==========')
        color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_fill_color"]/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, color_index).click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()

    def unhide_sheet(self, index, index1):  # 取消隐藏
        logging.info('==========unhide_sheet==========')
        self.operate_sheet(index, 'unhide')
        self.driver.find_elements(By.ID, 'com.yozo.office:id/lv_ss_sheet_hide')[index1].click()

    def operate_sheet(self, index,
                      operation):  # sheet操作的公共部分 options=['rename','insert','copy','remove','hide','unhide']
        logging.info('==========operate_sheet_%s==========' % operation)
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index).click()
        if not self.get_element_result('//*[@resource-id="com.yozo.office:id/ll_ss_sheet"]'):
            self.driver.find_element(By.XPATH,
                                     '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_sheet_%s' % operation).click()

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
        self.operate_sheet(index, 'rename')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_office_ss_sheet_rename_text').set_text(name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_office_ss_sheet_rename_ok').click()

    def check_rename_sheet(self, index, name):
        base_ele = self.driver.find_element(By.XPATH,
                                            '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index)
        text_name = base_ele.find_element(By.ID, 'com.yozo.office:id/tv_ss_sheet_name').text
        if text_name == name:
            logging.info('rename success')
            return True
        else:
            logging.error('rename fail')
            self.getScreenShot('rename fail')
            return False
