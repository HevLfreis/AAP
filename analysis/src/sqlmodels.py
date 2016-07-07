#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/4 
# Time: 18:14
#
from sqlalchemy import Column, String, Boolean
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class App(Base):
    __tablename__ = 'table_main'

    id = Column(Integer, primary_key=True)
    packagename = Column(String(100))
    app_version = Column(String(20))
    md5 = Column(String(32))
    permission_num_str = Column(String(500))
    risk = Column(Integer)
    minSDKversion = Column(Integer)
    ad_SDK = Column(String(200))
    CRYPTO = Column(Boolean)
    DYNAMIC = Column(Boolean)
    NATIVE = Column(Boolean)
    REFLECTION = Column(Boolean)

    def __init__(self, (packagename, app_version, md5, permission_num_str, risk, minSDKversion, ad_SDK,
    CRYPTO, DYNAMIC, NATIVE, REFLECTION)):
        self.packagename = packagename
        self.app_version = app_version
        self.md5 = md5
        self.permission_num_str = permission_num_str
        self.risk = risk
        self.minSDKversion = minSDKversion
        self.ad_SDK = ad_SDK
        self.CRYPTO = CRYPTO
        self.DYNAMIC = DYNAMIC
        self.NATIVE = NATIVE
        self.REFLECTION = REFLECTION


class Result(Base):
    __tablename__ = 'table_result'

    id = Column(Integer)
    permission_num_str = Column(String(1000))
    ad_count_str = Column(String(200), primary_key=True)
    minsdk_count_str = Column(String(100))
    obf_count_str = Column(String(50))

    def __init__(self, permission_num_str, ad_num_str, minsdk_count_str, obf_count_str):
        self.id = 1
        self.permission_num_str = permission_num_str
        self.ad_count_str = ad_num_str
        self.minsdk_count_str = minsdk_count_str
        self.obf_count_str = obf_count_str
