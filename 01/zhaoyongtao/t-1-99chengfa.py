#encoding:utf-8
#打印99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %2d '%(i,j,i*j),end=" ")#其中，%2d代表2个占位符
    print(' ')

'''
功能ok， 继续加油
1. 考虑打印上三角
'''
