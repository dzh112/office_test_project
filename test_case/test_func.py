#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import random
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.pgView import PGView
from businessView.ssView import SSView
from businessView.wpView import WPView
from common.myunit import StartEnd

share_list = ['wp_wx', 'wp_qq', 'wp_ding', 'wp_mail', 'ss_wx', 'ss_qq', 'ss_ding',
              'ss_mail', 'pg_wx', 'pg_qq', 'pg_ding', 'pg_mail']
wps = ['wp', 'ss', 'pg']
wp = ['wp', 'pg']
ws = ['wp', 'ss']
search_dict = {'wp': 'docx', 'ss': 'xlsx', 'pg': 'pptx'}
switch_list = ['无切换', '平滑淡出', '从全黑淡出', '切出', '从全黑切出', '溶解', '向下擦除', '向左擦除', '向右擦除',
               '向上擦除', '扇形展开', '从下抽出', '从左抽出', '从右抽出', '从上抽出', '从左下抽出', '从左上抽出',
               '从右下抽出', '从右上抽出', '盒状收缩', '盒状展开', '1根轮辐', '2根轮辐', '3根轮辐', '4根轮辐', '8根轮辐',
               '上下收缩', '上下展开', '左右收缩', '左右展开', '左下展开', '左上展开', '右下展开', '右上展开', '圆形',
               '菱形', '加号', '新闻快报', '向下推出', '向左推出', '向右推出', '向上推出', '向下插入', '向左插入',
               '向右插入', '向上插入', '向左下插入', '向左上插入', '向右下插入', '向右上插入', '水平百叶窗',
               '垂直百叶窗', '横向棋盘式', '纵向棋盘式', '水平梳理', '垂直梳理', '水平线条', '垂直线条', '随机']


