import logging
from common.common_fun import Common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By


class LoginView(Common):
    # username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    # password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    # loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    RightButton = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    username_type = (By.ID, 'com.yozo.office:id/et_account')
    password_type = (By.ID, 'com.yozo.office:id/et_pwd')
    loginBtn = (By.ID,'com.yozo.office:id/btn_login')

    logoutBtn = (By.ID, 'com.yozo.office:id/ll_myinfo_sure')
    doubleSure = (By.ID, 'com.yozo.office:id/btn_sure')
    back = (By.ID, 'com.yozo.office:id/iv_add_back')

    def login_action(self, username, password):
        logging.info('==========login_action==========')
        self.driver.find_element(By.ID,'com.yozo.office:id/ll_myinfo_unlogin').click()
        self.driver.implicitly_wait(3)
        logging.info('username is:%s' % username)
        self.find_element(*self.username_type).set_text(username)  # 输入手机号

        logging.info('password is:%s' % password)
        self.find_element(*self.password_type).set_text(password)  # 输入密码

        logging.info('click loginBtn')
        self.find_element(*self.loginBtn).click()  # 点击登录按钮
        logging.info('login finished!')

    def check_login_status(self):
        logging.info('==========check_login_status==========')
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_login')
        except NoSuchElementException:
            logging.error('login fail')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            return True

    def logout_action(self):
        logging.info('==========logout_action==========')
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.doubleSure).click()
        logging.info('logout finished!')
        # self.driver.keyevent(4)
        self.driver.find_element(*self.back).click()

    # def login_action(self, username, password):
    #     self.check_cancelBtn()
    #     self.check_skipBtn()
    #
    #     logging.info('============login_action==============')
    #     logging.info('username is:%s' % username)
    #     self.driver.find_element(*self.username_type).send_keys(username)
    #
    #     logging.info('password is:%s' % password)
    #     self.driver.find_element(*self.password_type).send_keys(password)
    #
    #     logging.info('click loginBtn')
    #     self.driver.find_element(*self.loginBtn).click()
    #     logging.info('login finished!')

    def check_account_alert(self):
        logging.info('=====check_account_alert====')
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip_commit')
            element.click()

    # def check_loginStatus(self):
    #     logging.info('====check_loginStatus======')
    #     self.check_market_ad()
    #     self.check_account_alert()
    #
    #     try:
    #
    #         self.driver.find_element(*self.button_mysefl).click()
    #         self.driver.find_element(*self.username)
    #     except NoSuchElementException:
    #         logging.error('login Fail!')
    #         self.getScreenShot('login fail')
    #         return False
    #     else:
    #         logging.info('login success!')
    #         self.logout_action()
    #         return True

    # def logout_action(self):
    #     logging.info('=====logout_action======')
    #     self.driver.find_element(*self.RightButton).click()
    #     self.driver.find_element(*self.logoutBtn).click()
    #     self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('自学网2018', 'zxw2018')
    # l.login_action('自学网2018','34454')
    l.check_loginStatus()
