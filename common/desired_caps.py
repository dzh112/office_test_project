import xlrd
from appium import webdriver
import yaml
import logging
import logging.config
import os

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def get_data(file_path, sheet_name, begin=0, end=5000):  # 获取A1开始第一列的数据
    file = xlrd.open_workbook(file_path, encoding_override="uft-8")
    sheet = file.sheet_by_name(sheet_name)
    # return sheet.col_values(0)[0:2499]
    return sheet.col_values(0)[begin:end]


def appium_desired():
    with open('../config/yozo_office_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        print(data)
    desired_caps = data['desired_caps']
    # desired_caps['platformName']=data['platformName']
    # desired_caps['platformVersion']=data['platformVersion']
    # desired_caps['deviceName']=data['deviceName']
    #
    # #app属性 值为绝对路径，如果有appActivity和appPackage则不需要此属性
    # base_dir = os.path.dirname(os.path.dirname(__file__)) #项目绝对路径
    # app_path = os.path.join(base_dir, 'app', data['appname'])
    # desired_caps['app']=app_path
    #
    # desired_caps['appPackage']=data['appPackage']
    # desired_caps['appActivity']=data['appActivity']
    # desired_caps['noReset']=data['noReset']
    #
    #
    # desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    # desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    # print( os.path.dirname(os.path.dirname(__file__)))
    appium_desired()

    # with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    #     data = yaml.load(file)
    #
    # base_dir=os.path.dirname(os.path.dirname(__file__))
    # print(os.path.dirname(__file__))
    # print(base_dir)
    #
    # app_path=os.path.join(base_dir,'app',data['appname'])
    # print(app_path)
