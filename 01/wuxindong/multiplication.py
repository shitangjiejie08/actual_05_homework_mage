#!/usr/bin/env python
# encoding:utf-8

BASE = 9

for multiplicant in range(1, BASE+1):
    for multiplier in range(1, multiplicant+1):
        msg = "{multiplicant} * {multiplier} = {total}".format(
            multiplicant = multiplicant,
            multiplier = multiplier,
            total = multiplicant * multiplier
        )
        print(msg, end='\t')
    print("")

'''
功能ok, 继续加油
1. 可以尝试打印上三角
'''
