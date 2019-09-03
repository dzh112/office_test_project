import logging
import time
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WpView
from common.myunit import StartEnd


class TestWordSignOption(StartEnd):
    def signoption_setup(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        wv = WpView(self.driver)
        wv.switch_option('签批')

    def test_wp_sign(self):
        # wp签批
        logging.info('==========test_wp_pic_fixed_rotation==========')
        self.signoption_setup()
        gv = GeneralView(self.driver)
        gv.use_finger('wp')
        gv.use_finger('wp')
        gv.pen_type('wp', '钢笔')
        gv.pen_color('wp', 15)
        gv.pen_size('wp', 3)
        gv.swipe(300, 400, 800, 400, 500)
        gv.pen_type('wp', '荧光笔')
        gv.pen_color('wp', 30)
        gv.pen_size('wp', 6)
        gv.swipe(300, 600, 800, 600, 500)
        gv.pen_type('wp', '擦除')
        gv.swipe(200, 400, 900, 400, 500)
        gv.swipe(200, 600, 900, 600, 500)
        time.sleep(3)


