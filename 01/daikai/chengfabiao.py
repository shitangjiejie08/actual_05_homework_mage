#encoding:utf-8

# 1、for循环方法
#for i in range(1,10):
#    for j in range(1,i+1):
#        print(i,"x",j,"=",i*j,"\t",end="")
#    print()


# 2、while循环方法
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(i,"x",j,"=",i*j,"\t",end="")
        j += 1
    print("")
    i += 1

'''
功能ok，继续加油
1. 可以考虑打印下上三角形
'''
