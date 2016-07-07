#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-22 
# Time: 下午7:34
#
from shutil import move
from zipfile import BadZipfile
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from analysis.src.sqlmodels import Base
from androguard.core.analysis import analysis
from androguard.core.analysis.analysis import VMAnalysis
from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from analysis.src.ad_detect import AdDetect
from analysis.src.eval_risk import eval_risk
from analysis.src.md5 import getFileMD5
from analysis.src.permissions import Permission


class ApkAnalysis:
    # filepath    path of the apks
    # engine      the sqlalchemy sql engine
    # curdir      the dir of the workspace
    #
    # mode        ApkAnalysis contains 3 modes
    #
    #             0 -- lite   : all the dex files of the apks will not be analysis , this
    #                           guarantees the running speed to be fast
    #             1 -- medium : the analyze of the dex file is decided by the permission red flag
    #             2 -- deep   : all the dex files will be analysed, NOTICE!!!, this will take a long
    #                           time
    # returns     start_analysis() returns a tuple containing all the data App() needs

    def __init__(self, filepath, curdir, mode):
        self.filepath = filepath

        self.permission_count = []
        self.ad_count = []
        self.minsdk_count = []
        self.obf_count = []

        self.curdir = curdir

        self.mode = self.check_mode(mode)

    def start_analysis(self):

        ####################################################

        # count the use of each permission
        self.permission_count = [0 for i in range(131)]

        # count the use of each ad SDK
        self.ad_count = [0 for i in range(37)]

        # count the use of each android sdk (min)
        self.minsdk_count = [0 for i in range(6)]

        # count the use of obfuscation tech
        self.obf_count = [0 for i in range(4)]

        #####################################################

        permission_num_str = ''

        print 'analysis... %s ' % self.filepath

        try:
            apk = APK(self.filepath)
        except BadZipfile:
            print 'find a BadZip'
            # self.move_badfile('BadZipfile', self.filepath)
            return None
        except Exception, e:
            print e
            print 'find an Exception'
            # self.move_badfile('UnknownError', self.filepath)
            return None

        else:

            # pemission
            p = Permission()
            result = p.perms2nums(apk.get_details_permissions())

            k = 0
            for j in result:
                self.permission_count[j] += 1
                permission_num_str = permission_num_str + '.' + str(result[k])
                k += 1

            # md5
            if getFileMD5(self.filepath)[0] is not False:
                md5 = getFileMD5(self.filepath)[1]

            # AD Sdk
            try:
                ad_detect = AdDetect(apk.get_activities())
                ad_names = ad_detect.get_ad_name()
            except AttributeError:
                print 'find an AttributeError'
                ad_names_str = '/Error'
                self.save2log('AttributeError', self.filepath)
            except IndexError:
                print 'find an IndexError'
                ad_names_str = '/Error'
                self.save2log('IndexError', self.filepath)
            except Exception:
                print 'find an Exception'
                ad_names_str = '/Error'
                self.save2log('UnknownError', self.filepath)
            else:
                ad_names_str = ''
                for l in ad_names:
                    ad_names_str = ad_names_str + '/' + l[0]
                    self.ad_count[l[1]] += 1

            # package name
            package = apk.get_package()
            if len(package) > 95:
                package = 'fuck.you.stupid.developer'

            # app version
            try:
                androidversion_name = apk.get_androidversion_name()
            except KeyError:
                androidversion_name = '/Error'
            else:
                if len(androidversion_name) > 18:
                    androidversion_name = androidversion_name[0:18]

            # obfuscation
            try:
                # mode select
                if self.mode == 0:
                    obf1 = None
                    obf2 = None
                    obf3 = None
                    obf4 = None
                    obf_risk = 0
                elif self.mode == 1:
                    if p.isRedApk():
                        d = DalvikVMFormat(apk.get_dex())
                        dx = VMAnalysis(d)
                        da = DeepAnalysis(dx)
                        obf1 = da.has_crypto()
                        obf2 = da.has_dynamic()
                        obf3 = da.has_native()
                        obf4 = da.has_reflection()
                        self.obf_check(obf1, obf2, obf3, obf4)
                        obf_risk = da.get_risk()
                    else:
                        obf1 = None
                        obf2 = None
                        obf3 = None
                        obf4 = None
                        obf_risk = 0
                else:
                    d = DalvikVMFormat(apk.get_dex())
                    dx = VMAnalysis(d)
                    da = DeepAnalysis(dx)
                    obf1 = da.has_crypto()
                    obf2 = da.has_dynamic()
                    obf3 = da.has_native()
                    obf4 = da.has_reflection()
                    self.obf_check(obf1, obf2, obf3, obf4)
                    obf_risk = da.get_risk()
            except Exception:
                obf1 = None
                obf2 = None
                obf3 = None
                obf4 = None
                obf_risk = 0
                self.save2log('Dex Exception', self.filepath)

            risk = eval_risk(p.risk, p.red_risk, ad_detect.get_risk(), obf_risk)

            # min req sdk
            sdk = self.minsdk_check(apk.get_min_sdk_version())
            self.minsdk_count[sdk] += 1

            #

            bag_result = (package, androidversion_name, md5, permission_num_str, risk,
                          apk.get_min_sdk_version(), ad_names_str, obf1, obf2, obf3, obf4)

            return bag_result

    def getPermission_count(self):
        return self.permission_count

    def getAd_count(self):
        return self.ad_count

    def getMinsdk_count(self):
        return self.minsdk_count

    def getObf_count(self):
        return self.obf_count

    def save2log(self, exception_name, filepath):
        o = open(self.curdir + 'apk_exception\error.log', 'a')
        o.write(exception_name + ':   ' + filepath + '\n')
        o.close()

    def check_mode(self, mode):
        if mode > 2 or mode < 0:
            return 0
        else:
            return mode

    def minsdk_check(self, ver):
        if ver is None:
            ver = '1'
        ver = int(ver)
        if ver < 8:
            return 0  # Other
        elif ver == 8:
            return 1  # Froyo
        elif ver == 9 or ver == 10:
            return 2  # Gingerbread
        elif 10 < ver <= 13:
            return 3  # Honeybomb
        elif 14 < ver <= 15:
            return 4  # Ice Cream Sandwich
        else:
            return 5  # Jellybean

    def obf_check(self, obf1, obf2, obf3, obf4):
        if obf1:
            self.obf_count[0] += 1
        if obf2:
            self.obf_count[1] += 1
        if obf3:
            self.obf_count[2] += 1
        if obf4:
            self.obf_count[3] += 1

    def move_badfile(self, error_name, filepath):
        try:
            move(filepath, self.curdir + 'apk_exception\\' + error_name)
        except IOError:
            self.save2log('fuck!Cant move', self.filepath)
        else:
            self.save2log(error_name, self.filepath)


