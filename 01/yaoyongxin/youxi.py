#enconding: utf-8
import random
num=random.randint(0,100)
time=0
while time <= 5:
    if time == 5:
        print("真笨，5次都猜不中！重新来一次吧:D")
        break
    a=int(input("请输入一个0-100间的数字： "))
    time+=1
    if a < num:
        print("猜小了!")
        if 5-time != 0:
            print("你还有",5-time,"次机会，祝好运！")
        continue
    elif a > num:
        print("猜大了!")
        if 5-time != 0:
            print("你还有",5-time,"次机会，祝好运！")
        continue
    elif a == num:
        print("真聪明，猜中了！")
        break

'''
功能ok， 继续加油
1. 简化程序，考虑continue是否有用
'''
