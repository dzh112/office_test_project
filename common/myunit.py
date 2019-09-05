import unittest

from airtest.core.api import connect_device

from businessView.openView import OpenView
from common.desired_caps import appium_desired
import logging
from time import sleep

from common.start import start_server, stop_server


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info('=====setUpClass=====')
        start_server()

    @classmethod
    def tearDownClass(cls):
        logging.info('=====tearDownClass=====')
        stop_server()

    def setUp(self):
        logging.info('=====setUp====')
        ov = OpenView(self)
        connect_device(ov.get_phone_dev())
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        self.driver.close_app()
