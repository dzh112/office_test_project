#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.common_fun import Common
from common.tool import *


class SaveView(Common):
    def save_as(self,file_name):
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()  # 点击搜索功能
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(file_name)  # 输入搜索内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % file_name).click()  # 点击第一个文件
        time.sleep(5)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_app_frame_office_view_container')  # 打开文件后的视图
        self.driver.save_screenshot('before_save.png')  # 保存截图
        ele_screenshots(ele, 'before_save.png')  # 截取视图元素
        if self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text == '文件':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()  # 点击功能按钮
            self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="文件"]').click()  # 点击文件选项
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="另存为"]').click()  # 点击另存为
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_folder').click()  # 选择路径
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local').click()  # 点击本地
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(
            'untitledfile')  # 输入文件名
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # 点击保存
        time.sleep(5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()  # 关闭文件
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').set_text('untitledfile')  # 输入搜索内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_title').click()  # 点击第一个文件名
        time.sleep(5)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_app_frame_office_view_container')  # 打开文件后的视图
        self.driver.save_screenshot('after_save.png')  # 保存截图
        ele_screenshots(ele, 'after_save.png')  # 截取视图元素


if __name__ == '__main__':
    pass
    # driver = appium_desired()
    # l = SaveView(driver)
    # print(l.get_data('../data/need_run.csv',2))
