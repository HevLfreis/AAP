#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-28
# Time: 下午4:45
# Detecting the ad sdk in apks
from analysis.dict.ad_dic import ADMODULE


class AdDetect:

    def __init__(self, activities):
        self.activities = activities
        self.length = len(self.activities)
        self.risk = 0

    # check the activity name in ad module dic
    def get_ad_name(self):
        self.activities_transfer()
        ad_names = []
        for i in range(self.length):
            if ADMODULE.has_key(self.activities[i]):
                if [ADMODULE.get(self.activities[i])[0], ADMODULE.get(self.activities[i])[2]] in ad_names:
                    pass
                else:
                    ad_names.append([ADMODULE.get(self.activities[i])[0],
                                     ADMODULE.get(self.activities[i])[2]])
                    self.risk += 1
            else:
                pass
        if ad_names is None:
            return None
        else:
            return ad_names

    def get_risk(self):
        return self.risk

    # delete the activity name of the ad_activity label
    def activities_transfer(self):

        for i in range(self.length):
            # print self.activities[i]
            length_2 = len(self.activities[i])
            for j in range(0, -length_2 - 1, -1):
                # print self.activities[i][j]
                if self.activities[i][j] is '.':
                    self.activities[i] = self.activities[i][0:length_2 + j]
                    break
                else:
                    pass

    # #transfer the ad name str to [adname, adlink]
    # def name2link(self, ad_str):
    #     str_list = []
    #
    #     ad_str_list = ad_str.split('/')
    #     print ad_str_list
    #     for i in range(1, len(ad_str_list)):
    #         str_list.append(ad_str_list[i])
    #     return str_list



if __name__ == '__main__':
    adtest = AdDetect(['cn.domob.android.Adgfsf, ', 'cn.domob.android.Ad666656546547547, ','com.guohead.sdk.hfkdshdfkg','com.fractalist.hsghsk'])
    print adtest.get_ad_name()
    print adtest.name2link('/Youmi/AdWo/AdMob/MillennialMedia/AirAD ad/Waps')
