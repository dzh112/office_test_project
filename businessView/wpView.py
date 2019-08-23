import logging
import random
import time
from common.common_fun import Common
from selenium.webdriver.common.by import By


class WpView(Common):
    self_adaption_icon = (By.ID, 'com.yozo.office:id/yozo_ui_quick_option_wp_read_full_screen')
    toolbar_button = (By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode')  # 编辑签批切换
    option_group_button = (By.ID, 'com.yozo.office:id/yozo_ui_option_group_button')  # 菜单项
    find_replace = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_find_replace')  # 查看-查找替换
    find_content = (By.ID, 'com.yozo.office:id/yozo_ui_et_find_content')  # 查看-查找输入框
    icon_search = (By.ID, 'com.yozo.office:id/yozo_ui_iv_icon_search')  # 查看-查找搜索图标
    find_previous = (By.ID, 'com.yozo.office:id/yozo_ui_iv_find_previous')  # 查看-查找上一个
    find_next = (By.ID, 'com.yozo.office:id/yozo_ui_iv_find_next')  # 查看-查找下一个
    find_replace_switch = (By.ID, 'com.yozo.office:id/yozo_ui_iv_find_replace_switch')  # 查看-查找切换
    rb_replace = (By.ID, 'com.yozo.office:id/rb_replace')  # 查看-查找与替换
    replace_content = (By.ID, 'com.yozo.office:id/yozo_ui_et_replace_content')  # 查看-替换输入框
    replace_one = (By.ID, 'com.yozo.office:id/yozo_ui_iv_replace_one')  # 查看-替换单个
    replace_all = (By.ID, 'com.yozo.office:id/yozo_ui_tv_replace_all')  # 查看-替换所有
    bookmark_insert = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_bookmark_insert')  # 插入书签
    bookmark_name_edit = (By.ID, 'com.yozo.office:id/bookmark_name_edit')  # 书签名输入框
    bookmark_sure_btn = (By.ID, 'com.yozo.office:id/sure_btn')  # 书签弹窗确定
    bookmark_catalog = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_bookmark_catalog')  # 书签列表
    option_expand_button = (By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button')  # 展开菜单栏
    wp_goto = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_goto')  # 跳转页
    goto_page = (By.ID, 'com.yozo.office:id/et_goto_page')  # 输入页码
    goto_id_ok = (By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok')  # 跳转页确定
    high_light = (By.XPATH, '//android.widget.TextView[@text="高亮颜色"]')
    system2 = (By.ID, 'com.yozo.office:id/yozo_ui_option_title_container')  # 字体标题
    reduce_size = (By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left')  # 缩小字号

    def self_adaption(self):
        # 点击自适应屏幕按钮
        self.driver.find_element(*self.self_adaption_icon).click()

    def wp_find_replace(self):
        # 查找关键字，并替换

        self.driver.find_element(*self.find_replace).click()
        self.driver.find_element(*self.find_content).send_keys("文档")
        self.driver.find_element(*self.icon_search).click()
        self.driver.find_element(*self.find_previous).click()
        self.driver.find_element(*self.find_next).click()

        self.driver.find_element(*self.find_replace_switch).click()
        self.driver.find_element(*self.rb_replace).click()
        self.driver.find_element(*self.replace_content).send_keys("file")
        self.driver.find_element(*self.replace_one).click()
        self.driver.find_element(*self.replace_all).click()

    def wp_bookmark(self):
        # 插入书签
        self.driver.find_element(*self.bookmark_insert).click()
        self.driver.find_element(*self.bookmark_name_edit).send_keys("file")
        self.driver.find_element(*self.bookmark_sure_btn).click()
        insert_result = self.exist("//*[@text='添加书签成功']")
        self.driver.find_element(*self.option_expand_button).click()
        self.driver.find_element(*self.bookmark_catalog).click()
        catalog_result = self.exist('//android.widget.TextView[@text="file"]')
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="file"]').click()
        return insert_result and catalog_result

    def wp_jump(self):
        # 跳转页
        self.driver.find_element(*self.wp_goto).click()
        self.driver.find_element(*self.goto_page).send_keys(random.randint(1, 6))
        self.driver.find_element(*self.goto_id_ok).click()

    def fonts_list(self):
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_font_name').click()
        s1 = self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="系统"]')
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_title_container')
        # self.driver.drag_and_drop(s1, s2)
        self.driver.scroll(s1, s2)
        while True:
            for i in self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[1:]:
                i.click()
                time.sleep(0.5)
            old_start_list = self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[1].text
            old_end_list = self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[-1].text
            self.driver.scroll(self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[-1],
                               self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[1])
            new_start_list = self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[1].text
            new_end_list = self.driver.find_elements(By.ID, 'com.yozo.office:id/label_text_view')[-1].text
            if old_start_list == new_start_list and old_end_list == new_end_list:
                break

    def fonts_size_list(self):
        size1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_recycler_view')
        while True:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
            if int(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[0].text) == 5:
                for i in range(4):
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
                break
        while True:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
            if int(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[-1].text) == 50:
                for i in range(4):
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
                break

    def fonts_effect(self):
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_font_style')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.CheckBox']"):
            i.click()

    def fonts_color(self):
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_font_color')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s1.find_element(By.XPATH, "//*[@class='android.widget.ImageView']").click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_id_color_all')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def fonts_bullet(self):
        self.driver.scroll(self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="高亮颜色"]'),
                           self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_title_container'))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_item_bullets_numbers')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s1.find_element(By.XPATH, "//*[@class='android.widget.ImageView']").click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def align_indent(self):
        self.driver.scroll(self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="高亮颜色"]'),
                           self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_title_container'))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_para_hor_align')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_para_indent')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']"):
            i.click()

    def line_space_size(self):
        self.driver.scroll(self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="高亮颜色"]'),
                           self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_title_container'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_para_line_space').click()
        size1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_recycler_view')
        while True:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
            if float(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[0].text) == 0.25:
                for i in range(4):
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
                break
        while True:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
            if float(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[-1].text) == 6.00:
                for i in range(4):
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
                break

    def switch_option(self, option):
        # 展开菜单栏
        logging.info('==========open %s option==========' % option)
        if self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text == option:
            if not self.exist("//*[@resource-id='com.yozo.office:id/yozo_ui_option_content_container']"):
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').click()
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='%s']" % option).click()

    def insert_shape(self):
        # 插入形状
        logging.info('==========insert shape==========')
        # 文本框
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_insert_shape')
        s1.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[0].click()
        # 形状-更多
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_shape_insert')
        s2.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[-1].click()
        s3 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_id_more_shape_main_container')
        # 42种常用的基本形状
        for i in s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[:18]:
            i.click()
        self.driver.scroll(s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[-1],
                           s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[0])
        for i in s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']"):
            i.click()
        # 记录最近使用的6种自选图形
        s4 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_id_more_shape_sub_container')
        for i in s4.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']"):
            i.click()

    def insert_table(self):
        # 插入表格
        logging.info('==========insert table==========')
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_insert_table')
        s1.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[0].click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_table_style')
        s2.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[-1].click()
        s3 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')
        for i in s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[:15]:
            i.click()
        self.driver.scroll(s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[-1],
                           s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']")[0])
        for i in s3.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']"):
            i.click()

    def fonts_high_light(self):
        # 字体高亮
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.reduce_size))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_highlight_color')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s1.find_element(By.XPATH, "//*[@class='android.widget.ImageView']").click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def column(self):
        # 分栏
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.system2))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_columns')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def insert_watermark(self):
        # 插入水印
        '''斜视水印'''
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_insert_watermark').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_water_mark').send_keys('斜视')
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/rg_water_mark')
        s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']")[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
        self.driver.find_element(*self.option_expand_button).click()
        '''删除水印'''
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_insert_watermark').click()
        self.driver.find_element(By.XPATH, "//*[@text='删除文档中的水印']").click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
        self.driver.find_element(*self.option_expand_button).click()
        '''水平水印'''
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_insert_watermark').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_water_mark').send_keys('水平')
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/rg_water_mark')
        s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']")[1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
        self.driver.find_element(*self.option_expand_button).click()

    def check_approve_revision(self):
        # 更改用户名
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_change_name').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_name').clear()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_name').send_keys('revision')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
        # 接受修订
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_model').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_accept').click()
        self.driver.press_keycode(keycode=48)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_reject').click()

    def choose_pic(self):
        x = self.get_size()[0]
        y = self.get_size()[1]
        for i in range(2, 8):
            self.tap(int(x * 0.5), int(y * (i / 10)))
            if self.exist("//*[@resource-id='com.yozo.office:id/yozo_ui_quick_option_wp_picture_surround']"):
                break
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_wp_picture_surround').click()

    def surround(self):
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RelativeLayout']"):
            i.click()