#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-8-2 
# Time: 上午10:19
# Risk formula


def eval_risk(perm_risk, perm_red, ad_risk, obfuscation_risk):
    return perm_risk + perm_red * 10 + ad_risk * 5 + obfuscation_risk * 20
