import logging
import time

from appium.webdriver.common.touch_action import TouchAction

from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd


class TestWordEditOption(StartEnd):
    def test_wp_text_select(self):
        # 文本选取
        logging.info('==========test_wp_fonts==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wv = WpView(self.driver)
        wv.switch_option('编辑')
        s = ov.get_size()
        action = TouchAction(self.driver)
        action.long_press(x=s[0] * 0.5, y=s[1] * 0.5).wait(1000).move_to(x=s[0] * 0.6, y=s[1] * 0.5).release().perform()

    def test_wp_fonts(self):
        # 遍历字体列表
        logging.info('==========test_wp_fonts==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.fonts_list()

    def test_wp_fonts_size(self):
        # 遍历字体大小
        logging.info('==========test_wp_fonts_size==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.fonts_size_list()

    def test_wp_fonts_effect(self):
        # 设置字体效果
        logging.info('==========test_wp_fonts_effect==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.fonts_effect()

    def test_wp_fonts_color(self):
        # 设置字体颜色
        logging.info('==========test_wp_fonts_color==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.fonts_color()

    def test_wp_fonts_high_light(self):
        # 设置字体高亮
        logging.info('==========test_wp_fonts_high_light==========')
        self.test_wp_text_select()
        wcv = WpView(self.driver)
        wcv.fonts_high_light()

    def test_wp_fonts_bullet(self):
        # 设置字体项目符号
        logging.info('==========test_wp_fonts_bullet==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.fonts_bullet()

    def test_wp_fonts_align_indent(self):
        # 设置字体对齐、缩进量
        logging.info('==========test_wp_fonts_align_indent==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.align_indent()

    def test_wp_fonts_column(self):
        # 设置分栏
        logging.info('==========test_wp_fonts_column==========')
        self.test_wp_text_select()
        wcv = WpView(self.driver)
        wcv.column()

    def test_wp_line_space_size(self):
        # 多倍行距
        logging.info('==========test_wp_line_space_size==========')
        self.test_wp_text_select()
        wv = WpView(self.driver)
        wv.line_space_size()
