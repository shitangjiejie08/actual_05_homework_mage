#encoding: utf-8
import random
# 生成随机数
rand_num = random.randint(0,100)


user_input = int(input("please input the number(1-100) you guess: "))

count = 5

while count > 1:
    if user_input > rand_num:
        print("the number you guess is a little bigger")
        user_input = int(input("please input the number: "))
    elif user_input < rand_num:
        print("the number you guess is a little less")
        user_input = int(input("please input the number: "))
    else:
        print("you win")
        break
    count -= 1
else:
    print("Please play again,the right number is：" + str(rand_num))

'''
功能ok，继续加油
'''
