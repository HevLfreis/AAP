#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-8-13 
# Time: 上午10:29
#
import os
import win32file
import win32con
from analysis.src.link_prepare import analysis_in_threads


def watcher_win(path_for_watch, mysql_engine, curdir, mode):
    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }
    # Thanks to Claudio Grondi for the correct set of numbers
    FILE_LIST_DIRECTORY = 0x0001

    path_to_watch = path_for_watch
    hDir = win32file.CreateFile(
        path_to_watch,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
    )
    file2deal = []
    while 1:
        #
        # ReadDirectoryChangesW takes a previously-created
        # handle to a directory, a buffer size for results,
        # a flag to indicate whether to watch subtrees and
        # a filter of what changes to notify.
        #
        # NB Tim Juchcinski reports that he needed to up
        # the buffer size to be sure of picking up all
        # events when a large number of files were
        # deleted at once.
        #
        results = win32file.ReadDirectoryChangesW(
            hDir,
            1024,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
            win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
            win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
            win32con.FILE_NOTIFY_CHANGE_SIZE |
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
            win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None
        )
        for action, file in results:
            full_filename = os.path.join(path_to_watch, file)
            print full_filename, ACTIONS.get(action, "Unknown")
            if ACTIONS.get(action, "Unknown") == 'Created':
                file2deal.append(full_filename)

        # analyze every 20 new apk files
        if len(file2deal) is 1:
            print "new analysis begins"
            thread_num = 1
            threads = analysis_in_threads(file2deal, thread_num, mysql_engine, curdir, mode)
            for i in range(thread_num):
                threads[i].start()
            file2deal = []


if __name__ == '__main__':
    watcher_win('D:\\temp\\')