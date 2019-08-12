#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from businessView.cloudView import CloudView

from businessView.selectView import SelectView
from common.myunit import StartEnd
from common.tool import *


class TestCloud(StartEnd):
    csv_file = '../data/account.csv'

    def test_cloud(self):
        logging.info('======test_cloud=====')
        sv = SelectView(self.driver)
        cv = CloudView(self.driver)
        sv.select_index('cloud')
        if cv.check_cloud_button():
            data1 = cv.get_csv_data(self.csv_file, 4)
            cv.cloud_login_action(username=data1[0], password=data1[1])
        self.assertTrue(cv.check_upload_folder(), msg='cloud login fail')


if __name__ == '__main__':
    unittest.main()
