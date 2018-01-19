#encoding :utf-8
#2017-03-20
#郭中源
#
#作业一，乘法表

lista = [ '1','2','3','4','5','6','7','8','9' ]
for i in  lista :
	for j in lista :
		if int(i) != int(j) :
 			print ( i , '*' , j , '=', int(i) * int(j) ,' ',end= '')
		else :
 			print ( i , '*' , j , '=', int(i) * int(j))
 			break


'''
功能ok， 继续加油
1. 可以考虑使用while循环如何实现
'''
