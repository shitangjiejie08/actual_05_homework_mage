#!/usr/local/bin/python3
# 99cfb 

for i in range(1,10):
    for j in range(1,1+i):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print('')

for i in range(1,10):
   for j in range(1,i+1):
       print('%d*%d=%2d' % (i,j,i*j),end='\t')
   print('')

'''
功能ok， 继续加油
1. 可以在a*b=c后加上空格，区分列显示

'''
