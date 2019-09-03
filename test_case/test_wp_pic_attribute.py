import logging
import time
import unittest

from appium.webdriver.common.touch_action import TouchAction

from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd
from airtest.core.api import *


class TestWordPictureAttrbute(StartEnd):
    def choose_pic_setup(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        time.sleep(3)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wp = WpView(self.driver)
        wp.swipeup()
        wp.choose_pic()

    @unittest.skip('skip test_undo_redo')
    def test_wp_pic_fixed_rotate(self):
        # 图片旋转
        logging.info('==========test_wp_pic_fixed_rotation==========')
        self.choose_pic_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wp = WpView(self.driver)
        wp.pic_fixed_rotate()

    @unittest.skip('skip test_undo_redo')
    def test_wp_pic_change_size(self):
        # 设置图片宽高
        logging.info('==========test_wp_pic_change_size==========')
        self.choose_pic_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wp = WpView(self.driver)
        wp.pic_change_size()
        time.sleep(5)

    def test_wp_pic_shadow(self):
        # 图片阴影
        logging.info('==========test_wp_pic_shadow==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        wp.pic_effect()

    @unittest.skip('skip test_undo_redo')
    def test_wp_pic_broad(self):
        # 图片轮廓
        logging.info('==========test_wp_pic_broad==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        wp.pic_broad()

    @unittest.skip('skip test_undo_redo')
    def test_wp_pic_broad_type(self):
        # 图片轮廓类型
        logging.info('==========test_wp_pic_broad_type==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        wp.pic_broad_type()

    @unittest.skip('skip test_undo_redo')
    def test_wp_pic_broad_width(self):
        # 设置图片轮廓粗细
        logging.info('==========test_wp_pic_broad_width==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        wp.pic_broad_width()

    def test_wp_pic_surround(self):
        # 设置图片环绕
        logging.info('==========test_wp_pic_surround==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        wp.surround('picture')
        time.sleep(10)

    def test_wp_pic_move(self):
        # 移动图片位置
        logging.info('==========test_wp_pic_move==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wp = WpView(self.driver)
        wp.swipeup()
        a = wp.choose_pic()
        wp.surround_peripheral()
        self.driver.swipe(a[0], a[1], 0, 0)
        time.sleep(10)

    def test_wp_pic_layer(self):  # 有缺陷，嵌入型图片永远在底层
        # 设置图片叠放次序
        logging.info('==========test_wp_pic_layer==========')
        self.test_wp_pic_copy_paste()
        wp = WpView(self.driver)
        wp.choose_pic()
        wp.surround_peripheral()
        self.driver.keyevent(4)
        self.driver.keyevent(4)
        wp.pic_layer()

    def test_wp_pic_free_rotate(self):
        # 图片自由旋转
        logging.info('==========test_wp_pic_free_rotate==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        wp.object_free_rotate()
        time.sleep(10)

    def test_wp_pic_save_album(self):
        # 保存图片至相册
        logging.info('==========test_wp_pic_save_album==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        wp.pic_save_to_album()
        self.assertTrue(wp.get_toast_message('图片保存成功'), 'picture save to album fail')

    def test_wp_pic_rotate_90(self):
        # 图片旋转90度
        logging.info('==========test_wp_pic_rotate_90==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        wp.object_rotate_90()
        time.sleep(10)

    def test_wp_pic_cut_paste(self):
        logging.info('==========test_wp_pic_cut_paste==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        wp.object_cut_paste()
        time.sleep(10)

    def test_wp_pic_copy_paste(self):
        logging.info('==========test_wp_pic_copy_paste==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        wp.object_copy_paste()
        time.sleep(10)

    def test_wp_pic_delete(self):
        logging.info('==========test_wp_pic_delete==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        wp.object_delete()
        time.sleep(10)

    def test_wp_pic_control_point(self):
        logging.info('==========test_wp_pic_control_point==========')
        self.choose_pic_setup()
        wp = WpView(self.driver)
        connect_device(wp.get_phone_dev())
        wp.adjust_object_place()
        # 手势拖拉大小控制点
        wp.pic_control_point()
        time.sleep(10)
