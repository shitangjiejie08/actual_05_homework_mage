#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.0
@author: huangyisan
@license: Apache Licence
@file: chengfabiao.py
@time: 2017/3/18 22:10
"""

for i in range(1,10):
    for j in range(1,10):
        if i<j:
            continue
        print("%d*%d=%d" %(i,j,i*j),end='\t')
    print('')

'''
功能ok，继续加油
1. 考虑14~16行如何改为2行，或者一行
2. 考虑如何打印上三角
'''
