#encoding:utf-8

#次数通过计数器count来循环，猜对即跳出break，如果所有机会都没有猜对，
#应打印出随机数

import random
count = 0
print("猜数字游戏，最多有6次机会哦")
num1 = random.randint(0, 100)

while count <= 6:
    num2 = int(input('''祝你好运,在游戏开始，请输入0-100以内的任意整数：'''))
    if num2 > num1:
        print("猜大了")
    elif num2 < num1:
        print("猜小了")
    else:
        print("恭喜你,猜对了")
        break   #猜对即退出
    count += 1
    print("你还有"+ str(6-count)+"次机会")
    #print("你还有%d次机会"% (6-count))
else:
    print("6次机会已经用完，请重新开始")
    print("正确的数字是：%d" % num1)

'''
功能ok，继续加油
'''
