#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.webdriver.common.by import By

from businessView.createView import CreateView
from businessView.loginView import LoginView
from common.common_fun import Common


class GeneralView(Common):

    def share_file(self, way):  # 分享way=['wx','qq','ding','mail']
        logging.info('==========share_file==========')
        self.group_button_click('文件')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_share_by_%s' % way).click()

    def export_pdf(self, file_name, save_path):  # 导出pdf
        logging.info('==========export_pdf==========')
        self.group_button_click('文件')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_export_pdf').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_folder').click()
        logging.info('choose save path %s' % save_path)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        if self.get_toast_message('您尚未登录，请登录'):
            l = LoginView(self.driver)
            l.login_action('13915575564', 'zhang199412')
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('file named %s' % file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(file_name)

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_type').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # save

    def check_export_pdf(self):
        logging.info('==========check_export_pdf==========')
        return self.get_toast_message('导出成功')

    def switch_write_read(self):  # 阅读模式与编辑模式切换
        logging.info('==========switch_write_read==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()

    def check_write_read(self):
        logging.info('==========check_write_read==========')
        redo = '//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_undo"]'
        if self.get_element(redo):
            logging.info('edit mode')
            return False
        else:
            logging.info('read mode')
            return True

    def screen_rotate(self, rotate):  # 旋转屏幕
        logging.info('==========screen_rotate==========')
        # allowed_values = ['LANDSCAPE', 'PORTRAIT']
        self.driver.orientation = rotate

    def check_rotate(self):
        logging.info('==========check_rotate==========')
        f_width = self.driver.get_window_size()['width']
        print(f_width)
        self.screen_rotate('LANDSCAPE')
        s_width = self.driver.get_window_size()['height']
        print(s_width)
        if f_width == s_width:
            return True
        else:
            return False

    def undo_option(self):  # 撤销
        logging.info('==========undo_option==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo').click()

    def redo_option(self):  # 重做
        logging.info('==========redo_option==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_redo').click()

    def check_undo_redo_event(self):
        logging.info('==========check_undo_redo_event==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo')  # 判断页面是否已切过来

        logging.info('capture before undo')
        self.getScreenShot4Compare('before_undo')

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_app_frame_office_view_container').click()
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=48)
        self.driver.press_keycode(keycode=47)
        self.driver.press_keycode(keycode=47)

        logging.info('capture before redo')
        self.getScreenShot4Compare('before_redo')
        self.undo_option()  # 此处的undo在截图中undo未完全成功，程序进度需要调整
        time.sleep(5)

        logging.info('capture after undo')
        self.getScreenShot4Compare('after_undo')
        self.redo_option()

        time.sleep(5)
        logging.info('capture after redo')
        self.getScreenShot4Compare('after_redo')

        result1 = self.compare_pic('before_undo.png', 'after_undo.png')
        result2 = self.compare_pic('before_redo.png', 'after_redo.png')
        return result1, result2
