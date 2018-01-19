#encoding=utf-8


#9x9乘法口诀表，使用for实现
nums1=[1,2,3,4,5,6,7,8,9]
nums2=[1,2,3,4,5,6,7,8,9]
for i in nums1:
	for j in nums2:
		print(i, 'x', j, '=', i * j,' ',end='')
		if j==9:
			print('\n')
print('*********************************************************************************************************')



#9x9乘法表，使用while实现
numsa=[1,2,3,4,5,6,7,8,9]
count=1
while count<=9:
	for a in numsa:
		print(count,'x',a,'=',count*a,' ',end='')
	if a==9:
		print('\n')
	count+=1