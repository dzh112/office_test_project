#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import logging
import math
import operator
import os
from functools import reduce

import xlrd
from PIL import Image, ImageChops

from common.common_fun import Common
from common.desired_caps import appium_desired


class SaveView(Common):

    def img_unite(self,save_name):
        img1, img2 = Image.open('before_save.png'), Image.open('after_save.png')
        diff = ImageChops.difference(img1, img2)
        if diff.getbbox() is None:
            print("两张图片一样")
        else:
            diff.save('contrast.png')
            print("两张图片不一样")
        size1, size2, size3 = img1.size, img2.size, diff.size
        joint = Image.new('RGB', (size1[0] + size2[0] + size3[0], size1[1]))
        loc1, loc2, loc3 = (0, 0), (size1[0], 0), (size1[0] + size2[0], 0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.paste(diff, loc3)
        joint.save('../screenshots/%s.png' % save_name)
        # joint.save(get_project_path() + '\\ErrorCapture\\%s.png' % save_name)
        os.remove('before_save.png')
        os.remove('after_save.png')
        os.remove('contrast.png')

    def image_contrast(self):
        image1 = Image.open('before_save.png')
        image2 = Image.open('after_save.png')
        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        print(result)
        return result

    def ele_screenshots(self,ele, pic_name):
        left = ele.location['x']
        top = ele.location['y']
        right = ele.location['x'] + ele.size['width']
        bottom = ele.location['y'] + ele.size['height']
        im = Image.open(pic_name)
        im = im.crop((left, top, right, bottom))
        im.save(pic_name)

    def get_data(self,file_path, sheet_name,begin=0,end=5000):  # 获取A1开始第一列的数据
        file = xlrd.open_workbook(file_path, encoding_override="uft-8")
        sheet = file.sheet_by_name(sheet_name)
        # return sheet.col_values(0)[0:2499]
        return sheet.col_values(0)[begin:end]

if __name__ == '__main__':
    pass
    # driver = appium_desired()
    # l = SaveView(driver)
    # print(l.get_data('../data/need_run.csv',2))
