# encoding:utf-8

for i in range(1,10):
	for j in range(1,i+1):
		if j != i:
		    print(i, '*', j, '=', i*j,'\t', end = ' ')
		else:
			print(i, '*', j, '=', i*j)

'''
功能ok， 继续加油
1. 考虑打印上三角格式
'''
