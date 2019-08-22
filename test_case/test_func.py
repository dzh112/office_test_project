#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
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


@ddt
class TestFunc(StartEnd):

    def test_num_style(self):
        logging.info('==========test_cell_border==========')
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
        ele1 ='//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_font_name"]'
        ele2 = '//*[@text="单元格填充"]'
        ele3 = '//*[@text="数字格式"]'
        ss.swipe_ele(ele2,ele1)
        ss.swipe_ele(ele3,ele2)
        ss.cell_num_style()

    def test_cell_border(self): #遍历边框所有功能
        logging.info('==========test_cell_border==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        time.sleep(1)
        self.driver.swipe(200, 1856, 200, 1150, 2000)
        ss.cell_border()

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
        ss.cell_align('水平居中','下对齐')
        # ss.cell_color()


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
        gv.font_name()
        self.driver.keyevent(4)
        gv.font_size(23)
        gv.font_style('加粗')
        gv.font_style('倾斜')
        gv.font_style('删除线')
        gv.font_style('下划线')
        gv.font_color()

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

    def test_expand_fold(self):  # 编辑栏收起展开
        logging.info('==========test_expand_fold==========')
        ov = OpenView(self.driver)
        ov.open_file('用地统计表.xls')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.fold_expand()
        gv.fold_expand()

    def test_search_replace(self):  # 查找替换
        logging.info('==========test_search_replace==========')
        ov = OpenView(self.driver)
        ov.open_file('用地统计表.xls')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.search_content('其中')
        gv.replace('其次')
        time.sleep(3)
        gv.replace('其次', 'all')

    def test_copy(self):  # 复制,先不写
        logging.info('==========test_zoom==========')
        cv = CreateView(self.driver)
        cv.create_file('ss', 0)
        time.sleep(1)

        cv.tap(110 + 263, 295 + 55)  # 选中单元格
        cv.drag(110 + 263 * 2, 295 + 55 * 2, 110 + 263 * 3, 295 + 55 * 2)

        # cv.tap(110 + 263*1.5, 295 + 55*1.5)#双击进入编辑
        # cv.tap(110 + 263*1.5, 295 + 55*1.5)

    def test_zoom_pinch(self):
        logging.info('==========test_zoom==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')
        ov.zoom()
        time.sleep(3)
        ov.pinch()
        time.sleep(3)

    def test_read_mode(self):  # 横屏模式
        logging.info('==========test_read_mode==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.switch_write_read()
        self.assertTrue(gv.check_write_read())

    @data(*waylist)
    def test_share_file(self, way):  # 分享文件
        logging.info('==========test_share_file==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        gv.share_file(way)

    # @unittest.skip('skip test_undo_redo')
    def test_export_pdf(self):  # 导出pdf
        logging.info('==========test_export_pdf==========')
        ov = OpenView(self.driver)
        ov.open_file('save1.doc')

        gv = GeneralView(self.driver)
        file_name = 'export_pdf ' + gv.getTime('%H_%M_%S')
        gv.export_pdf(file_name, 'local')

        self.assertTrue(gv.check_export_pdf())

    @unittest.skip('skip test_undo_redo')
    def test_save_as_existFile(self):  # 已有文件另存为
        logging.info('==========test_save_as_existFile==========')
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)
        ov.open_file('save1.doc')
        file_name = 'save_as_existFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
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

    @unittest.skip('skip test_undo_redo')
    def test_save_as_newFile(self):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_as_newFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_option(file_name, 'local', 1, 'save_as')
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
    def test_save_newFile(self):  # 新建脚本保存
        logging.info('==========test_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file('wp', 0)
        file_name = 'save_newFile ' + cv.getTime('%H_%M_%S')
        cv.save_file_icon(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_undo_redo')
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
