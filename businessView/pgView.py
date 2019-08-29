#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.webdriver.common.by import By

from businessView.generalView import GeneralView


class PGView(GeneralView):


    def switch_mode(self):  # 切换
        logging.info('==========switch_mode==========')

    def pause_resume_play(self):  # 暂停、回复播放
        logging.info('==========pause_resume==========')
        # self.find_element(By.ID,'com.yozo.office:id/yozo_ui_id_pg_play_pause_button').click()
        # x, y = self.get_size()
        # self.tap(y * 0.5, x * 0.5)
        self.tap(880, 540)

    def quit_play(self):  # 退出播放
        logging.info('==========quit_paly==========')
        self.driver.keyevent(4)

    def play_mode(self, mode):  # 播放模式 current,first,autoplay
        logging.info('==========play_mode==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_play_%s' % mode).click()

    def edit_template(self, template):  # 模板
        logging.info('==========edit_template==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_edit_templet').click()
        range = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
        eles = self.driver.find_elements(By.XPATH, range)
        template_ele = '%s[@index="%s"]' % (range, template)
        if int(template) > 8:
            self.swipe_ele1(eles[-1], eles[0])
        self.driver.find_element(By.XPATH, template_ele).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def edit_format(self, format):  # 版式
        # format = ['标题与副标题', '标题', '标题与文本', '标题与两栏文本', '标题与竖排文本-上下', '标题与竖排文本-左右',
        #           '空白','标题与图片','标题、文本与图片','标题、图片与文本','标题、图片与竖排文本','标题、竖排文本与图片']
        logging.info('==========edit_format==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_edit_format').click()
        range = '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout'
        format_ele = '//*[@text="%s"]' % format
        self.swipe_search2(format_ele, range)
        self.driver.find_element(By.XPATH, format_ele).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def thumbnail_scroll(self):  # 缩略图滚屏
        logging.info('==========thumbnail_scroll==========')
        eles = self.driver.find_elements(By.XPATH, '//android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                                   '/android.view.View')
        if len(eles) >= 3:
            self.swipe_ele2(eles[2], eles[0])

    def add_new(self):  # 新建
        logging.info('==========add_new==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_pg_add_slide_button_id').click()

    def search_slide(self, index):  # 查找幻灯片
        logging.info('==========search_slide==========')
        for i in range(10000):
            if not self.get_element_result('//android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                           '/android.view.View[@index="%s"]' % (int(index) - 1)):
                self.thumbnail_scroll()
            else:
                break
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                           '/android.view.View[@index="%s"]' % (int(index) - 1)).click()

    def check_comment(self, index):
        logging.info('==========add_new==========')
        self.search_slide(index)

        if self.get_element_result('//android.widget.Button'):
            self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()

    def delete_comment(self):  # 删除备注
        logging.info('==========edit_comment==========')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_note_body_delete_note').click()

    def edit_comment(self, comment):  # 编辑备注
        logging.info('==========edit_comment==========')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_note_body_edit_note').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_et').set_text(comment)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_ok').click()

    def add_comment(self, index, comment):  # 插入备注
        logging.info('==========add_comment==========')
        self.search_slide(index)

        if not self.get_element_result('//*[@text="备注"]'):
            self.group_button_click('插入')
        self.driver.find_element(By.XPATH, '//*[@text="备注"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_et').set_text(comment)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_ok').click()


if __name__ == '__main__':
    for i in range(12):
        print(i)
