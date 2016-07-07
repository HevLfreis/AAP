#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-25 
# Time: 下午8:17
# Main program
import os
from analysis.src.apk_analysis_module_2 import first_to_run
from analysis.src.link_prepare import get_filepaths, analysis_in_threads
from analysis.src.watcher_win import watcher_win

# run only once !!!
mysql_link = 'mysql://root:12345678@127.0.0.1/android_app_info_all'
engine = first_to_run(mysql_link)

thread_num = 3

curdir = os.getcwd().rstrip('src')
print 'current work dir is ' + curdir

mode = 0

apk_dir = 'D:/temp'

# filepaths = get_filepaths(apk_dir)
#
# threads = analysis_in_threads(filepaths, thread_num, engine, curdir, mode)
#
# for i in range(thread_num):
#     threads[i].start()

watcher_win(apk_dir, engine, curdir, mode)









