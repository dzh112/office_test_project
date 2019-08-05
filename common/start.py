import logging

from appium import webdriver
import time
import yaml
import os


def start_server():
    logging.info('start appium')
    caps = get_desired_caps()
    port, udid = caps['port'], caps['desired_caps']['udid']
    cmd = os.popen('netstat -ano | findstr "%s" ' % port)
    msg = cmd.read()
    if "LISTENING" in msg:
        print("appium服务已经启动：%s" % msg)
    else:
        print("appium服务启动：%s" % msg)
        os.system("start /b appium -a 127.0.0.1 --session-override -p %s -U %s" % (port,udid))
        time.sleep(5)


def stop_server():
    port = get_desired_caps()['port']
    msg = os.popen('netstat -ano | findstr %s' % port)
    if msg:
        # pid = msg.read().split()[-1]
        msg.close()
        time.sleep(3)
        # os.system("start /b taskkill /F /PID %s" % pid)
        os.system("start /b taskkill /F /t /IM node.exe")
        print("kill successfully")
    else:
        print('进程未找到')

    # os.system("start /b taskkill /f /fi "imagename eq node.exe")


def get_desired_caps():
    yml_path = os.path.join("../config/yozo_office_caps.yaml")
    f = open(yml_path, "r", encoding="utf-8")
    dev_info = f.read()
    f.close()
    info = yaml.load(dev_info, Loader=yaml.FullLoader)
    # print(info)
    return info
    # for cap in info:
    #     # if devices_name in cap["desc"]:  # 判断输入的设备名称是否存在
    #     return  cap['port'],cap['desired_caps'],


# @threads(2)
def run_app():
    desired_caps = get_desired_caps()
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % desired_caps['port'], desired_caps['desired_caps'])
    time.sleep(3)
    # driver.implicitly_wait(3)
    return driver


if __name__ == "__main__":
    # cap = get_desired_caps()
    # sheet_name = cap['sheet_name']
    # print(cap)
    # print(sheet_name)
    # msg = os.popen('start /b adb connect 127.0.0.1:62001').read()
    # msg1 = os.popen('start /b adb connect 127.0.0.1:62001').read()
    # msg3 = os.popen('start /b adb connect %s' % '127.0.0.1:62025').read()
    # msg2 = os.popen('start /b adb disconnect 127.0.0.1:62001').read()
    # os.popen('start /b adb connect 127.0.0.1:62002').read()
    print('+++++++++')
    # print(int('0xae',10))
    # print(msg)
    # print(msg1)
    # print(msg2)
    # print(msg3)
    # os.system("start /b taskkill /F /t /IM node.exe")
    os.system("start /b appium -a 127.0.0.1 --session-override -p 4723 -bp 4724 -U 127.0.0.1:62001")
    time.sleep(5)
    cmd = os.popen('netstat -ano | findstr 4723')
    msg = cmd.read()
    print('msg:%s' % msg)
    print(type(msg))
    msgs = msg.split()
    print(msgs)
    print(msgs[-1])
    print(type(msgs))
    time.sleep(10)
    os.system("start /b taskkill /F /PID %s" % msgs[-1])

    # os.system("start /b taskkill /F /t /IM node.exe")

    # devices = ["deviceA"]
    # for i in devices:
    #     run_app(i)
    # time.sleep(10)
    # stop_server('deviceA')
    # cap = get_desired_caps('deviceA')
    # print(get_desired_caps('deviceA')[0]['deviceName'])
    # des,port = get_desired_caps('deviceA')
    # print(port)
    # print(des)
    pass
