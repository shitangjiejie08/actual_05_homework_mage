#!/usr/bin/env python
# encoding:utf-8

import random

rand_num = random.randint(0, 100)
user_input = int(input("Please guess a number: "))

count = 5

while count > 1:
    if user_input > rand_num:
        print("oh, bigger")
        user_input = int(input("try again: "))
    elif user_input < rand_num:
        print("oh, smaller")
        user_input = int(input("try again: "))
    else:
        print("Bingo, well done")
        break
    count -= 1
else:
    print("fool, restart again")

'''
功能ok，继续加油
'''
