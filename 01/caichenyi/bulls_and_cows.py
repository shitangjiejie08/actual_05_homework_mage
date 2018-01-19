# encoding: utf-8
# Author: Cai Chenyi

# 猜数字
import random
random_num = random.randint(0,100)
print(random_num)
loop = 5
min = 0
max = 100
for i in range(1,loop + 1):
    num = int(input('请输入第%d次猜测[%d~%d]：' % (i, min, max)))
    if num == random_num:
        print('恭喜猜对了，游戏结束')
        break
    elif num < random_num:
        print('你猜的太小了')
        min = num + 1
    elif num > random_num:
        print('你猜的太大了')
        max = num - 1
if num != random_num:
    print('%d次机会用完，游戏失败' % loop)



'''
功能ok，善于学习，继续加油

改进点
1. 变量名的定义:
    可以看看下节课max, min这两个变量是什么东西
2. 变量定义位置:
    变量在使用时尽量在缩进同一级或上N级别进行定义，num，可以尝试在if-else的的子语句中分别定义a = 1, b=2后if同一缩进级别打印a, b看什么现象

if True:
    a = 1
else:
    b = 2

print(a, b)
'''
