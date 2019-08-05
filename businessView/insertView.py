#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.webdriver.common.by import By

from common.common_fun import Common


class InsertView(Common):

    def create_file(self, types):  # 新建文档\
        logging.info('======create %s file=====' % types)
        self.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_main').click()  # 点击加号
        self.find_element(By.ID, 'com.yozo.office:id/fb_show_menu_%s' % types).click()  # 选择WP
        self.find_element(By.XPATH, '//android.widget.TextView[@text="新建空白"]').click()  # 选择新建

    def save_close(self, types):  # 保存关闭文档
        logging.info('======save and close file=====')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()  # 点击保存
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local').click()  # 选本地
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(
            'test_insert_%s' % types)  # 清空输入test_insert
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # 点击保存
        # self.driver.switch_to.alert.accept() #弹出框默认允许
        try:
            if self.driver.find_element(By.ID, 'android:id/content').is_displayed():
                self.find_element(By.ID, 'android:id/button1').click()
        except Exception:
            print('弹出框捕捉失败')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()  # 点击关闭

    def insert_common(self, types):  # 通用插入
        logging.info('======insert common function======')
        if self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text == '插入':
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()
        else:
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()  # 点击功能按钮
            self.find_element(By.XPATH, '//android.widget.TextView[@text="插入"]').click()  # 点击插入选项
        if types == 'wp':
            pic_id = 'com.yozo.office:id/yozo_ui_wp_option_id_pick_image'  # WP中图片ID
        elif types == 'ss':
            pic_id = 'com.yozo.office:id/yozo_ui_ss_option_id_insert_picture'  # SS中图片ID
        else:
            pic_id = 'com.yozo.office:id/yozo_ui_pg_option_id_insert_picture'  # PG中图片ID
        self.find_element(By.ID, pic_id).click()  # 点击插入图片
        self.driver.tap([(530, 1320)], 100)
        time.sleep(1)
        self.driver.tap([(510, 1030)], 100)
        time.sleep(1)
        self.find_element(By.ID, 'com.android.gallery3d:id/filtershow_done').click()  # 图片保存
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="插入"]').click()
        base_shape = '//*[@resource-id="com.yozo.office:id/yozo_ui_' + types + '_option_id_insert_shape"]/android.widget.FrameLayout[1]'
        # 'com.yozo.office:id/yozo_ui_ss_option_id_insert_shape'
        self.find_element(By.XPATH, base_shape).click()  # 点击，后跳转至形状
        expand_all_again = '//*[@resource-id="com.yozo.office:id/yozo_ui_' + types + '_option_id_shape_insert"]/android.widget.FrameLayout[6]'
        self.find_element(By.XPATH, expand_all_again).click()  # 点击形状中插入内展开全部选项
        base_shapes = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more_shape_main_container"]/android.widget.FrameLayout'
        # 'com.yozo.office:id/yozo_ui_option_id_more_shape_main_container'
        # 代码需要优化
        base_elements = self.find_elements(By.XPATH, base_shapes)  # 获取元素组
        # map(lambda ele:ele.click(),base_elements)
        for ele in base_elements:
            ele.click()
        self.driver.swipe(915, 1875, 915, 1559)  # 滑屏
        base_elements = self.find_elements(By.XPATH, base_shapes)  # 获取元素组
        for ele in base_elements[18:]:
            ele.click()
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()  # 返回
        # self.driver.keyevent(4)

    def swipe_ss(self, ele1, str, last_id=''):  # SS图表插入滑动点击
        start = 0
        # 定位元素组
        elements = self.find_elements(By.XPATH, ele1)
        first_id = elements[0].get_attribute("resourceId")
        last_ids = elements[-1].get_attribute("resourceId")
        y_first = elements[0].location['y']  # 第一个元素的y坐标
        x_last = elements[-1].location['x']  # 最后一个元素的x坐标
        y_last = elements[-1].location['y']  # 最后一个元素的y坐标
        if first_id != str:
            for index, ele in enumerate(elements):
                if ele.get_attribute("resourceId") == last_id:
                    if index != len(elements) - 1:
                        start = index + 1
                        break
                    else:
                        return
        for ele in elements[start:]:
            ele.click()
            sub_eles = self.find_elements(By.XPATH,
                                          '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
            for sub_ele in sub_eles:
                sub_ele.click()
                try:
                    if self.driver.find_element(By.ID, 'android:id/customPanel').is_displayed():
                        self.driver.keyevent(4)
                except Exception:
                    print(Exception)
            self.driver.keyevent(4)
        time.sleep(1)
        self.driver.swipe(x_last, y_last, x_last, y_first, 1800)
        self.swipe_ss(self, ele1, str, last_ids)

    def insert_SS(self):
        logging.info('======insert_SS=====')
        ele = self.find_element(By.XPATH,
                                '//*[@resource-id="com.yozo.office:id/yozo_ss_frame_table_container"]/android.view.View/android.view.View')
        x = ele.location['x'] + ele.size['width'] / 2
        y = ele.location['y'] + ele.size['height'] / 2
        self.driver.tap([(x, y)], 100)  # 点击中心的单元格
        self.find_element(By.ID, 'com.yozo.office:id/formulabar_edit_container').click()
        self.driver.keyevent(9)
        self.driver.keyevent(10)
        self.driver.keyevent(10)
        self.driver.keyevent(10)
        self.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="插入"]').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="图表"]').click()  # 点击插入图表
        # self.driver.implicitly_wait(5) #隐性等待
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_chart_type_0').click()  # 点击插入柱状图
        self.find_element(By.XPATH,
                          '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]').click()  # 点击插入图表
        self.find_element(By.XPATH, '//android.widget.TextView[@text="图表类型"]').click()  # 点击图表类型
        type_base_mark = '//android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout'
        first_id = 'com.yozo.office:id/yozo_ui_ss_option_id_chart_type_0'
        self.swipe_ss(self, type_base_mark, first_id)
        self.driver.keyevent(4)

    def insert_WP(self):  # WP插入特殊部分
        logging.info('======insert_WP=====')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="插入"]').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="水印"]').click()  # 点击插入水印
        self.find_element(By.ID, 'com.yozo.office:id/et_water_mark').send_keys('YOZO')  # 输入YOZO
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()  # 点击确定

    def insert_PG(self):
        logging.info('======insert_PG=====')
        # 插入幻灯片
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="插入"]').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="幻灯片"]').click()
        # 插入备注
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="插入"]').click()
        self.find_element(By.XPATH, '//android.widget.TextView[@text="备注"]').click()
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_et').set_text("YOZO")
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_ok').click()  # 点击确定
        self.find_element(By.XPATH, "//*[@class='android.widget.Button']").click()
        ppt_remarks = self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_note_body_show_note').text
        self.driver.keyevent(4)
