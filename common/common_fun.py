from selenium.webdriver.support.wait import WebDriverWait

from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time, os
import csv


class Common(BaseView):

    def get_elements_attribute(self, elements, attr):
        logging.info('==========get_elements_attribute==========')
        try:
            # attr1 = (By.XPATH, '//*[@resource-id="%s"]' % elements)
            eles = self.driver.find_elements(By.XPATH, elements)
        except NoSuchElementException:
            logging.error("%s locate fail" % str(elements))
            self.getScreenShot("%s locate fail" % str(elements))
            raise
        else:
            logging.info("%s locate success" % str(elements))
            eles_attr = list(map(lambda x: x.get_attribute(attr), eles))
            return eles_attr

    def get_toast_message(self, toast_message):
        logging.info('==========get_toast_message==========')
        message = '//*[@text="' + toast_message + '"]'
        try:
            # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(By.XPATH, message))
            self.driver.find_element(By.XPATH, message)
        except NoSuchElementException:
            logging.error('get toast message: %s fail!' % toast_message)
            return False
        else:
            logging.info('get toast message: %s success!' % toast_message)
            return True

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def exist(self, element):
        try:
            self.find_element(By.XPATH, element)
        except NoSuchElementException:
            logging.info('=====%s element not exist!======' % element)
            return False
        else:
            logging.info('=====%s element exist!======' % element)
            return True

    @staticmethod
    def clear_special_str(a):
        c = ['.', '_', '-']
        for i in c:
            a = a.replace(i, '')
        return a


if __name__ == '__main__':
    # driver=appium_desired()
    # com=Common(driver)
    # com.check_cancelBtn()
    # # com.check_skipBtn()
    # com.swipeLeft()
    # com.getScreenShot('startApp')

    list = ["这", "是", "一个", "测试", "数据"]
    # for i in range(len(list)):
    # print(i, list[i])

    list1 = ["这", "是", "一个", "测试", "数据"]
    # for index, item in enumerate(list1):
    #     print(index, item)
