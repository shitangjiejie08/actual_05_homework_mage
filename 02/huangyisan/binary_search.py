#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.0
@author: huangyisan
@license: Apache Licence
@file: erfenchazhao.py
@time: 2017/3/29 22:17
"""

'''
三种情况：
1、刚好要查的数字等于中间索引对应的元素，则print该中间索引对应的数字。
2、查找的数字小于中间索引对应的元素，那么起始索引不变，结束索引变成上一轮的中间索引，本轮中间索引变成
"起始索引+上一轮中间索引"除以二，并取整。
3、查找的数字大于中间索引对应的元素，那么结束索引不变，起始索引变成上一轮的中间索引，本轮中间索引变成
"上一轮中间索引+结束索引"除以二，并取整。
4、不断循环步骤2和3，直到触发1。
'''

list_a = [1, 3, 5, 6, 9, 11, 15, 17, 20, 26, 29, 38, 45, 49, 50, 55, 61, 68, 73]
find_num = int(input('list为{0}\n输入想查位置的元素:'.format(list_a)))
start_index = 0
mid_index = len(list_a) // 2
end_index = len(list_a)
if find_num in list_a:
    while True:
        #步骤2
        if find_num < list_a[mid_index]:
            #start_index = 0
            end_index = mid_index
            mid_index = (start_index+end_index)//2
        #步骤3
        elif find_num > list_a[mid_index]:
            start_index = mid_index
            #end_index = end_index
            mid_index = (start_index+end_index)//2
        #步骤1，就是刚好输入查找的数字等于循环抑或首轮循环的中间数值
        else:
            print('{0}为第{1}个元素，索引为{2}'.format(find_num, mid_index+1,list_a.index(find_num)))
            break
else:
    print('请输入{0}中存在的元素'.format(list_a))

'''
功能ok，代码可以在优化一下
考虑
line 27已经判断了元素是否存在，line28~42行还有判断吗？
删除掉27行后，当元素不存在时什么时候结束循环
'''
