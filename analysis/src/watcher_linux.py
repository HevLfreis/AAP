#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-8-13 
# Time: 下午7:13
# 
# from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE, IN_CREATE, IN_CLOSE_WRITE, IN_MOVED_FROM, IN_MOVED_TO
# import signal
#
# def hand_hub(n=0, e=0):
#     print 'catch a hub SIGINT'
#
#
# class proc_evt(ProcessEvent):
#     def process_IN_CREATE(self, event):
#         print ('process_IN_CREATE, %s, %s, %s'%(event.path, event.name, event.maskname ))
#         str = event.maskname
#
#     def process_IN_DELETE(self, event):
#         print ('process_IN_DELETE, %s, %s, %s'%(event.path, event.name, event.maskname ))
#
#         str = event.maskname
#
#     def process_IN_CLOSE_WRITE(self, event):
#         print ('process_IN_CLOSE_WRITE, %s, %s, %s'%(event.path, event.name, event.maskname ))
#         str = event.maskname
#
#     def process_IN_MOVED_FROM(self, event):
#         print ('process_IN_MOVED_FROM, %s, %s, %s'%(event.path, event.name, event.maskname ))
#         str = event.maskname
#
#     def process_IN_MOVED_TO(self, event):
#         print ('process_IN_MOVED_TO, %s, %s, %s'%(event.path, event.name, event.maskname ))
#         str = event.maskname
#
# class notify(object):
#
#     def __init__(self, local_rootpath):
#         self.wm = WatchManager()
#         mask = IN_DELETE | IN_CREATE | IN_CLOSE_WRITE | IN_MOVED_FROM | IN_MOVED_TO
#
#         self.notifier = Notifier(self.wm, proc_evt())
#         self.wm.add_watch(local_rootpath, mask, rec = True)
#
#
#     def run(self):
#         signal.signal(signal.SIGHUP, hand_hub)
#
#         while (True):
#             try:
#                 self.notifier.process_events()
#                 if self.notifier.check_events():
#                     self.notifier.read_events()
#             except:
#                 self.notifier.stop()
#                 break