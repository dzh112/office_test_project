import random
from common.common_fun import Common
from selenium.webdriver.common.by import By


class WpLookUpView(Common):
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

    def self_adaption(self):
        # 点击自适应屏幕按钮
        self.driver.find_element(*self.self_adaption_icon).click()

    def switch_lookup(self):
        # 切换编辑/阅读
        self.driver.find_element(*self.toolbar_button).click()
        # 切换到查看菜单
        self.driver.find_element(*self.option_group_button).click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="查看"]').click()

    def wp_find_replace(self):
        # 查找关键字，并替换
        self.switch_lookup()
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
        self.switch_lookup()
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
        self.switch_lookup()
        self.driver.find_element(*self.wp_goto).click()
        self.driver.find_element(*self.goto_page).send_keys(random.randint(1, 6))
        self.driver.find_element(*self.goto_id_ok).click()
