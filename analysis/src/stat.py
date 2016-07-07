#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/12 
# Time: 19:10
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from analysis.src.apk_analysis_module_2 import ApkAnalysis
from analysis.src.sqlmodels import Base, App, Result
from analysis.dict.ad_dic import ADMODULE


def format2Str(intobj):
    strobj = ''
    for i in range(len(intobj)):
        strobj = strobj + '.' + str(intobj[i])
    return strobj


permission_count = [0]
for i in range(130):
    permission_count.append(0)

ad_count = [0]
for i in range(36):
    ad_count.append(0)

minsdk_count = [0]
for i in range(5):
    minsdk_count.append(0)

obf_count = [0]
for i in range(3):
    obf_count.append(0)

mysql_link = 'mysql://root:12345678@127.0.0.1/android_app_info_all'


mysql_engine = create_engine(mysql_link, echo=False)
Base.metadata.create_all(mysql_engine)
Session = sessionmaker(bind=mysql_engine)
session = Session()

apps = session.query(App).all()
a = ApkAnalysis(None, None, None)

for app in apps:
    for num in app.permission_num_str.lstrip('.').split('.'):
        if num != '':
            permission_count[int(num)] += 1


    for mod in app.ad_SDK.lstrip("/").split("/"):
        if mod != '':
            for k, ads in ADMODULE.items():
                # print mod, ads[0]
                if mod == ads[0]:

                    ad_count[ads[2]] += 1

    minsdk_count[a.minsdk_check(app.minSDKversion)] += 1

    if app.CRYPTO:
        obf_count[0] += 1
    if app.DYNAMIC:
        obf_count[1] += 1
    if app.NATIVE:
        obf_count[2] += 1
    if app.REFLECTION:
        obf_count[3] += 1


print permission_count
print ad_count
print minsdk_count
print obf_count

r = Result(format2Str(permission_count), format2Str(ad_count), format2Str(minsdk_count), format2Str(obf_count))
session.add(r)
session.commit()




