#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-23 
# Time: 下午8:49
# Input file path output md5 of the file
import hashlib


def getFileMD5(strFile):
    file = None
    strMd5 = ''

    try:
        file = open(strFile, 'rb')
        md5 = hashlib.md5()
        while True:
            strRead = file.read(8096)
            if not strRead:
                break
            md5.update(strRead)
            #read file finish
        bRet = True
        strMd5 = md5.hexdigest()
    except IOError:
        bRet = False
    finally:
        if file:
            file.close()

    return [bRet, strMd5]


def getFileMD5fromfile(file):
    strMd5 = ''

    try:
        md5 = hashlib.md5()
        while True:
            strRead = file.read(8096)
            if not strRead:
                break
            md5.update(strRead)
            #read file finish
        bRet = True
        strMd5 = md5.hexdigest()
    except IOError:
        bRet = False
    finally:
        if file:
            file.close()

    return [bRet, strMd5]

if "__main__" == __name__:
    print(getFileMD5("f:\Python Works\Apk Analysis\Test\\1.apk"))
