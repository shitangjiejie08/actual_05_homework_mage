#!/usr/local/bin/python3
#
import random

# 生成随机数
rand_num = random.randint(0,100)

user_input = int(input("请输入一个1-100的数字: "))

count = 5

while count > 1:
    if user_input > rand_num:
        print("猜大了！")
        user_input = int(input("请输入一个1-100的数字: "))
    elif user_input < rand_num:
        print("猜小了！")
        user_input = int(input("请输入一个1-100的数字: "))
    else:
        print("猜对了，本宝宝佩服！")
        break
    count -= 1
else:
    print("太笨了，下次再来！正确答案是：" + str(rand_num))

'''
功能ok， 继续加油
'''
