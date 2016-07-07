#!/usr/bin/env python
# coding: utf-8
# created by haytham teng haytham_teng@foxmail.com 
# Date: 13-8-4 
# Time: 下午1:44
#
import random
import os
from analysis.src.md5 import getFileMD5
from analysis.src.apk_analysis_module_2 import ApkAnalysis
from table.models import Main, Result


def formatStr2Num(str):
    num_list = []
    str_list = str.split('.')
    for i in range(1, len(str_list)):
        num_list.append(int(str_list[i]))
    return num_list


def formatNum2Str(num_list):
    mystr = ''
    for i in range(len(num_list)):
        mystr = mystr + '.' + str(num_list[i])
    return mystr


def perm_top(perm_str, top_num=10):
    perm_num = formatStr2Num(perm_str)

    permDic = dict(ACCESS_CHECKIN_PROPERTIES=perm_num[0],
                   ACCESS_COARSE_LOCATION=perm_num[1],
                   ACCESS_FINE_LOCATION=perm_num[2],
                   ACCESS_LOCATION_EXTRA_COMMANDS=perm_num[3],
                   ACCESS_MOCK_LOCATION=perm_num[4],
                   ACCESS_NETWORK_STATE=perm_num[5],
                   ACCESS_SURFACE_FLINGER=perm_num[6],
                   ACCESS_WIFI_STATE=perm_num[7],
                   ACCOUNT_MANAGER=perm_num[8],
                   ADD_VOICEMAIL=perm_num[9],
                   AUTHENTICATE_ACCOUNTS=perm_num[10],
                   BATTERY_STATS=perm_num[11],
                   BIND_ACCESSIBILITY_SERVICE=perm_num[12],
                   BIND_APPWIDGET=perm_num[13],
                   BIND_DEVICE_ADMIN=perm_num[14],
                   BIND_INPUT_METHOD=perm_num[15],
                   BIND_REMOTEVIEWS=perm_num[16],
                   BIND_TEXT_SERVICE=perm_num[17],
                   BIND_VPN_SERVICE=perm_num[18],
                   BIND_WALLPAPER=perm_num[19],
                   BLUETOOTH=perm_num[20],
                   BLUETOOTH_ADMIN=perm_num[21],
                   BRICK=perm_num[22],
                   BROADCAST_PACKAGE_REMOVED=perm_num[23],
                   BROADCAST_SMS=perm_num[24],
                   BROADCAST_STICKY=perm_num[25],
                   BROADCAST_WAP_PUSH=perm_num[26],
                   CALL_PHONE=perm_num[27],
                   CALL_PRIVILEGED=perm_num[28],
                   CAMERA=perm_num[29],
                   CHANGE_COMPONENT_ENABLED_STATE=perm_num[30],
                   CHANGE_CONFIGURATION=perm_num[31],
                   CHANGE_NETWORK_STATE=perm_num[32],
                   CHANGE_WIFI_MULTICAST_STATE=perm_num[33],
                   CHANGE_WIFI_STATE=perm_num[34],
                   CLEAR_APP_CACHE=perm_num[35],
                   CLEAR_APP_USER_DATA=perm_num[36],
                   CONTROL_LOCATION_UPDATES=perm_num[37],
                   DELETE_CACHE_FILES=perm_num[38],
                   DELETE_PACKAGES=perm_num[39],
                   DEVICE_POWER=perm_num[40],
                   DIAGNOSTIC=perm_num[41],
                   DISABLE_KEYGUARD=perm_num[42],
                   DUMP=perm_num[43],
                   EXPAND_STATUS_BAR=perm_num[44],
                   FACTORY_TEST=perm_num[45],
                   FLASHLIGHT=perm_num[46],
                   FORCE_BACK=perm_num[47],
                   GET_ACCOUNTS=perm_num[48],
                   GET_PACKAGE_SIZE=perm_num[49],
                   GET_TASKS=perm_num[50],
                   GLOBAL_SEARCH=perm_num[51],
                   HARDWARE_TEST=perm_num[52],
                   INJECT_EVENTS=perm_num[53],
                   INSTALL_LOCATION_PROVIDER=perm_num[54],
                   INSTALL_PACKAGES=perm_num[55],
                   INTERNAL_SYSTEM_WINDOW=perm_num[56],
                   INTERNET=perm_num[57],
                   KILL_BACKGROUND_PROCESSES=perm_num[58],
                   MANAGE_ACCOUNTS=perm_num[59],
                   MANAGE_APP_TOKENS=perm_num[60],
                   MASTER_CLEAR=perm_num[61],
                   MODIFY_AUDIO_SETTINGS=perm_num[62],
                   MODIFY_PHONE_STATE=perm_num[63],
                   MOUNT_FORMAT_FILESYSTEMS=perm_num[64],
                   MOUNT_UNMOUNT_FILESYSTEMS=perm_num[65],
                   NFC=perm_num[66],
                   PERSISTENT_ACTIVITY=perm_num[67],
                   PROCESS_OUTGOING_CALLS=perm_num[68],
                   READ_CALENDAR=perm_num[69],
                   READ_CALL_LOG=perm_num[70],
                   READ_CONTACTS=perm_num[71],
                   READ_EXTERNAL_STORAGE=perm_num[72],
                   READ_FRAME_BUFFER=perm_num[73],
                   READ_HISTORY_BOOKMARKS=perm_num[74],
                   READ_INPUT_STATE=perm_num[75],
                   READ_LOGS=perm_num[76],
                   READ_PHONE_STATE=perm_num[77],
                   READ_PROFILE=perm_num[78],
                   READ_SMS=perm_num[79],
                   READ_SOCIAL_STREAM=perm_num[80],
                   READ_SYNC_SETTINGS=perm_num[81],
                   READ_SYNC_STATS=perm_num[82],
                   READ_USER_DICTIONARY=perm_num[83],
                   REBOOT=perm_num[84],
                   RECEIVE_BOOT_COMPLETED=perm_num[85],
                   RECEIVE_MMS=perm_num[86],
                   RECEIVE_SMS=perm_num[87],
                   RECEIVE_WAP_PUSH=perm_num[88],
                   RECORD_AUDIO=perm_num[89],
                   REORDER_TASKS=perm_num[90],
                   RESTART_PACKAGES=perm_num[91],
                   SEND_SMS=perm_num[92],
                   SET_ACTIVITY_WATCHER=perm_num[93],
                   SET_ALARM=perm_num[94],
                   SET_ALWAYS_FINISH=perm_num[95],
                   SET_ANIMATION_SCALE=perm_num[96],
                   SET_DEBUG_APP=perm_num[97],
                   SET_ORIENTATION=perm_num[98],
                   SET_POINTER_SPEED=perm_num[99],
                   SET_PREFERRED_APPLICATIONS=perm_num[100],
                   SET_PROCESS_LIMIT=perm_num[101],
                   SET_TIME=perm_num[102],
                   SET_TIME_ZONE=perm_num[103],
                   SET_WALLPAPER=perm_num[104],
                   SET_WALLPAPER_HINTS=perm_num[105],
                   SIGNAL_PERSISTENT_PROCESSES=perm_num[106],
                   STATUS_BAR=perm_num[107],
                   SUBSCRIBED_FEEDS_READ=perm_num[108],
                   SUBSCRIBED_FEEDS_WRITE=perm_num[109],
                   SYSTEM_ALERT_WINDOW=perm_num[110],
                   UPDATE_DEVICE_STATS=perm_num[111],
                   USE_CREDENTIALS=perm_num[112],
                   USE_SIP=perm_num[113],
                   VIBRATE=perm_num[114],
                   WAKE_LOCK=perm_num[115],
                   WRITE_APN_SETTINGS=perm_num[116],
                   WRITE_CALENDAR=perm_num[117],
                   WRITE_CALL_LOG=perm_num[118],
                   WRITE_CONTACTS=perm_num[119],
                   WRITE_EXTERNAL_STORAGE=perm_num[120],
                   WRITE_GSERVICES=perm_num[121],
                   WRITE_HISTORY_BOOKMARKS=perm_num[122],
                   WRITE_PROFILE=perm_num[123],
                   WRITE_SECURE_SETTINGS=perm_num[124],
                   WRITE_SETTINGS=perm_num[125],
                   WRITE_SMS=perm_num[126],
                   WRITE_SOCIAL_STREAM=perm_num[127],
                   WRITE_SYNC_SETTINGS=perm_num[128],
                   WRITE_USER_DICTIONARY=perm_num[129],
                   OTHERS=perm_num[130])

    s = sorted(permDic.iteritems(), key=lambda a: a[1], reverse=True)
    final_list = []
    for i in range(top_num):
        final_list.append(s[i])
    return final_list


