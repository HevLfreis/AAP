#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-7-22 
# Time: 下午8:19
#
from analysis.dict.perm_dic import permDic, redFlags


class Permission:
    def __init__(self):

        # risk is a num decide by the permissions that the app grants
        # permission has two risk-property normal and dangerous
        # risk = dangerous/normal+dangerous
        self.risk = 0.0
        self.red_risk = 0

    def getDic(self):
        return permDic

    # get the value of the permission return OTHERS if not in the dic
    def getItem(self, str):
        if permDic.get(str) is not None:
            return permDic.get(str)
        else:
            return permDic.get('OTHERS')

    # input detail_permission list return permission nums and update the risk

    def perms2nums(self, perms):
        if perms is None:
            return []
        else:
            perm_num = []
            i = 0
            for (key, value) in perms.iteritems():
                if key.startswith('android.permission.'):
                    perm_num.append(self.getItem(key.strip('android.permission.')))

                    if redFlags.get(key.strip('android.permission.')) is not None:
                        self.red_risk += 1
                    self.risk += self.riskTrans(value[0])
                else:
                    pass
                i += 1
            if i == 0:
                self.risk == 0
            else:
                self.risk = int((self.risk / i) * 100)
            return perm_num

    def numstr2list(self, perm_str):

        perm_num = []

        list_num = perm_str.split('.')

        count = 0
        for i in range(len(perm_str)):
            if perm_str[i] == '.':
                count += 1

        for i in range(1, count + 1):
            perm_num.append(int(list_num[i]))
        perm_num.sort()
        list = []
        perm_list = sorted(permDic.iteritems(), key=lambda a: a[1], reverse=False)
        for i in range(len(perm_num)):
            list.append(perm_list[perm_num[i]][0])
        self.description(list)
        return list

    def red_risk(self):
        return self.red_risk

    def isRedApk(self):
        return self.red_risk > 5

    def get_risk(self):
        return self.risk

    def riskTrans(self, risk_str):
        if risk_str == 'dangerous':
            return 1
        elif risk_str == 'normal':
            return 0
        else:
            return 0

    def description(self, perm_list):
        for i in range(len(perm_list)):
            if redFlags.has_key(perm_list[i]):

                perm_list[i] = [perm_list[i], redFlags.get(perm_list[i])]
            else:
                perm_list[i] = [perm_list[i], "NONE"]




if __name__ == '__main__':
    p = Permission()
    print p.getItem('android.permission.WRITE_PROFILE')
    print p.numstr2list('.114.120.5.57.77')


    #unused method
    #input permission list [] return permission nums
    # def getItems(self, strs):
    #     values = []
    #     self.formatStrs(strs)
    #     for i in range(0, len(strs)):
    #         values.append(self.getItem(strs[i]))
    #     return values

    #delete the 'android.permission.'
    # def formatStrs(self, strs):
    #     for i in range(0, len(strs)):
    #         strs[i] = strs[i].strip('android.permission.')
    #     return strs