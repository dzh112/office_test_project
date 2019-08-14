#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest

from businessView.cloudView import CloudView

from businessView.selectView import SelectView
from businessView.sortView import SortView
from common.myunit import StartEnd
from common.tool import *


class TestCloud(StartEnd):
    csv_file = '../data/account.csv'

    def test_cloud_login(self):
        logging.info('======test_cloud=====')
        # 云文档登录
        sv = SelectView(self.driver)
        cv = CloudView(self.driver)
        sv.select_index('cloud')
        login_state = cv.exist("//*[@resource-id='com.yozo.office:id/btn_logo']")
        print("====%s=====" % login_state)
        if login_state:
            data1 = cv.get_csv_data(self.csv_file, 4)
            cv.cloud_login_action(username=data1[0], password=data1[1])
        self.assertTrue(cv.exist("//*[@text='自动上传']"), msg='Cloud login fail!')

    def test_cloud_create_new_folder(self):
        self.test_cloud_login()
        # 新建文件夹
        cv = CloudView(self.driver)
        new_folder_name = time.strftime("%Y%m%d%H%M%S")
        cv.cloud_new_folder(new_folder_name)
        self.assertTrue(cv.exist("//*[@text='%s']" % new_folder_name), msg='New folder fail!')

    def test_cloud_time_up(self):
        self.test_cloud_login()
        # 按时间升序排序
        stv = SortView(self.driver)
        type, sort = 'time', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))

    def test_cloud_time_down(self):
        self.test_cloud_login()
        # 按时间降序排序
        stv = SortView(self.driver)
        type, sort = 'time', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))

    def test_cloud_type_up(self):
        self.test_cloud_login()
        # 按类型升序排序
        stv = SortView(self.driver)
        type, sort = 'type', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))

    def test_cloud_type_down(self):
        self.test_cloud_login()
        # 按类型降序排序
        stv = SortView(self.driver)
        type, sort = 'type', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))

    def test_cloud_name_up(self):
        self.test_cloud_login()
        # 按类型降序排序
        stv = SortView(self.driver)
        type, sort = 'name', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))

    def test_cloud_name_down(self):
        self.test_cloud_login()
        # 按类型降序排序
        stv = SortView(self.driver)
        type, sort = 'name', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort))

    def test_cloud_folder_pop(self):
        self.test_cloud_login()
        # 前提 此时云文档内已存在文件夹和office文档
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        # 重命名文件夹
        rename_folder = cv.cloud_rename_folder(index=count - 2)
        self.assertTrue(cv.exist("//*[@text='%s']" % rename_folder), msg='Rename folder fail!')
        # 复制文件夹

        # 删除文件夹
        delete_name = cv.cloud_delete_new_folder(index=count - 2)
        self.assertFalse(cv.exist("//*[@text='%s']" % delete_name), msg='Delete folder fail!')

    def test_cloud_file_download(self):
        self.test_cloud_login()
        # 云文档下载
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        cv.cloud_download_file(count)
        # self.assertTrue(cv.get_toast_message('文件下载成功'), msg='Cloud file download fail!')
        self.assertTrue(cv.exist("//*[@text='文件下载成功']"), msg='Cloud file download fail!')

    def test_cloud_file_delete(self):
        self.test_cloud_login()
        # 云文档删除
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        delete_file = cv.cloud_delete_file(count)
        self.assertFalse(cv.exist("//*[@text='%s']" % delete_file), msg='Cloud file delete fail!')

    def test_cloud_file_rename(self):
        self.test_cloud_login()
        # 云文档重命名
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        rename_file = cv.cloud_rename_file(count)
        self.assertTrue(cv.exist("//*[@text='%s']" % rename_file), msg='Cloud file rename fail!')

    def test_cloud_file_share(self):
        self.test_cloud_login()
        # 云文档分享
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        cv.cloud_share_file(count)
        self.assertTrue(cv.exist("//*[@resource-id='com.yozo.office:id/ll_share']"), msg='Cloud file share fail!')

    def test_cloud_file_info(self):
        self.test_cloud_login()
        # 云文档信息获取
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        cv.cloud_file_info(count)
        self.assertTrue(cv.exist("//*[@resource-id='com.yozo.office:id/tv_fileloc']"), msg='Cloud file info get fail!')

    def test_cloud_file_copy(self):
        self.test_cloud_login()
        # 云文档复制
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        cv.cloud_copy_file(count)
        self.assertTrue(cv.exist("//*[@text='操作成功']"), msg='Cloud file copy fail!')


if __name__ == '__main__':
    unittest.main()
