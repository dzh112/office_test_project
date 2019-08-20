#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.webdriver.common.by import By
from common.common_fun import Common


class GeneralView(Common):

    def switch_write_read(self):
        logging.info('==========switch_write_read==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()

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
        logging.info('==========create_file_wp==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_main').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_wp').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/iv_gv_image')[0].click()
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
