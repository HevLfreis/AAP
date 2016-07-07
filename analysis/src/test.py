#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com
# Date: 13-8-4 
# Time: 下午12:32
# 
# import json
# import networkx as nx
# import matplotlib.pyplot as plt
#
#
# G = nx.Graph()
# G.add_node(1)
# G.add_node(2)
# G.add_edge(1, 2)
# nx.draw(G)
# plt.show()

# data = [{'a':"A",'b':(2,4),'c':3.0}]  #list对象
# print "DATA:",repr(data)
#
# data_string = json.dumps(data)
# print "JSON:",data_string
#
#
# def test123(data):
#     return json.dumps(data)
#
# def list_has(list, key):
#     if len(list) == 0:
#         return False
#     else:
#         for i in list:
#             if i == key:
#                 return True
#             else:
#                 pass
#         return False
#
# list = ['4','5']
# print list_has(list,'6')