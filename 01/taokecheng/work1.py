#!/bin/evn python
#encoding:utf-8

for i in range(1,10):
	for j in range(1,i+1):
		print('{}x{}{}{:<4}'.format(j,i,'=',i*j),end='')
		# print(j,'x',i,'=',i*j,'\t',end='')
	print('')

'''
功能ok， 继续加油
1. 尝试打印上三角
'''
