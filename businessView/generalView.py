#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time
from selenium.webdriver.common.by import By
from businessView.createView import CreateView
from businessView.loginView import LoginView
from common.common_fun import Common


class GeneralView(Common):

    def shape_content_align(self, type, horizontal='左对齐', vertical='上对齐'):
        logging.info('==========cell_align: %s_%s==========' % (horizontal, vertical))
        align_dict = {'左对齐': '1', '水平居中': '2', '右对齐': '3', '上对齐': '4', '垂直居中': '5', '下对齐': '6'}
        style_index1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_text_align"]' \
                       '/android.widget.FrameLayout[%s]' % (type, align_dict[horizontal])
        style_index2 = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_text_align"]' \
                       '/android.widget.FrameLayout[%s]' % (type, align_dict[vertical])
        self.driver.find_element(By.XPATH, style_index1).click()
        self.driver.find_element(By.XPATH, style_index2).click()

    def shape_insert(self, type, index=0, s_index=0):  # 通用插入
        logging.info('======insert_shape======')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_insert"]'
                                           '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            eleA = '//*[@text="最近使用"]'
            eleB = '//*[@text="基本形状"]'
            if self.get_element_result(eleA):
                self.swipe_ele(eleB, eleA)
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more_shape'
                                             '_main_container"]/android.widget.FrameLayout')
            if len(eles) < s_index:
                time.sleep(0.5)
                self.swipe_ele1(eles[-1], eles[0])
                time.sleep(0.5)
                eles = self.driver.find_elements(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more'
                                                           '_shape_main_container"]/android.widget.FrameLayout')
                eles[s_index - 19].click()
            else:
                eles[s_index - 1].click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_layer(self, lay='置于顶层'):  # 图形叠放次序
        logging.info('======shape_layer======')
        lay_dict = {'上移一层': '1', '置于顶层': '2', '下移一层': '3', '置于底层': '4'}
        self.driver.find_element(By.XPATH, '//*[@text="叠放次序"]').click()
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]' %
                                 lay_dict[lay]).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_effect_type(self, type, index=1, shadow=8, three_d=8):  # 边框效果
        logging.info('======shape_effect_type======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_effect_type"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            self.driver.find_element(By.XPATH,
                                     '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_shadow"]/android.widget.FrameLayout[%s]' % shadow).click()
            if self.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_3d"]'):
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_3d"]/android.widget.FrameLayout[%s]' % three_d).click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_border_width(self, type, index=1, size=1):  # 边框粗细size=1-30
        logging.info('======shape_border_width======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_border_width"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            for i in range(60):
                font_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_recycler_view"]/android.widget.TextView[@index="1"]'
                font = int((self.get_element(font_ele).text)[:-2])
                if size != font:
                    if size < font:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
                    else:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
                else:
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
                    break

    def shape_border_type(self, type, index=1, s_index=1):  # 边框格式
        logging.info('======shape_boeder_type======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_border_type"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_shape_border_type"]/android.widget.FrameLayout')
            eles[s_index - 1].click()
            time.sleep(0.5)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_border_color(self, type, index=1, s_index=0):  # 边框颜色
        logging.info('======shape_border_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_border_color"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]/android.widget.FrameLayout')
            eles[s_index - 1].click()
            time.sleep(0.5)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_fill_color_transparency(self, transparency=0):  # 0-100
        logging.info('======shape_fill_color_transparency======')
        eles = self.driver.find_elements(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]/android.widget.FrameLayout')
        self.swipe_ele1(eles[-1], eles[0])
        seekbar = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_seekbar').rect
        x, y, width, height = int(seekbar['x']), int(seekbar['y']), int(seekbar['width']), int(seekbar['height'])
        for i in range(x, x + width, 6):
            display = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_seekbar_display').text
            display_num = int(display[:-1])
            if transparency == display_num:
                break
            else:
                self.tap(i, y)
                time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_fill_color(self, type, index, s_index=36):
        logging.info('======shape_fill_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_fill_color"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index == 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]/android.widget.FrameLayout')
            if len(eles) < 42 and len(eles) > 0:
                self.swipe_ele1(eles[0], eles[-1])
            eles[s_index - 1].click()
            time.sleep(0.5)
            # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_option(self, type, index, width=3.81, height=3.81, top=0.13, bottom=0.13, left=0.25,
                     right=0.25):  # 旋转、镜像、剪切
        logging.info('======shape_option======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index == 5:
            width_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_width')
            width_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(width))
            height_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_height')
            height_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(height))
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.group_button_click('形状')
        if index == 6:
            top_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_top')
            top_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(top))
            bottom_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_bottom')
            bottom_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(bottom))
            left_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_left')
            left_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(left))
            eleA = '//*[@text="左边距(单位:厘米)"]'
            eleB = '//*[@text="上边距(单位:厘米)"]'
            self.swipe_ele(eleA, eleB)
            right_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_right')
            right_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(right))
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.group_button_click('形状')

    def pen_size(self, type, index):  # 签批字粗细 1-6
        logging.info('======pen_size======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_sign_pen_size"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()

    def pen_color(self, type, index=41):  # 签批颜色 1-42
        logging.info('======pen_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_sign_pen_color"]/android.widget.FrameLayout[6]' % type).click()
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]' % index).click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def pen_type(self, type, pen='钢笔'):  # 钢笔、荧光笔、擦除
        logging.info('======pen_type======')
        pen_list = ['钢笔', '荧光笔', '擦除']
        index = pen_list.index(pen) + 1
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_sign_pen_type"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()

    def use_finger(self, type):  # 是否使用手指
        logging.info('======use_finger======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_sign_use_finger' % type).click()

    def insert_shape(self, type, index=0, s_index=0):  # 通用插入
        logging.info('======insert_shape======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eleA = '//*[@text="最近使用"]'
            eleB = '//*[@text="基本形状"]'
            self.swipe_ele(eleB, eleA)
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more_shape_main_container"]/android.widget.FrameLayout')
            if len(eles) < s_index:
                time.sleep(0.5)
                self.swipe_ele1(eles[-1], eles[0])
                time.sleep(0.5)
                eles = self.driver.find_elements(By.XPATH,
                                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more_shape_main_container"]/android.widget.FrameLayout')
                eles[s_index - 19].click()
            else:
                eles[s_index - 1].click()

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
        time.sleep(5)
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
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo').click()
        time.sleep(1)

    def redo_option(self):  # 重做
        logging.info('==========redo_option==========')
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_redo').click()
        time.sleep(1)

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

    def check_wp_undo(self):
        return self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text == '编辑'

    def check_wp_redo(self):
        return self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text == '形状'
