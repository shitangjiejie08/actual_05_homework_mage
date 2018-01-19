#!/usr/bin/python3.5
#encoding: utf-8

import random
random_num = random.randint(0,100)



count = 0
while count < 5:
    input_num = int(input('Please input number: '))
    if input_num == random_num:
        print('Great, you win.')
        break
    elif input_num < random_num:
        print('too small,again!')
    elif input_num > random_num:
        print('too big,again!')
    count += 1


if count >= 5:
    print('You lose.The number is', random_num)


'''
功能ok， 继续加油
'''
