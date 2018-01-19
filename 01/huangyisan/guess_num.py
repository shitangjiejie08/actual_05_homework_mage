#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.0
@author: huangyisan
@license: Apache Licence
@file: guess_num.py
@time: 2017/3/18 22:38
"""

import random
real_num=random.randint(0,100)
count=5
while count:    #当count自减到0，则跳出。
    print('总共5次机会，当前还剩下%s次~' %count)
    try:    #捕获非整数输入的错误。
        guess_num = int(input('enter a num: '))
    except ValueError as e:
        print('\033[1;31;40m你敢不敢输入一个整数，再捣乱抽你哦~\033[0m')
    else:
        if guess_num == real_num:
            print('\033[1;33;41m猜到了\033[0m')
            break
        elif guess_num < real_num:
            count -= 1
            print('猜小了')
        else:
            count -= 1
            print('猜大了')
else:
    print("\033[1;31;40m太笨了，下次再来 \033[0m")

'''
功能ok，继续加油
'''