class DeepAnalysis:
    # Obfuscation dic
    ObfDic = {
        "REFLECTION": 0,  # presence of the reflection API
        "NATIVE": 0,  # presence of loading a shared library
        "DYNAMIC": 0,  # presence of loading dynamically a new dex file
        "CRYPTO": 0,  # presence of crypto functions
    }

    def __init__(self, dx):
        self.dx = dx
        self.risk = 0

    def getObf(self):

        self.ObfDic['REFLECTION'] = int(analysis.is_reflection_code(self.dx))
        self.ObfDic['NATIVE'] = int(analysis.is_native_code(self.dx))
        self.ObfDic['DYNAMIC'] = int(analysis.is_dyn_code(self.dx))
        self.ObfDic['CRYPTO'] = int(analysis.is_crypto_code(self.dx))

        return self.ObfDic

    #
    def has_reflection(self):
        if analysis.is_reflection_code(self.dx):
            self.risk += 1
            return True
        else:
            return False

    def has_native(self):
        if analysis.is_native_code(self.dx):
            self.risk += 1
            return True
        else:
            return False

    def has_dynamic(self):
        if analysis.is_dyn_code(self.dx):
            self.risk += 1
            return True
        else:
            return False

    def has_crypto(self):
        if analysis.is_crypto_code(self.dx):
            self.risk += 1
            return True
        else:
            return False

    def get_risk(self):
        return self.risk

    def format2Str(self):
        str = ''
        for (key, value) in self.ObfDic.iteritems():
            if value == 1:
                str = str + '/' + key
            else:
                pass
        return str


# for main program linking to the database and create the table structure
def first_to_run(link):
    # link to the mysql
    mysql_engine = create_engine(link, echo=False)
    Base.metadata.create_all(mysql_engine)

    # Session = sessionmaker(bind=mysql_engine)
    # session = Session()
    #
    # a = App('com.apk_analysis.test', None, None, None, None, None, None, None, None, None, None)
    # session.add(a)
    # session.commit()

    return mysql_engine


def test2():
    a = ApkAnalysis("D:/temp/BaiduYun_4.3.0.apk", None, 2)
    print a.start_analysis()
    print a.getPermission_count()


if __name__ == '__main__':
    # a = APK("f:\Python Works\Apk Analysis\\test\\5.apk")
    # d = DalvikVMFormat(a.get_dex())
    # print a.package
    # dx = VMAnalysis(d)
    # da = DeepAnalysis(dx)
    # print da.getObf()
    test2()
