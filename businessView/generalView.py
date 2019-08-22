#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.webdriver.common.by import By

from businessView.createView import CreateView
from businessView.loginView import LoginView
from common.common_fun import Common


class GeneralView(Common):

    def font_color(self):  # 字体颜色
        logging.info('==========font_color==========')
        color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_color"]/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, color_index).click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()

    def font_color_custom(self):  # 自定义字体颜色，暂时无用
        logging.info('==========font_color_custom==========')
        color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_color"]/com.yozo.office:id/yozo_ui_ss_option_id_font_color[6]'
        self.driver.find_element(By.XPATH, color_index).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_id_color_others').click()

    def font_style(self, style):  # 加粗，倾斜，划掉，下划线
        logging.info('==========font_style==========')
        style_dict = {'加粗': '0', '倾斜': '1', '删除线': '2', '下划线': '3'}
        style_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_style"]/android.widget.FrameLayout[@index="%s"]' % \
                      style_dict[style]
        self.driver.find_element(By.XPATH, style_index).click()

    def font_name(self):  # 字体类型选择，目前只取系统自带选项的第一个
        logging.info('==========font_name==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_font_name').click()
        time.sleep(1)
        self.driver.swipe(200, 1800, 200, 1180)
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/system_font_names"]/android.widget.RelativeLayout[4]').click()

    def font_size(self, size):  # 字体大小
        logging.info('==========font_size: %s==========' % size)
        font_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_recycler_view"]/android.widget.TextView[@index="1"]'
        font = int(self.get_element(font_ele).text)
        if size != font:
            if size < font:
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
            else:
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
            self.font_size(size)

    def fold_expand(self):
        logging.info('==========fold_expand==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()

    def search_content(self, content):  # 查找内容
        logging.info('==========search_content==========')
        setting_btn = '//*[@resource-id="com.yozo.office:id/yozo_ui_iv_find_replace_switch"]'
        if self.get_element_result(setting_btn):
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_find_replace_switch').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/rb_find').click()
        else:
            self.group_button_click('查看')
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_ll_find').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_et_find_content').set_text(content)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_icon_search').click()

    def replace(self, replace, num='one'):
        logging.info('==========replace==========')
        if not self.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_iv_replace_one"]'):
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_find_replace_switch').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/rb_replace').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_et_replace_content').set_text(replace)
        if num == 'one':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_replace_one').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_tv_replace_all').click()

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
        if self.get_element_result(redo):
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
