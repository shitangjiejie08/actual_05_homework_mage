#!/usr/local/bin/python3
#encoding: utf-8

nums=[5,13,19,21,37,56,64,75,80,88,92]

find_num=int(input('please input the num you wanna search: '))

start=0
end=len(nums)-1

while True:
	mid=(start+end) // 2
	if find_num == nums[mid]:
		print('找到了，索引为:',mid)
		break
	elif find_num > nums[mid]:
		#print('在后半段')
		start = mid + 1
	else:
		#print('在前半段')
		end = mid - 1
	if start > end:
		print('未找到')
		break

'''
功能ok，继续加油
'''
