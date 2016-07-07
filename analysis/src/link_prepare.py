#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-27 
# Time: 下午8:36
#
import os
from analysis.src.thread_engine_2 import AnalysisThread


def get_filepaths(apk_dir):
    if os.path.isfile(apk_dir):
        return
    filepaths = []

    for i in os.listdir(apk_dir):
        mydir = apk_dir + '\\' + i
        if os.path.isdir(mydir):
            filepaths += get_filepaths(mydir)
        else:
            filepaths.append(mydir)
    return filepaths


def analysis_in_threads(filepaths, thread_num, engine, curdir, mode):
    length = len(filepaths)

    print 'total_num = %s' % length

    my_thread = []

    tem = path_divider(filepaths, thread_num)

    for i in range(thread_num):
        my_thread.append(AnalysisThread(tem[i], length, engine, curdir, mode))

    return my_thread


def path_divider(filepaths, num):

    path_divided = []
    for i in range(num):
        path_divided.append([])
    # print path_divided

    i = len(filepaths) - 1
    # print i
    while i >= 0:
        for j in range(num):
            if i is -1:
                break
            else:
                path_divided[j].append(filepaths[i])
                # print filepaths[i]
                i -= 1

    return path_divided

if __name__ == '__main__':
    path_divider(None, 4)