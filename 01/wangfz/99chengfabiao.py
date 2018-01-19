#encoding:utf-8
#打印乘法口诀表
n = 1
while (n <=9 ):
    x = 1
    while x <= n:
        l = n * x
        print(x,'*',n,'=',l,"  ",end=" ")
        x += 1
    print("\n")
    n += 1

'''
功能ok， 继续加油
1. while, if, elif后的条件表达式可以不使用()
2. 尝试去除空行
3. 尝试打印上三角
'''
