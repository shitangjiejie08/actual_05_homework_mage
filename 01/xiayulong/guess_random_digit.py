# encoding: utf-8

import random

target = random.randint(0,100)
time = 1

YG = input("请输入一个整数(0-100之间的整数), 退出(quit): ")

while "quit" != YG.lower() and "q" != YG.lower():
    time += 1
    if time > 5:
        print("你太笨了，下次再来吧，数字是",target)
        break
    if YG.isdecimal():
        temp = int(YG)
        if temp > target:
            print("偏大")
        elif temp < target:
            print("偏小")
        else:
            print("真聪明，你猜对了，Your Guess:",temp,"\nTarget:",target)
            break
        YG = input("请再输入一个整数(0-100之间的整数), 退出(quit): ")
    else:
        YG = input("请重新输入一个整数(0-100之间的整数), 退出(quit): ")

'''
功能ok，继续加油
'''
