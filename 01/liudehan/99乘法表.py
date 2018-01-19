#!/usr/bin/env python
#encoding: utf-8
for i in range(10):
    b=1
    while b <= i:
        print('{}X{}{}{:<4}'.format(b,i,'=',b*i),end='')
        b+=1
    print()

'''
功能 ok， 继续加油
1. 第一行打印空行，为什么？
2. 文件命名采用变量名命名规则，不要使用中文，养成良好编码习惯
'''
