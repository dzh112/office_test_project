import logging
import time
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd
from airtest.core.api import *


class TestWordShapeAttrbute(StartEnd):
    def shapeatt_setup(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('插入')
        wv.insert_text_box()

    def test_wp_shape_copy_paste(self):
        # 形状复制粘贴
        logging.info('==========test_wp_shape_copy_paste==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())

        wv.object_copy_paste()
        time.sleep(10)

    def test_wp_shape_cut_paste(self):
        # 形状剪切粘贴
        logging.info('==========test_wp_shape_cut_paste==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())

        wv.object_cut_paste()
        time.sleep(10)

    def test_wp_shape_delete(self):
        # 形状 删除
        logging.info('==========test_wp_shape_delete==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())
        wv.object_delete()
        time.sleep(10)

    def test_wp_shape_rotate_90(self):
        # 形状旋转90度
        logging.info('==========test_wp_shape_rotate_90==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())

        wv.object_rotate_90()
        time.sleep(10)

    def test_wp_shape_free_rotate(self):
        # 形状自由旋转
        logging.info('==========test_wp_shape_free_rotate==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())

        wv.object_free_rotate()
        time.sleep(10)

    def test_wp_shape_control_point(self):
        # 手势拖拉形状控制点
        logging.info('==========test_wp_shape_control_point==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())

        wv.shape_control_point()
        time.sleep(10)

    def test_wp_shape_text_select(self):
        # 文本框内容选取
        logging.info('==========test_wp_shape_text_select==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # # connect_device(wv.get_phone_dev())
        wv.text_box_text_select()
        self.assertTrue(exists(Template(r'../Res/res_delete.png', resolution=(1080, 1920))))

    def test_wp_shape_move(self):
        # 文本框移动
        logging.info('==========test_wp_shape_move==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        # connect_device(wv.get_phone_dev())
        wv.text_box_move()
        time.sleep(10)

    def test_wp_shape_fixed_rotate(self):
        # 形状旋转
        logging.info('==========test_wp_shape_fixed_rotate==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        wv.shape_fixed_rotate()

    def test_wp_shape_change_size(self):
        # 设置形状宽高
        logging.info('==========test_wp_shape_change_size==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        wv.shape_chang_size()

    def test_wp_shape_text_box_margin(self):
        # 设置文本框边距
        logging.info('==========test_wp_shape_margin_text_box==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        wv.text_box_margin()

    def test_wp_shape_fill_color(self):
        # 设置形状填充色及透明度
        logging.info('==========test_wp_shape_fill_color==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        self.assertTrue(wv.shape_fill_color(), msg='Filling color transparency fail')

    def test_wp_shape_broad(self):
        # 形状轮廓
        logging.info('==========test_wp_shape_broad==========')
        self.shapeatt_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wv = WpView(self.driver)
        wv.shape_broad()

    def test_wp_shape_type(self):
        # 形状轮廓类型
        logging.info('==========test_wp_shape_broad==========')
        self.shapeatt_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wv = WpView(self.driver)
        wv.shape_broad_type()

    def test_wp_shape_broad_width(self):
        # 设置形状轮廓粗细
        logging.info('==========test_wp_shape_broad==========')
        self.shapeatt_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wv = WpView(self.driver)
        wv.shape_broad_width()

    def test_wp_shape_shadow(self):
        # 设置形状阴影和三维效果
        logging.info('==========test_wp_shape_broad==========')
        self.shapeatt_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wv = WpView(self.driver)
        wv.shape_effect()

    def test_wp_shape_surround(self):
        # 设置形状文字环绕效果
        logging.info('==========test_wp_shape_surround==========')
        self.shapeatt_setup()
        gv = GeneralView(self.driver)
        gv.fold_expand()
        wv = WpView(self.driver)
        wv.surround('shape')

    def test_wp_shape_layer(self):
        # 设置形状叠放次序
        logging.info('==========test_wp_shape_surround==========')
        self.shapeatt_setup()
        wv = WpView(self.driver)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.switch_write_read()
        wv.switch_option('插入')
        wv.insert_text_box()
        gv.fold_expand()
        wv.shape_layer()

    def test_wp_shape_text_fonts(self):
        # 设置形状内选取文字字体
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.fonts_list()

    def test_wp_shape_text_fonts_size(self):
        # 设置形状内选取文字字号
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.fonts_size_list()

    def test_wp_shape_text_effect(self):
        # 设置形状内选取文字效果
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.fonts_effect()

    def test_wp_shape_text_color(self):
        # 设置形状内选取文字颜色
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.fonts_color()

    def test_wp_shape_text_high_light(self):
        # 设置形状内选取文字高亮
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.fonts_high_light()

    def test_wp_shape_text_bullet(self):
        # 设置形状内选取文字项目符号
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.fonts_bullet()

    def test_wp_shape_text_align_indent(self):
        # 设置形状内选取文字对齐、缩进量
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.align_indent()

    def test_wp_shape_text_line_space_size(self):
        # 设置形状内选取文字多倍行距
        self.test_wp_shape_text_select()
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        wv.line_space_size()
