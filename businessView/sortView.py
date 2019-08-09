#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from functools import reduce

from selenium.webdriver.common.by import By

from common.common_fun import Common


class SortView(Common):

    def sort(self, type='time', sort='down'):
        # type =  ['type','name','size','time'] #可选择的排序类型
        # sort = ['up','down']  #升序还是降序
        logging.info('==========sort_%s_%s==========' % (type, sort))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_shot').click()
        logging.info('sorted by %s' % type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/rl_sort_%s' % type).click()
        logging.info('sort with %s' % sort)
        logging.info('sort finish')
        self.driver.implicitly_wait(5)

    def check_sort(self, type='time', sort='down'):
        logging.info('==========check_sort_%s_%s==========' % (type, sort))
        if type == 'type':
            logging.info('check sort with type')
            type_sort = ['doc', 'xls', 'ppt', 'pdf']
            ele_id = '//android.widget.TextView[@resource-id="com.yozo.office:id/tv_title"]'
            attr = 'name'
            ele_text = self.get_elements_attribute(ele_id, attr)
            eles_suffix = list(map(lambda x: x[x.rindex('.') + 1:].lower(), ele_text))  # 获取尾缀名
            eles_suffix1 = list(map(lambda x: x[:-1] if x[-1] == 'x' else x, eles_suffix))  # 尾缀名去'x'
            single_suffix = reduce(lambda x, i: x if i in x else x + [i], [[], ] + eles_suffix1)  # 尾缀去保证顺序不变去重
            len_suffix = len(single_suffix)
            sort_index = []
            if len_suffix == 1:
                logging.info('only one type!')
                return True
            else:
                if sort == 'down':
                    single_suffix.reverse()
                [sort_index.append(type_sort.index(i)) for i in single_suffix if i in type_sort]
                for i in range(len_suffix - 2):
                    if sort_index[i] > sort_index[i + 1]:
                        logging.error('%s with %s sort fail' % (type, sort))
                        self.getScreenShot('%s with %s sort fail' % (type, sort))
                        return False
                logging.info('%s with %s sort success' % (type, sort))
                return True


if __name__ == '__main__':
    # eles = ['0045.doc', '00056.pdf', '456.docx', '7897.xls', '456s.docx']
    # eles_suffix = list(map(lambda x: x[x.index('.') + 1:], eles))
    # eles_suffix1 = list(map(lambda x: x[:-1] if x[-1] == 'x' else x, eles_suffix))
    # single_suffix = reduce(lambda x, i: x if i in x else x + [i], [[], ] + eles_suffix1)
    # print(eles_suffix)
    # print(eles_suffix1)
    # print(single_suffix)
    # e = list(enumerate(single_suffix))
    # print(e)
    type_sort = ['doc', 'xls', 'ppt', 'pdf']
    # sort = 'up'
    sort = 'down'
    # sub_sort = [ 'xls', 'ppt', 'pdf']
    sub_sort = ['pdf', 'ppt', 'doc']
    sort_index = []
    result = True
    if sort == 'down':
        # sub_sort = reversed(sub_sort)
        sub_sort.reverse()
    print('++++++++++++')
    print(sub_sort)
    [sort_index.append(type_sort.index(i)) for i in sub_sort if i in type_sort]
    print(sort_index)
    # for i in sub_sort:
    #     if i in type_sort:
    #         sort_index.append(type_sort.index(i))
    # print(sort_index)
    for i in range(len(sort_index) - 2):
        if sort_index[i] < sort_index[i + 1]:
            result = True
        else:
            result = False
            break
    print(result)
