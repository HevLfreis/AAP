#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-24 
# Time: 下午7:50
# Timer
import time


class Stopwatch:
    def __init__(self):
        self.time = time.time()

    def elapsedTime(self):
        return time.time() - self.time