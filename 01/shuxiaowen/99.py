#encoding: utf-8

#99乘法口诀表
for x in range(1,10):
	print('\t',x,'\t',end = '')
print('')

for i in range(1,10):
	print(i,'\t',end = '')
	for j in range(1,i+1):
		print(j,' * ',i,' =', i*j,'\t',end = '')
	print('')

'''
功能ok，继续加油
1. 考虑如何去除空行
2. 尝试打印上三角
'''