def ad(ad_str):
    ad_num = formatStr2Num(ad_str)

    adDic = {'AdMob': ad_num[0], 'Baidu': ad_num[1], 'Youmi': ad_num[2], 'MobWin': ad_num[3], 'Wooboo': ad_num[4],
             'Casee': ad_num[5], 'Wiyun': ad_num[6], 'AdChina': ad_num[7], 'AdWo': ad_num[8], 'Wq': ad_num[9],
             'AppMedia': ad_num[10], 'Tinmoo': ad_num[11], 'LSense': ad_num[12], 'Winad': ad_num[13],
             'Izp': ad_num[14], 'Mobisage': ad_num[15], 'Umeng': ad_num[16], 'Fractalist': ad_num[17],
             'Lmmob': ad_num[18],
             'SuiZong': ad_num[19], 'Aduu': ad_num[20], 'MillennialMedia': ad_num[21], 'Greystripe': ad_num[22],
             'InMobi': ad_num[23], 'MdotM': ad_num[24], 'ZestADZ': ad_num[25], 'Smaato': ad_num[26], 'Waps': ad_num[27],
             'Wapscn': ad_num[28], 'Yijifen': ad_num[29], 'Juzi': ad_num[30], 'Adview': ad_num[31],
             'Adtouch': ad_num[32],
             'AirADad': ad_num[33], 'Vpon': ad_num[34], 'Domob': ad_num[35], 'GuoHead': ad_num[36]}
    return adDic