@ddt
class TestFunc(StartEnd):

    # # @unittest.skip('skip test_wp_check_approve')
    def test_wp_check_approve(self):  # 修订
        logging.info('==========test_wp_check_approve==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('审阅')
        wp.change_name('super_root')
        wp.group_button_click('审阅')
        wp.revision_on_off('开启')
        wp.tap(450, 550)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('审阅')
        wp.revision_accept_not('yes')
        wp.tap(450, 550)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('审阅')
        wp.revision_accept_not()
        wp.group_button_click('审阅')
        wp.revision_on_off('关闭')
        time.sleep(3)

    # @unittest.skip('skip test_wp_insert_watermark')
    def test_wp_insert_watermark(self):
        logging.info('==========test_wp_insert_watermark==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.insert_watermark('YOZO')
        time.sleep(1)
        wp.group_button_click('插入')
        wp.insert_watermark('yozo', delete='delete')
        time.sleep(3)

    # @unittest.skip('skip test_wp_font_attr')
    def test_wp_font_attr(self):
        logging.info('==========test_wp_font_attr===========')
        cv = CreateView(self.driver)
        type = 'wp'
        cv.create_file(type)
        time.sleep(1)
        wp = WPView(self.driver)
        wp.group_button_click('编辑')
        wp.font_size(16)
        # wp.font_name(type)
        wp.font_style(type, '倾斜')
        wp.font_color(type, 3)
        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ele3 = '//*[@text="高亮颜色"]'
        ele4 = '//*[@text="分栏"]'
        wp.swipe_ele(ele2, ele1)
        time.sleep(1)
        wp.tap(450, 450)
        for i in range(100):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('编辑')
        wp.drag_coordinate(450, 500, 200, 500)
        wp.high_light_color(type, 3)
        wp.bullets_numbers(type, 6, 14)
        wp.text_align(type, '右对齐')
        wp.swipe_ele(ele3, ele1)
        wp.text_line_space(type, 2.5)
        wp.text_indent(type, '右缩进')
        wp.swipe_ele(ele4, ele1)
        wp.text_columns(4)
        wp.text_columns(3)
        wp.text_columns(2)
        time.sleep(3)

    # @unittest.skip('skip test_wp_jump')
    def test_wp_jump(self):  # 跳转页
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.group_button_click('查看')
        wp.page_jump(7)
        time.sleep(2)

    # @unittest.skip('skip test_wp_bookmark')
    def test_wp_bookmark(self):
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.group_button_click('查看')
        wp.add_bookmark('test')
        self.assertTrue(wp.check_add_bookmark(), '书签插入失败！')
        wp.swipeUp()
        wp.swipeUp()
        wp.group_button_click('查看')
        wp.list_bookmark('test')

    # @unittest.skip('skip test_wp_text_select')
    def test_wp_text_select(self):  # 文本选取
        logging.info('==========test_wp_text_select==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.switch_write_read()
        x, y = wp.get_size()
        wp.drag_coordinate(x * 0.5, y * 0.4, x * 0.6, y * 0.5)
        time.sleep(3)

    # @unittest.skip('skip test_wp_read_self_adaption')
    def test_wp_read_self_adaption(self):  # wp阅读自适应
        logging.info('==========test_wp_read_self_adaption==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.read_self_adaption()
        time.sleep(1)
        self.assertFalse(wp.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                         'read self adaption set fail!')

    # @unittest.skip('skip test_ppt_play_switch')
    @data(*switch_list)
    def test_ppt_play_switch(self, switch):  # 幻灯片切换
        logging.info('==========test_ppt_play_switch==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')
        pg = PGView(self.driver)
        pg.switch_write_read()

        pg.group_button_click('切换')
        pg.switch_mode(switch, 'all')
        pg.group_button_click('播放')
        pg.play_mode()
        time.sleep(20)

    # @unittest.skip('skip test_ppt_play')
    def test_ppt_play(self):  # ppt播放
        logging.info('==========test_ppt_play==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')
        pg = PGView(self.driver)
        pg.group_button_click('播放')
        pg.play_mode('first')
        x, y = pg.get_size()

        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        pg.quit_play()
        # pg.screen_rotate('PORTRAIT')
        # pg.group_button_click('播放')
        pg.play_mode('current')
        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        pg.quit_play()
        # pg.screen_rotate('PORTRAIT')
        # pg.group_button_click('播放')
        pg.swipeRight()
        pg.swipeRight()
        pg.swipeRight()
        pg.play_mode('autoplay')
        time.sleep(2)
        pg.pause_resume_play()
        time.sleep(1)
        pg.pause_resume_play()
        time.sleep(20)
        # pg.screen_rotate('PORTRAIT')

    # @unittest.skip('skip test_ppt_template')
    def test_ppt_template(self):
        logging.info('==========test_ppt_template==========')
        cv = CreateView(self.driver)
        cv.create_file('pg')
        pg = PGView(self.driver)
        pg.group_button_click('编辑')
        for i in range(11):
            pg.edit_template(i)
        time.sleep(3)

    # @unittest.skip('skip test_ppt_format')
    def test_ppt_format(self):
        logging.info('==========test_ppt_format==========')
        format = ['标题与副标题', '标题', '标题与文本', '标题与两栏文本', '标题与竖排文本-上下', '标题与竖排文本-左右',
                  '空白', '标题与图片', '标题、文本与图片', '标题、图片与文本', '标题、图片与竖排文本', '标题、竖排文本与图片']
        cv = CreateView(self.driver)
        cv.create_file('pg')
        pg = PGView(self.driver)
        pg.group_button_click('编辑')
        for i in format:
            pg.edit_format(i)
        time.sleep(3)

    # @unittest.skip('skip test_ppt_add_scroll_comment')
    def test_ppt_add_scroll_comment(self):  # ppt缩略图滚屏备注
        logging.info('==========test_ppt_add_scroll_comment==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')
        pg = PGView(self.driver)
        pg.switch_write_read()
        pg.add_new()
        pg.add_comment(5, 'test2')
        pg.add_new()
        pg.check_comment(5)
        pg.edit_comment('TEST')
        pg.add_new()
        pg.check_comment(5)
        pg.delete_comment()
        time.sleep(1)

    # @unittest.skip('skip test_shape_text_attr_pg')
    def test_shape_text_attr_pg(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========test_shape_text_attr_pg==========')
        type = 'pg'
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        gv.group_button_click('编辑')
        gv.font_name(type, 'AndroidClock')
        gv.font_size(15)
        gv.font_style(type, '倾斜')
        gv.font_color(type, 6, 29)
        gv.swipe_ele('//*[@text="字体颜色"]', '//*[@text="编辑"]')
        time.sleep(1)
        gv.tap(550, 450)
        time.sleep(1)
        gv.tap(550, 450, 6)
        time.sleep(1)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        time.sleep(1)
        gv.group_button_click('编辑')
        # gv.high_light_color(type,6,6)
        gv.bullets_numbers(type, 6, 10)
        gv.text_align(type, '分散对齐')
        gv.text_align(type, '右对齐')
        gv.text_line_space(type, 1.5)
        gv.text_line_space(type, 3)
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '左缩进')
        time.sleep(3)

    # @unittest.skip('skip test_shape_text_attr_wp')
    def test_shape_text_attr_wp(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========test_shape_text_attr_wp==========')
        type = 'wp'
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        # if type == 'wp':
        gv.tap(700, 767, 5)
        gv.tap(700, 767, 6)
        # else:
        #     gv.tap(550, 450)
        #     time.sleep(1)
        #     gv.tap(550, 450, 6)
        time.sleep(1)
        gv.group_button_click('编辑')
        gv.font_name(type, 'AndroidClock')
        gv.font_size(15)
        gv.font_style(type, '倾斜')
        gv.font_color(type, 6, 29)
        gv.swipe_ele('//*[@text="字体颜色"]', '//*[@text="编辑"]')
        time.sleep(1)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        time.sleep(1)
        gv.swipe_ele('//*[@text="高亮颜色"]', '//*[@text="编辑"]')
        # gv.high_light_color(type,6,6)
        gv.bullets_numbers(type, 6, 10)
        gv.text_align(type, '分散对齐')
        gv.text_align(type, '右对齐')
        gv.text_line_space(type, 1.5)
        gv.text_line_space(type, 3)
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '左缩进')
        time.sleep(3)

    # @unittest.skip('skip test_shape_attr1')
    @data(*wps)
    def test_shape_attr1(self, type):
        logging.info('==========test_shape_attr1==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        time.sleep(1)
        if type == 'pg':
            gv.tap(550, 450, 3)  # 双击进入编辑
            gv.tap(550, 450, 4)  # 双击进入编辑
        else:
            gv.tap(700, 767, 3)  # 双击进入编辑
            gv.tap(700, 767, 4)  # 双击进入编辑
        for i in range(50):
            self.driver.press_keycode(random.randint(7, 16))
        gv.group_button_click('编辑')

        if type == 'wp':
            time.sleep(1)
            gv.tap(250, 250)
            time.sleep(1)
            gv.tap(700, 767)
            time.sleep(1)
            gv.group_button_click('形状')
        elif type == 'pg':
            time.sleep(1)
            gv.tap(250, 250)
            time.sleep(1)
            gv.tap(550, 680)

        gv.shape_option(type, 5, width=5, height=5)
        gv.shape_option(type, 6, top=0.5, bottom=0.5, left=0.5, right=0.5)
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]' % type
        ele2 = '//*[@text="轮廓"]'
        ele3 = '//*[@text="效果"]'
        gv.swipe_ele(ele2, ele1)
        gv.swipe_ele(ele3, ele2)
        gv.shape_content_align(type, '右对齐', '下对齐')
        gv.shape_content_align(type)
        gv.shape_content_align(type, '水平居中', '垂直居中')
        time.sleep(3)

    # @unittest.skip('skip test_shape_attr')
    @data(*wps)
    def test_shape_attr(self,type):
        logging.info('==========test_shape_attr==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 6, 30)
        gv.shape_insert(type, 6, 31)
        gv.shape_insert(type, 6, 32)
        gv.shape_insert(type, 6, 33)
        gv.shape_option(type, 2)
        gv.shape_fill_color(type, 6, 24)
        gv.shape_fill_color_transparency(5)
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]'%type
        ele2 = '//*[@text="轮廓"]'
        gv.swipe_ele(ele2, ele1)
        gv.shape_border_color(type, 6, 5)
        gv.shape_border_type(type, 6, 3)
        gv.shape_border_width(type, 6, 20)
        ele3 = '//*[@text="效果"]'
        gv.swipe_ele(ele3, ele2)
        gv.shape_effect_type(type, 6, 4, 5)
        gv.shape_layer('下移一层')
        gv.shape_layer('置于底层')
        gv.shape_layer('上移一层')
        gv.shape_layer('置于顶层')
        time.sleep(3)

    # @unittest.skip('skip test_signature')
    @data(*wps)
    def test_signature(self, type):  # 签批
        logging.info('==========test_signature==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('签批')
        gv.use_finger(type)
        gv.use_finger(type)
        gv.pen_type(type, '钢笔')
        gv.pen_color(type, 15)
        gv.pen_size(type, 3)
        gv.swipe(300, 400, 800, 400, 500)
        gv.pen_type(type, '荧光笔')
        gv.pen_color(type, 30)
        gv.pen_size(type, 6)
        gv.swipe(300, 600, 800, 600, 500)
        gv.pen_type(type, '擦除')
        gv.swipe(200, 400, 900, 400, 500)
        gv.swipe(200, 600, 900, 600, 500)
        time.sleep(3)

    # @unittest.skip('skip test_formula1')
    def test_formula1(self):  # 其他类型公式
        logging.info('==========test_formula1==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        for i in range(10):
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))  # 双击进入编辑
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
            self.driver.press_keycode(random.randint(7, 16))
        ss = SSView(self.driver)

        cv.tap(110 + 263 * 2.5, 295 + 55 * 11.5)
        ss.formula_all('最近使用', 'ABS')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 1.5)
        ss.formula_all('数学和三角', 'ABS')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 2.5)
        ss.formula_all('财务', 'DOLLARDE')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        time.sleep(0.5)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 5.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 3.5)
        ss.formula_all('逻辑', 'AND')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        time.sleep(0.5)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 5.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 4.5)
        ss.formula_all('文本', 'ASC')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 5.5)
        ss.formula_all('日期和时间', 'NOW')
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 6.5)
        ss.formula_all('查找与引用', 'COLUMN')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 7.5)
        ss.formula_all('统计', 'AVERAGE')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        # cv.tap(110 + 263 * 2.5, 295 + 55 * 8.5)
        # ss.formula_all('工程', 'DEC2BIN')
        # cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        # self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 9.5)
        ss.formula_all('信息', 'ISBLANK')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 10.5)
        ss.formula_all('所有公式', 'ABS')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    # @unittest.skip('skip test_formula')
    def test_formula(self):
        logging.info('==========test_formula==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        for i in range(10):
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))  # 双击进入编辑
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
            self.driver.press_keycode(random.randint(7, 16))
        ss = SSView(self.driver)

        cv.tap(110 + 263 * 2.5, 295 + 55 * 1.5)  # 求和
        ss.auto_sum('求和')
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 2.5)  # 平均值
        ss.auto_sum('平均值')
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 3.5)  # 计数
        ss.auto_sum('计数')
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 4.5)  # 最大值
        ss.auto_sum('最大值')
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 5.5)  # 最小值
        ss.auto_sum('最小值')
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        time.sleep(3)

    # @unittest.skip('skip test_data_table')
    def test_data_table(self):  # 数据排序，工作表格式
        logging.info('==========test_data_table==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))  # 双击进入编辑
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
            self.driver.press_keycode(random.randint(7, 16))
        ss = SSView(self.driver)
        ss.group_button_click('查看')
        time.sleep(1)
        ss.data_sort('降序')
        ss.data_sort('升序')
        ss.sheet_style('隐藏编辑栏')
        ss.sheet_style('隐藏编辑栏')
        ss.sheet_style('隐藏表头')
        ss.sheet_style('隐藏表头')
        ss.sheet_style('隐藏网格线')
        ss.sheet_style('冻结窗口')
        ss.sheet_style('取消冻结')
        ss.sheet_style('100%')
        time.sleep(3)

    # @unittest.skip('skip test_insert_shape')
    @data(*wps)
    def test_insert_shape(self, type):
        logging.info('==========test_insert_shape==========')
        cv = CreateView(self.driver)
        cv.create_file(type)

        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        # ss.insert_chart()
        gv.group_button_click('插入')
        gv.insert_shape(type)
        for i in range(42):
            gv.shape_insert(type, 6, i)
        time.sleep(3)

    # @unittest.skip('skip test_table_style')
    def test_table_style(self):  # 表格样式
        logging.info('==========test_table_style==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        cv.drag_coordinate(110 + 263 * 2, 295 + 55 * 2, 110 + 263 * 3, 295 + 55 * 4)
        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_name"]'
        ele2 = '//*[@text="单元格填充"]'
        ele3 = '//*[@text="数字格式"]'
        ele4 = '//*[@text="插入单元格"]'
        ele5 = '//*[@text="设置行高列宽"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele2)
        ss.swipe_ele(ele4, ele3)
        ss.swipe_ele(ele5, ele4)
        ss.table_style()

    # @unittest.skip('skip test_cell_inser_delete_fit')
    def test_cell_inser_delete_fit(self):  # 插入删除行宽列高清除
        logging.info('==========test_cell_inser_delete_fit==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        gv = GeneralView(self.driver)
        gv.font_style(type, '删除线')

        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_name"]'
        ele2 = '//*[@text="单元格填充"]'
        ele3 = '//*[@text="数字格式"]'
        ele4 = '//*[@text="插入单元格"]'
        ele5 = '//*[@text="设置行高列宽"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele2)
        ss.swipe_ele(ele4, ele3)
        ss.cell_insert('右移')
        ss.cell_insert('下移')
        ss.cell_insert('插入整行')
        ss.cell_insert('插入整列')
        ss.cell_delete('删除整列')
        ss.cell_delete('删除整行')
        ss.cell_delete('上移')
        ss.cell_delete('左移')
        ss.cell_set_size(5, 5)
        ss.group_button_click('编辑')
        ss.cell_clear('清除格式')
        gv.undo_option()
        ss.cell_clear('清除内容')
        gv.undo_option()
        ss.cell_clear('清除所有')
        gv.undo_option()
        ss.swipe_ele(ele4, ele5)
        ss.cell_fit_height()
        ss.cell_fit_width()
        time.sleep(3)

    # @unittest.skip('skip test_merge_wrap')
    def test_merge_wrap(self):
        logging.info('==========test_merge_wrap==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        cv.drag_coordinate(110 + 263 * 2, 295 + 55 * 2, 110 + 263 * 3, 295 + 55 * 2)

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_name"]'
        ele2 = '//*[@text="单元格填充"]'
        ele3 = '//*[@text="数字格式"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele2)
        ss.cell_merge_split()
        ss.cell_merge_split()
        ss.cell_auto_wrap()
        ss.cell_auto_wrap()
        time.sleep(3)

    # @unittest.skip('skip test_num_style')
    def test_num_style(self):
        logging.info('==========test_num_style==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.press_keycode(15)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_name"]'
        ele2 = '//*[@text="单元格填充"]'
        ele3 = '//*[@text="数字格式"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele2)
        ss.cell_num_style()

    # @unittest.skip('skip test_cell_border')
    def test_cell_border(self):  # 遍历边框所有功能
        logging.info('==========test_cell_border==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        time.sleep(1)
        self.driver.swipe(200, 1856, 200, 1150, 2000)
        ss.cell_border()

    # @unittest.skip('skip test_cell_attr')
    def test_cell_attr(self):
        logging.info('==========test_cell_attr==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        time.sleep(1)
        self.driver.swipe(200, 1856, 200, 1150, 2000)
        ss.cell_align('水平居中', '下对齐')
        # ss.cell_color()

    # @unittest.skip('skip test_font_attr')
    def test_font_attr(self):
        logging.info('==========test_font_attr==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        gv = GeneralView(self.driver)
        gv.group_button_click('编辑')
        type = 'ss'
        gv.font_name(type)
        self.driver.keyevent(4)
        gv.font_size(23)
        gv.font_style(type, '加粗')
        gv.font_style(type, '倾斜')
        gv.font_style(type, '删除线')
        gv.font_style(type, '下划线')
        gv.font_color(type)

    # @unittest.skip('skip test_drag_sheet')
    def test_drag_sheet(self):  # sheet拖动
        logging.info('==========test_drag_sheet==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.add_sheet()
        ss.add_sheet()
        ele1 = ss.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="0"]')
        ele2 = ss.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="2"]')
        # ele1 = ss.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="0"]')
        # ele2 = ss.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="2"]')
        ss.drag_element(ele1, ele2)

    # @unittest.skip('skip test_sheet_operation1')
    def test_sheet_operation1(self):  # sheet相关功能
        logging.info('==========test_sheet_operation1==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.operate_sheet(0, 'insert')
        ss.operate_sheet(0, 'copy')
        ss.operate_sheet(0, 'remove')
        ss.operate_sheet(0, 'hide')
        ss.unhide_sheet(0, 0)

    # @unittest.skip('skip test_sheet_operation')
    def test_sheet_operation(self):  # sheet相关功能
        logging.info('==========test_sheet_operation==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.hide_sheet()
        ss.show_sheet()
        ss.add_sheet()
        ss.rename_sheet(0, 'test')
        self.assertTrue(ss.check_rename_sheet(0, 'test'))

    # @unittest.skip('skip test_expand_fold')
    @data(*wps)
    def test_expand_fold(self, type):  # 编辑栏收起展开
        logging.info('==========test_expand_fold==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.fold_expand()
        gv.fold_expand()

    # @unittest.skip('skip test_search_replace')
    @data(*wps)
    def test_search_replace(self, type):  # 查找替换
        logging.info('==========test_search_replace==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        if type in ws:
            gv.group_button_click('查看')
        gv.search_content(type, '的')
        gv.replace_content('得')
        time.sleep(3)
        gv.replace_content('得', 'all')

    # @unittest.skip('skip test_zoom_pinch')
    @data(*wps)
    def test_zoom_pinch(self, type):
        logging.info('==========test_zoom_pinch==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        ov.zoom()
        ov.pinch()
        time.sleep(3)

    # @unittest.skip('skip test_read_mode')
    @data(*wps)
    def test_read_mode(self, type):  # 阅读模式
        logging.info('==========test_read_mode==========')
        cv = CreateView(self.driver)
        cv.create_file(type)

        gv = GeneralView(self.driver)
        gv.switch_write_read()
        self.assertTrue(gv.check_write_read())

    # @unittest.skip('skip test_share_file')
    @data(*share_list)
    def test_share_file(self, way):  # 分享文件
        logging.info('==========test_share_file==========')
        index = way.index('_')
        suffix = search_dict[way[0:index]]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)

        gv = GeneralView(self.driver)
        gv.share_file(way[0:index], way[index + 1:])

    # @unittest.skip('skip test_export_pdf')
    @data(*wp)
    def test_export_pdf(self, type):  # 导出pdf
        logging.info('==========test_export_pdf==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)

        gv = GeneralView(self.driver)
        file_name = 'export_pdf ' + gv.getTime('%H_%M_%S')
        gv.export_pdf(file_name, 'local')

        self.assertTrue(gv.check_export_pdf())

    # @unittest.skip('skip test_scroll_screen')
    @data(*wps)
    def test_scroll_screen(self, type):  # 滚屏
        logging.info('==========test_scroll_screen_==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        if type == 'pg':
            ov.swipeLeft()
            ov.swipeLeft()
            ov.swipeRight()
        elif type == 'ss':
            ov.swipeLeft()
            ov.swipeLeft()
            ov.swipeRight()
            ov.swipeUp()
            ov.swipeUp()
            ov.swipeDown()
        else:
            ov.swipeUp()
            ov.swipeUp()
            ov.swipeDown()
        time.sleep(3)

    # @unittest.skip('skip test_save_as_existFile')
    @data(*wps)
    def test_save_as_existFile(self, type):  # 已有文件另存为
        logging.info('==========test_save_as_existFile==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        cv = CreateView(self.driver)
        file_name = 'save_as_exist ' + cv.getTime('%H_%M_%S')
        cv.save_as_file(file_name, 'local', 1)
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_save_existFile')
    @data(*wps)
    def test_save_existFile(self, type):  # 已有文件改动保存
        logging.info('==========test_save_existFile==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.group_button_click('签批')
        gv.pen_type(type, '荧光笔')
        self.driver.swipe(300, 400, 800, 500)
        cv.save_file()
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_save_as_newFile')
    @data(*wps)
    def test_save_as_newFile(self, type):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = 'save_as_new ' + cv.getTime('%H_%M_%S')
        cv.save_as_file(file_name, 'local', 1)
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_save_newFile')
    @data(*wps)
    def test_save_newFile(self, type):  # 新建脚本保存
        logging.info('==========test_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = 'save_new ' + cv.getTime('%H_%M_%S')
        cv.save_new_file(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_rotate')
    @data(*wps)
    def test_rotate(self, type):
        logging.info('==========test_rotate==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        # gv.screen_rotate('landscape')
        self.assertTrue(gv.check_rotate())
        gv.screen_rotate('portrait')

    # @unittest.skip('skip test_undo_redo')
    @data(*wps)
    def test_undo_redo(self, type):  # 撤销、重做
        logging.info('==========test_undo_redo==========')
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        cv.create_file(type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo')  # 判断页面是否已切过来

        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        gv.fold_expand()

        gv.undo_option()
        time.sleep(1)
        gv.redo_option()
        time.sleep(1)
        gv.undo_option()
        time.sleep(1)

        logging.info('capture before undo')
        gv.getScreenShot4Compare('before_undo')

        gv.redo_option()
        time.sleep(1)

        logging.info('capture before redo')
        gv.getScreenShot4Compare('before_redo')

        gv.undo_option()
        time.sleep(1)
        logging.info('capture after undo')
        gv.getScreenShot4Compare('after_undo')

        gv.redo_option()
        time.sleep(1)
        logging.info('capture after redo')
        gv.getScreenShot4Compare('after_redo')

        result1 = gv.compare_pic('before_undo.png', 'after_undo.png')
        result2 = gv.compare_pic('before_redo.png', 'after_redo.png')

        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')
