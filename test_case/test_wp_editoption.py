import logging
import time

from appium.webdriver.common.touch_action import TouchAction

from businessView.openView import OpenView
from businessView.wpCommonView import WpCommonView
from common.myunit import StartEnd


class TestWordEditOption(StartEnd):
    def wp_setup(self):
        logging.info('==========test_wp_fonts==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wcv = WpCommonView(self.driver)
        wcv.switch_edit()
        # s = ov.get_size()
        # action = TouchAction(self.driver)
        # action.long_press(x=s[0] * 0.5, y=s[1] * 0.5).wait(1000).move_to(x=s[0] * 0.6, y=s[1] * 0.5).release().perform()

    def test_wp_fonts(self):
        # 遍历字体列表
        logging.info('==========test_wp_fonts==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)

        wcv.fonts_list()

    def test_wp_fonts_size(self):
        # 遍历字体大小
        logging.info('==========test_wp_fonts_size==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)

        wcv.fonts_size_list()

    def test_wp_fonts_effect(self):
        # 设置字体效果
        logging.info('==========test_wp_fonts_effect==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)
        wcv.fonts_effect()

    def test_wp_fonts_color(self):
        # 设置字体颜色
        logging.info('==========test_wp_fonts_color==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)

        wcv.fonts_color()

    def test_wp_fonts_high_light(self):
        # 设置字体高亮
        logging.info('==========test_wp_fonts_high_light==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)
        wcv.fonts_high_light()

    def test_wp_fonts_bullet(self):
        # 设置字体项目符号
        logging.info('==========test_wp_fonts_bullet==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)
        wcv.fonts_bullet()

    def test_wp_fonts_align_indent(self):
        # 设置字体对齐、缩进量
        logging.info('==========test_wp_fonts_align_indent==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)
        wcv.align_indent()

    def test_wp_fonts_column(self):
        # 设置分栏
        logging.info('==========test_wp_fonts_column==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)
        wcv.column()

    def test_wp_line_space_size(self):
        # 多倍行距
        logging.info('==========test_wp_line_space_size==========')
        self.wp_setup()
        wcv = WpCommonView(self.driver)
        wcv.line_space_size()