def minsdk(minsdk_str):
    minsdk_num = formatStr2Num(minsdk_str)

    minsdkDic = {'Unknown': minsdk_num[0], 'Froyo': minsdk_num[1],
                 'Gingerbread': minsdk_num[2], 'Honeybomb': minsdk_num[3],
                 'IceCreamSandwich': minsdk_num[4], 'Jellybean': minsdk_num[5]}
    return minsdkDic


def obf(obf_str):
    obf_num = formatStr2Num(obf_str)

    obfDic = {"REFLECTION": obf_num[3],
              "NATIVE": obf_num[2],
              "DYNAMIC": obf_num[1],
              "CRYPTO": obf_num[0], }

    return obfDic


def handle_uploaded_file(f):
    file_name = '%d' % random.randint(0, 100000)
    path = os.path.dirname(__file__).rstrip('table') + 'static/user_upfile/' + file_name + '.apk'
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    md5 = getFileMD5(path)
    return [path, md5[1]]


def userApk_handle(path):
    dir = os.path.dirname(__file__).rstrip('table') + 'analysis/'
    analysis = ApkAnalysis(path, dir, 2)
    bag = analysis.start_analysis()
    if bag is not None:
        m = Main(packagename=bag[0], app_version=bag[1], md5=bag[2], permission_num_str=bag[3], risk=bag[4],
                 minSDKversion=bag[5],
                 ad_SDK=bag[6], CRYPTO=bag[7], DYNAMIC=bag[8], NATIVE=bag[9], REFLECTION=bag[10])
        m.save()

        r = Result.objects.get(id=1)
        p = formatStr2Num(r.permission_num_str)
        a = formatStr2Num(r.ad_count_str)
        m = formatStr2Num(r.minsdk_count_str)
        o = formatStr2Num(r.obf_count_str)
        r.delete()

        # p_old = a.getPermission_count()
        # a_old = a.getAd_count()

        for i in range(len(p)):
            p[i] += analysis.getPermission_count()[i]
        for i in range(len(a)):
            a[i] += analysis.getAd_count()[i]
        for i in range(len(m)):
            m[i] += analysis.getMinsdk_count()[i]
        for i in range(len(o)):
            o[i] += analysis.getObf_count()[i]

        new_r = Result(id=1, permission_num_str=formatNum2Str(p), ad_count_str=formatNum2Str(a), minsdk_count_str=formatNum2Str(m),
                       obf_count_str=formatNum2Str(o))
        new_r.save()
        return 0
    else:
        return 1








