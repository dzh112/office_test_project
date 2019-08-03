#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.saveView import SaveView
from common.common_fun import Common
from common.desired_caps import appium_desired
from common.myunit import StartEnd

@ddt
class TestSaveAs(StartEnd):

    script_file = '../data/need_run.csv'

    def get_info(self):
        data = SaveView(self.driver).get_csv_data(self.script_file, 1)
        data_list = SaveView(self.driver).get_data(data[0],data[1],data[2],data[3])
        return data_list

    data_list = get_info()
    @data(*data_list)
    def test_save_as(self,file_name):
        logging.info('======test_save_as=====')
        s = SaveView(self.driver)
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()  # 点击搜索功能
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(file_name)  # 输入搜索内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % file_name).click()  # 点击第一个文件
        # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()  # 切换只读
        # time.sleep(3)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_app_frame_office_view_container')  # 打开文件后的视图
        self.driver.driver.save_screenshot('before_save.png')  # 保存截图
        s.ele_screenshots(ele, 'before_save.png')  # 截取视图元素
        if self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text == '文件':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()  # 点击功能按钮
            self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="文件"]').click()  # 点击文件选项
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="另存为"]').click()  # 点击另存为
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_folder').click()  # 选择路径
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local').click()  # 点击本地
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').clear()  # 清除输入框内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').send_keys(
            'untitledfile')  # 输入文件名
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # 点击保存
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()  # 点击expand按钮
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()  # 关闭文件
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').clear()  # 清除输入框内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys('untitledfile')  # 输入搜索内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_title').click()  # 点击第一个文件名
        # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()  # 切换只读
        # time.sleep(3)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_app_frame_office_view_container')  # 打开文件后的视图
        self.driver.driver.save_screenshot('after_save.png')  # 保存截图
        s.ele_screenshots(ele, 'after_save.png')  # 截取视图元素
        result = s.image_contrast()  # 获取图片误差
        try:
            self.driver.assertLess(result, 2000, '实际误差为%s' % result)  # 确认误差是否符合需求
        except Exception:
            s.img_unite(self.driver)
            raise

if __name__ == '__main__':
    # unittest.main()
    driver = appium_desired()
    list = TestSaveAs.get_info(driver)
    print(list)
