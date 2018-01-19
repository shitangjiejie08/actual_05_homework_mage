#/bin/env python
#encoding:utf-8

import random

#插入排序法
# 算法描述：
#     1.从第一个元素开始，该元素可以认为已经被排序
#     2.取出下一个元素，在已经排序的元素序列中从后向前扫描
#     3.如果该元素（已排序）大于新元素，将该元素移到下一位置
#     4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
#     5.将新元素插入到该位置后
#     6.重复步骤2~5

#生成一个随机数组

n=0
random_list = []
while n <7:
	num  =  random.randint(0,100)
	if num not in random_list:
		random_list.append(num)
		n += 1

print(random_list)
insert_num = int(input('以上是一个随机的列表,插入一个数字与其排序：'))
input_list = [insert_num] + random_list

for i in range(1,len(input_list)):
	key = input_list[i]
	index = i
	for j in range(i-1,-1,-1):
		if input_list[j] > key:
			input_list[j+1] = input_list[j]
			index -= 1
		else:
			break
	input_list[index] = key


print('插入排序结果：')
print(input_list)

'''
功能ok，非常棒，加油
'''
#二分查找法

print('二分法从以上列表查找数据。')
search_num = int(input('请输入要查找的数字：'))
front = 0
end = len(input_list) - 1
while True:
	if front > end:
		print('找不到，输入的数字不在列表里！')
		break
	mid = int((front + end) / 2)
	if input_list[mid] > search_num:
		end = mid -1
	elif input_list[mid] < search_num:
		front = mid + 1
	elif input_list[mid] ==  search_num:
		print('要查找的数字找到了，在列表的index是：',input_list.index(search_num))
		break

'''
功能ok，继续加油
'''
