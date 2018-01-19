######################99乘法表
m=1
n=1
while(m<10):
    while(n<10):
        if m==1 & n==1:
            print("%2d * %2d = %2d\t" % (m, n, m * n))
            break
        elif n < m:
            print("%2d * %2d = %2d\t" %(n,m,m*n),end="")
            n += 1
            continue
        else:
            print("%2d * %2d = %2d" % (n, m, m * n))
            n += 1
            break
    m += 1
    n=1

'''
功能ok，继续加油
1. 程序有点绕，可以考虑下能不能将程序简化
2. python中while和if 条件语句可以不加()
3. 在布尔表达式中 且用and标识, &为位运算
'''




###################################################c猜数字游戏
import random
x = random.randint(0,100)
#the number you set to gess
i=1
n=5
print(x)
while(i<=5):
    print("@_@:")
    print(n,end="")
    print(" times left")
    y = input("please input the number you guess:")
    y = int(y)
    if(y == x):
        print("@_@:")
        print("you win")
        break
    elif(y > x):
        print("@_@:")
        print("the number you guess is a little bigger")
    elif(y < x):
        print("@_@:")
        print("the number you guess is a little less")
    i = i + 1
    n = n - 1
else:
    print("@_@:")
    print("times use up,you lose")


'''
功能ok，继续加油
1.可以看看代码，如果不需要使用变量可以删除
2. while, if, elif后的条件表达式不用()括起来，养成python良好的编码习惯
'''
