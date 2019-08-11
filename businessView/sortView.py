#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from functools import reduce

from selenium.webdriver.common.by import By

from common.common_fun import Common


class SortView(Common):

    def sort_file(self, type='time', sort='down'):
        # type =  ['type','name','size','time'] #可选择的排序类型
        # sort = ['up','down']  #升序还是降序
        logging.info('==========sort_file_%s_%s==========' % (type, sort))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_shot').click()
        logging.info('sorted by %s' % type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/rl_sort_%s' % type).click()
        logging.info('sort with %s' % sort)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sort_%s' % sort).click()
        logging.info('sort finish')
        self.driver.implicitly_wait(5)

    def check_sort_file(self, type='time', sort='down'):
        logging.info('==========check_sort_file_%s_%s==========' % (type, sort))
        ele_id = '//android.widget.TextView[@resource-id="com.yozo.office:id/tv_title"]'
        attr = 'name'
        ele_text = self.get_elements_attribute(ele_id, attr)
        print(ele_text)
        if type == 'type':
            logging.info('check sort with type')
            type_sort = ['doc', 'xls', 'ppt', 'pdf']
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
        if type == 'name':
            logging.info('check sort with name')
            ele_list = sorted(ele_text)
            if sort == 'down':
                ele_list.reverse()
            print(ele_list)
            if ele_text == ele_list:
                logging.info('%s with %s sort success' % (type, sort))
                return True
            else:
                logging.error('%s with %s sort fail' % (type, sort))
                self.getScreenShot('%s with %s sort fail' % (type, sort))
                return False
        if type == 'time':
            logging.info('check sort with time')
            ele_id = '//android.widget.TextView[@resource-id="com.yozo.office:id/tv_time"]'
            ele_time = self.get_elements_attribute(ele_id, attr)
            time_list = sorted(ele_time)
            if sort == 'down':
                time_list.reverse()
            if ele_time == time_list:
                logging.info('%s with %s sort success' % (type, sort))
                return True
            else:
                logging.error('%s with %s sort fail' % (type, sort))
                self.getScreenShot('%s with %s sort fail' % (type, sort))
                return False


if __name__ == '__main__':
    time_list = ['2019-07-02 上午09:23', '2019-07-02 上午09:25', '2019-07-01 下午09:11']
    print(time_list)
    time_list.sort()
    print(time_list)
    # type_sort = ['doc', 'xls', 'ppt', 'pdf']
    # type_sort = ['doc', 'pdf', 'ppt', 'xls']
    # print(type_sort)
    # # type_sort.reverse()
    # ss = sorted(type_sort)
    # print(ss)
    # print(ss == type_sort)
    # eles = ['0045.doc', '00056.pdf', '456.docx', '7897.xls', '456s.docx']
    # eles_suffix = list(map(lambda x: x[x.index('.') + 1:], eles))
    # eles_suffix1 = list(map(lambda x: x[:-1] if x[-1] == 'x' else x, eles_suffix))
    # single_suffix = reduce(lambda x, i: x if i in x else x + [i], [[], ] + eles_suffix1)
    # print(eles_suffix)
    # print(eles_suffix1)
    # print(single_suffix)
    # e = list(enumerate(single_suffix))
    # print(e)
    # type_sort = ['doc', 'xls', 'ppt', 'pdf']
    # sort = 'up'
    # sort = 'down'
    # sub_sort = [ 'xls', 'ppt', 'pdf']
    # sub_sort = ['pdf', 'ppt', 'doc']
    # sort_index = []
    # result = True
    # if sort == 'down':
    #     # sub_sort = reversed(sub_sort)
    #     sub_sort.reverse()
    # print('++++++++++++')
    # print(sub_sort)
    # [sort_index.append(type_sort.index(i)) for i in sub_sort if i in type_sort]
    # print(sort_index)
    # # for i in sub_sort:
    # #     if i in type_sort:
    # #         sort_index.append(type_sort.index(i))
    # # print(sort_index)
    # for i in range(len(sort_index) - 2):
    #     if sort_index[i] < sort_index[i + 1]:
    #         result = True
    #     else:
    #         result = False
    #         break
    # print(result)
