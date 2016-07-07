#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-25 
# Time: 下午10:53
#
import os
import threading
from time import sleep
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from analysis.src.apk_analysis_module_2 import ApkAnalysis, first_to_run
from analysis.src.sqlmodels import Result, App, Base
from analysis.src.stopwatch import Stopwatch

total_time = []

############################################

# count the use of each permission
permission_count = [0 for i in range(131)]

# count the use of each ad SDK
ad_count = [0 for i in range(37)]

# count the use of each android sdk (min)
minsdk_count = [0 for i in range(6)]

# count the use of obfuscation tech
obf_count = [0 for i in range(4)]

#############################################


class AnalysisThread(threading.Thread):
    def __init__(self, filepaths, total_length, engine, curdir, mode):
        threading.Thread.__init__(self)
        self.filepaths = filepaths
        self.total_length = total_length
        self.engine = engine
        self.curdir = curdir
        self.mode = mode
        self.elapsedTime = 0.0

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.len_paths = len(filepaths)

    def run(self):
        sleep(0.01)
        global total_time, permission_count
        timer = Stopwatch()

        k = 0
        for path in self.filepaths:
            a = ApkAnalysis(path, self.curdir, self.mode)
            bag = a.start_analysis()
            try:
                self.session.query(App).filter_by(md5=bag[2]).one()
            except TypeError:
                print 'bad file'
            except NoResultFound:
                app = App(bag)
                self.session.add(app)
                self.session_commit(k)
                k += 1
                print 'success by ' + self.name

                ############################################################

                for i in range(131):
                    if a.getPermission_count()[i] is not 0:
                        permission_count[i] += a.getPermission_count()[i]
                    else:
                        pass

                for i in range(37):
                    ad_count[i] += a.getAd_count()[i]

                for i in range(6):
                    minsdk_count[i] += a.getMinsdk_count()[i]

                for i in range(4):
                    obf_count[i] += a.getObf_count()[i]

                ############################################################
            else:
                print path + ' already in the database'

        print permission_count
        print ad_count
        print minsdk_count
        print obf_count

        r = Result(format2Str(permission_count), format2Str(ad_count), format2Str(minsdk_count), format2Str(obf_count))

        Base.metadata.create_all(self.engine)

        self.session.query(Result).filter(Result.id == 1).delete()
        self.session.add(r)
        self.session.commit()

        total_time.append(timer.elapsedTime())
        print total_time[-1] / self.total_length
        print self.name + ' finished'

    def session_commit(self, i, commit_num=200):
        if i % commit_num is 0 and i is not 0:
            self.session.commit()
            print '%s commit' % self.name
        elif i == self.len_paths - 1:
            self.session.commit()
            print '%s commit' % self.name


def format2Str(intobj):
    strobj = ''
    for i in range(len(intobj)):
        strobj = strobj + '.' + str(intobj[i])
    return strobj



# if __name__ == '__main__':
#     mysql_link = 'mysql://root:12345678@localhost/android_app_info'
#     engine = first_to_run(mysql_link)
#
#     thread_num = 2
#
#     curdir = os.getcwd().rstrip('src')
#     print 'current work dir is ' + curdir
#
#     apk_dir = 'e:\GoogleMarket\APPLICATION\Comics'
#
#     filepaths = get_filepaths(apk_dir)
#
#     a = AnalysisThread(filepaths, 1, engine, curdir, 1)
#     a.start()





