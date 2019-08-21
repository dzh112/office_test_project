import time

from common.common_fun import Common
from selenium.webdriver.common.by import By


class WpCommonView(Common):
    toolbar_button = (By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode')  # 编辑签批切换
    option_group_button = (By.ID, 'com.yozo.office:id/yozo_ui_option_group_button')  # 菜单项
    option_expand_button = (By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button')  # 展开菜单栏
    font_name = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_font_name')  # 设置字体类型
    system1 = (By.XPATH, '//android.widget.TextView[@text="系统"]')  # 系统字体
    system2 = (By.ID, 'com.yozo.office:id/yozo_ui_option_title_container')  # 字体标题
    system3 = (By.ID, 'com.yozo.office:id/label_text_view')  # 字体列表
    reduce_size = (By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left')  # 缩小字号
    enlarge_size = (By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right')  # 放大字号
    high_light = (By.XPATH, '//android.widget.TextView[@text="高亮颜色"]')
    line_space = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_para_line_space')

    def switch_edit(self):
        # 切换编辑/阅读
        time.sleep(2)
        self.driver.find_element(*self.toolbar_button).click()
        # 展开菜单栏
        self.driver.find_element(*self.option_expand_button).click()

    def fonts_list(self):
        self.driver.find_element(*self.font_name).click()
        s1 = self.driver.find_element(*self.system1)
        s2 = self.driver.find_element(*self.system2)
        # self.driver.drag_and_drop(s1, s2)
        self.driver.scroll(s1, s2)
        while True:
            for i in self.driver.find_elements(*self.system3)[1:]:
                i.click()
                time.sleep(0.5)
            old_start_list = self.driver.find_elements(*self.system3)[1].text
            old_end_list = self.driver.find_elements(*self.system3)[-1].text
            self.driver.scroll(self.driver.find_elements(*self.system3)[-1], self.driver.find_elements(*self.system3)[1])
            new_start_list = self.driver.find_elements(*self.system3)[1].text
            new_end_list = self.driver.find_elements(*self.system3)[-1].text
            if old_start_list == new_start_list and old_end_list == new_end_list:
                break

    def fonts_size_list(self):
        size1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_recycler_view')
        # 第一种方法
        # for i in range(int(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[0].text)-5+1):
        #     self.driver.find_element(*self.reduce_size).click()
        #
        # for i in range(50+1-int(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[-1].text)):
        #     self.driver.find_element(*self.enlarge_size).click()
        # 第二种方法
        while True:
            self.driver.find_element(*self.reduce_size).click()
            if int(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[0].text) == 5:
                self.driver.find_element(*self.reduce_size).click()
                break
        while True:
            self.driver.find_element(*self.enlarge_size).click()
            if int(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[-1].text) == 50:
                self.driver.find_element(*self.enlarge_size).click()
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

    def fonts_high_light(self):
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.reduce_size))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_highlight_color')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s1.find_element(By.XPATH, "//*[@class='android.widget.ImageView']").click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def fonts_bullet(self):
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.system2))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_item_bullets_numbers')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s1.find_element(By.XPATH, "//*[@class='android.widget.ImageView']").click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def align_indent(self):
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.system2))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_para_hor_align')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()
        s2 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_para_indent')
        for i in s2.find_elements(By.XPATH, "//*[@class='android.widget.ImageView']"):
            i.click()

    def column(self):
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.system2))
        s1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_columns')
        for i in s1.find_elements(By.XPATH, "//*[@class='android.widget.RadioButton']"):
            i.click()

    def line_space_size(self):
        self.driver.scroll(self.driver.find_element(*self.high_light), self.driver.find_element(*self.system2))
        self.driver.find_element(*self.line_space).click()
        size1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_recycler_view')
        while True:
            self.driver.find_element(*self.reduce_size).click()
            if float(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[0].text) == 0.25:
                self.driver.find_element(*self.reduce_size).click()
                break
        while True:
            self.driver.find_element(*self.enlarge_size).click()
            if float(size1.find_elements(By.XPATH, "//*[@class='android.widget.TextView']")[-1].text) == 6.00:
                self.driver.find_element(*self.enlarge_size).click()
                break
