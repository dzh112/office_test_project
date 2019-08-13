#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from businessView.cloudView import CloudView

from businessView.selectView import SelectView
from businessView.sortView import SortView
from common.myunit import StartEnd
from common.tool import *


class TestCloud(StartEnd):
    csv_file = '../data/account.csv'

    def test_cloud(self):
        logging.info('======test_cloud=====')
        # 云文档登录
        sv = SelectView(self.driver)
        cv = CloudView(self.driver)
        sv.select_index('cloud')
        if cv.check_cloud_button():
            data1 = cv.get_csv_data(self.csv_file, 4)
            cv.cloud_login_action(username=data1[0], password=data1[1])
        self.assertTrue(cv.check_upload_folder(), msg='Cloud login fail!')

        # 新建文件夹
        cv.cloud_new_folder("YOZO")
        self.assertTrue(cv.check_folder_name("YOZO"), msg='Folder create fail!')
        # 删除文件夹  无法定位到固定文件夹更多按钮
        # cv.cloud_delete_new_folder("YOZO")
        # 按时间升序排序
        stv = SortView(self.driver)
        type, sort = 'time', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))
        # 按时间降序排序
        type, sort = 'time', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))


if __name__ == '__main__':
    unittest.main()
