# encoding:utf-8

#插入排序
l=[1,5,4,7,9,3,2,6,8]

for i in range(1,len(l)):
	for j in range(i,0,-1):
		if l[j] < l[j-1]:
			l[j],l[j-1] = l[j-1],l[j]
		else:
			break
print(l)

'''
功能ok，继续加油
'''
