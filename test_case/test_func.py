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
from businessView.ssView import SSView
from common.myunit import StartEnd

waylist = ['wx', 'qq', 'ding', 'mail']
wps = ['wp', 'ss', 'pg']
ws = ['wp', 'ss']
search_dict={'wp':'docx','ss':'xlsx','pg':'pptx'}


@ddt
class TestFunc(StartEnd):

    @unittest.skip('skip test_shape_text_attr')
    def test_shape_text_attr(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========test_shape_text_attr==========')
        cv = CreateView(self.driver)
        type = 'wp'
        cv.create_file(type, 0)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        time.sleep(1)
        gv.tap(700, 767, 5)
        gv.tap(700, 767, 6)
        gv.group_button_click('编辑')
        gv.font_name(type)
        gv.font_size(15)
        gv.font_style(type, '倾斜')
        gv.font_color(type, 6, 29)
        gv.swipe_ele('//*[@text="字体颜色"]', '//*[@text="编辑"]')
        time.sleep(1)
        gv.tap(700, 767)
        for i in range(20):
            self.driver.press_keycode(random.randint(7, 16))
        time.sleep(1)
        # gv.tap(700, 767, 2)
        gv.group_button_click('编辑')
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

    @unittest.skip('skip test_shape_attr1')
    def test_shape_attr1(self):
        logging.info('==========test_shape_attr1==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        type = 'ss'
        gv.insert_shape('ss', 1)
        time.sleep(1)
        gv.tap(700, 767, 4)  # 双击进入编辑
        for i in range(100):
            self.driver.press_keycode(random.randint(7, 16))
        gv.group_button_click('编辑')

        gv.shape_option(type, 5, width=5, height=5)
        gv.shape_option(type, 6, top=0.5, bottom=0.5, left=0.5, right=0.5)
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_shape_quick_function"]'
        ele2 = '//*[@text="轮廓"]'
        ele3 = '//*[@text="效果"]'
        gv.swipe_ele(ele2, ele1)
        gv.swipe_ele(ele3, ele2)
        gv.shape_content_align(type, '右对齐', '下对齐')
        gv.shape_content_align(type)
        gv.shape_content_align(type, '水平居中', '垂直居中')
        time.sleep(3)

    @unittest.skip('skip test_shape_attr')
    def test_shape_attr(self):
        logging.info('==========test_shape_attr==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape('ss', 6, 30)
        gv.shape_insert('ss', 6, 31)
        gv.shape_insert('ss', 6, 32)
        gv.shape_insert('ss', 6, 33)
        type = 'ss'
        gv.shape_option(type, 2)
        gv.shape_fill_color(type, 6, 24)
        gv.shape_fill_color_transparency(5)
        ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_shape_quick_function"]'
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

    @unittest.skip('skip test_signature')
    @data(*wps)
    def test_signature(self,type):  # 签批
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

    @unittest.skip('skip test_formula1')
    def test_formula1(self):  # 其他类型公式
        logging.info('==========test_formula1==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_formula')
    def test_formula(self):
        logging.info('==========test_formula==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_data_table')
    def test_data_table(self):  # 数据排序，工作表格式
        logging.info('==========test_data_table==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_insert_shape')
    def test_insert_shape(self):
        logging.info('==========test_insert_shape==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)

        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        ss.insert_chart()
        gv.insert_shape('ss')

    @unittest.skip('skip test_table_style')
    def test_table_style(self):  # 表格样式
        logging.info('==========test_table_style==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_cell_inser_delete_fit')
    def test_cell_inser_delete_fit(self):  # 插入删除行宽列高清除
        logging.info('==========test_cell_inser_delete_fit==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_merge_wrap')
    def test_merge_wrap(self):
        logging.info('==========test_merge_wrap==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_num_style')
    def test_num_style(self):
        logging.info('==========test_num_style==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_cell_border')
    def test_cell_border(self):  # 遍历边框所有功能
        logging.info('==========test_cell_border==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        time.sleep(1)
        self.driver.swipe(200, 1856, 200, 1150, 2000)
        ss.cell_border()

    @unittest.skip('skip test_cell_attr')
    def test_cell_attr(self):
        logging.info('==========test_cell_attr==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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

    @unittest.skip('skip test_font_attr')
    def test_font_attr(self):
        logging.info('==========test_font_attr==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
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
        gv.font_style('加粗')
        gv.font_style('倾斜')
        gv.font_style('删除线')
        gv.font_style('下划线')
        gv.font_color()

    @unittest.skip('skip test_drag_sheet')
    def test_drag_sheet(self):  # sheet拖动
        logging.info('==========test_drag_sheet==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.add_sheet()
        ss.add_sheet()
        ele1 = ss.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="0"]')
        ele2 = ss.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="2"]')
        # ele1 = ss.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="0"]')
        # ele2 = ss.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="2"]')
        ss.drag_element(ele1, ele2)

    @unittest.skip('skip test_sheet_operation1')
    def test_sheet_operation1(self):  # sheet相关功能
        logging.info('==========test_sheet_operation1==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.operate_sheet(0, 'insert')
        ss.operate_sheet(0, 'copy')
        ss.operate_sheet(0, 'remove')
        ss.operate_sheet(0, 'hide')
        ss.unhide_sheet(0, 0)

    @unittest.skip('skip test_sheet_operation')
    def test_sheet_operation(self):  # sheet相关功能
        logging.info('==========test_sheet_operation==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.hide_sheet()
        ss.show_sheet()
        ss.add_sheet()
        ss.rename_sheet(0, 'test')
        self.assertTrue(ss.check_rename_sheet(0, 'test'))

    @unittest.skip('skip test_expand_fold')
    def test_expand_fold(self):  # 编辑栏收起展开
        logging.info('==========test_expand_fold==========')
        ov = OpenView(self.driver)
        ov.open_file('用地统计表.xls')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.fold_expand()
        gv.fold_expand()

    @unittest.skip('skip test_search_replace')
    @data(*wps)
    def test_search_replace(self,type):  # 查找替换
        logging.info('==========test_search_replace==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s'%suffix)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        if type in ws:
            gv.group_button_click('查看')
        gv.search_content(type,'的')
        gv.replace_content('得')
        time.sleep(3)
        gv.replace_content('得', 'all')

    @unittest.skip('skip test_zoom_pinch')
    def test_zoom_pinch(self):
        logging.info('==========test_zoom_pinch==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')
        ov.zoom()
        time.sleep(3)
        ov.pinch()
        time.sleep(3)

    @unittest.skip('skip test_read_mode')
    @data(*wps)
    def test_read_mode(self,type):  # 阅读模式
        logging.info('==========test_read_mode==========')
        cv = CreateView(self.driver)
        cv.create_file(type)

        gv = GeneralView(self.driver)
        gv.switch_write_read()
        self.assertTrue(gv.check_write_read())

    @unittest.skip('skip test_share_file')
    @data(*waylist)
    def test_share_file(self, way):  # 分享文件
        logging.info('==========test_share_file==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        gv.share_file(way)

    @unittest.skip('skip test_export_pdf')
    def test_export_pdf(self):  # 导出pdf
        logging.info('==========test_export_pdf==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        file_name = 'export_pdf ' + gv.getTime('%H_%M_%S')
        gv.export_pdf(file_name, 'local')

        self.assertTrue(gv.check_export_pdf())

    @unittest.skip('skip test_save_as_existFile')
    def test_save_as_existFile(self):  # 已有文件另存为
        logging.info('==========test_save_as_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        ov.open_file('save1.doc')
        file_name = 'save_as_existFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_save_existFile')
    def test_save_existFile(self):  # 已有文件改动保存
        logging.info('==========test_save_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        ov.open_file('save1.doc')
        gv.switch_write_read()
        self.driver.press_keycode(48)
        cv.save_file_icon()
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_save_as_newFile')
    def test_save_as_newFile(self):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_as_newFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_save_newFile')
    def test_save_newFile(self):  # 新建脚本保存
        logging.info('==========test_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_newFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_icon(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_rotate')
    def test_rotate(self):
        logging.info('==========test_rotate==========')
        ov = OpenView(self.driver)
        ov.open_file('00555.doc')
        gv = GeneralView(self.driver)
        # gv.screen_rotate('landscape')
        self.assertTrue(gv.check_rotate())
        gv.screen_rotate('portrait')

    @unittest.skip('skip test_undo_redo')
    def test_undo_redo(self):
        logging.info('==========test_undo_redo==========')
        gv = GeneralView(self.driver)
        result1, result2 = gv.check_undo_redo_event()

        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')
