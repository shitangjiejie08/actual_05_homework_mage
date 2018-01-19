# _*_ coding: utf-8 _*_
import os

"""
这是一个9x9乘法口诀表
"""


for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{}x{}={:<3}".format(j, i, i*j), end='')
    print(os.linesep)


'''
功能ok,继续加油
1. 考虑去除空行
2. 考虑打印上三角格式
'''
