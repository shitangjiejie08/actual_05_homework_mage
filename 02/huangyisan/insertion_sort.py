#!/usr/bin/env python3
# encoding: utf-8
"""
@version: 1.0
@author: huangyisan
@license: Apache Licence
@file: insert_task.py
@time: 2017/3/26 15:40
"""

'''
一、首先判断原本序列是升序还是降序排列
 1、降序情况：
 若输入的数字大于第一个索引对应的值，则在0号索引位置进行插入。  情况1
 若输入的数字小于最后一个索引对应的值，则在最后一个索引位置插入。  情况2
 若输入的数字已经存在原本序列中，则插入到原本序列中该数字所存在的索引位置。  情况3
 若输入的数字，从索引0开始比较，如果小于索引0并且小于索引1，则和索引1比较，直到找到该数值小于索引n，且大于索引n+1，则插入到索引n中。  情况4

 2、递增情况：
 若输入的数字小于第一个索引对应的值，则在0号索引位置进行插入。  情况5
 若输入的数字大于最后一个索引对应的值，则在最后一个索引位置插入。  情况6
 若输入的数字已经存在原本序列中，则插入到原本序列中该数字所存在的索引位置。  情况7
 若输入的数字，从索引0开始比较，如果小于索引0并且小于索引1，则和索引1比较，直到找到该数值大于索引n，且小于索引n+1，则插入到索引n中。  情况8
 '''

ori_list = [1, 2, 3, 6, 8, 9]
insert_str = int(input('enter a num: '))
index_count = 0
#递增情况
if ori_list[0] < ori_list[1]:
    while True:
        #情况6
        if index_count + 1 == len(ori_list):
            ori_list.insert(len(ori_list), insert_str)
            break
        #情况7
        elif insert_str in ori_list:
            ori_list.insert(ori_list.index(insert_str), insert_str)
            break
        #情况8
        elif insert_str > ori_list[index_count] and insert_str < ori_list[index_count + 1]:
            ori_list.insert(index_count + 1, insert_str)
            break
        #情况8，进行不断循环，找到需要插入的索引
        elif insert_str > ori_list[index_count] and insert_str > ori_list[index_count + 1]:
            index_count += 1
        #情况5
        else:
            ori_list.insert(0, insert_str)
            break
    print(ori_list)
#降序情况
else:
    while True:
        #情况2
        if index_count + 1 == len(ori_list):
            ori_list.insert(len(ori_list), insert_str)
            break
        #情况3
        elif insert_str in ori_list:
            ori_list.insert(ori_list.index(insert_str), insert_str)
            break
        #情况4
        elif insert_str < ori_list[index_count] and insert_str > ori_list[index_count + 1]:
            ori_list.insert(index_count + 1, insert_str)
            break
        # 情况4
        elif insert_str < ori_list[index_count] and insert_str < ori_list[index_count + 1]:
            index_count += 1
        #情况1
        else:
            ori_list.insert(0, insert_str)
            break
    print(ori_list)


'''
有点问题呢，注意编程一定要想清楚自己想要解决的问题是什么
注意拿到一个不知道的问题时，首先应该考虑查阅工具查找下插入排序是什么，再开始动手
'''
