#encoding:utf-8

import random
count = 5
print("猜数字游戏，一共有5次机会哦")
num2 = int(input('''
                祝你好运,在游戏开始，请输入0-100以内的任意整数：
                     '''))

while count > 0 and :
    num1 = random.randint(0, 100)
    num2 = int(input('''
                     祝你好运,在游戏开始，请输入0-100以内的任意整数：
                     '''))
    if num2 > num1:
        print("猜大了")
    elif num2 < num1:
        print("猜小了")
    else:
        print("恭喜你猜对了")
    count -= 1
    print("你还有"+str(count)+'次机会')
else:
    print("5次机会已经用完，请重新开始")


'''
代码有点问题呢?继续加油
1. while循环后的and
2. 打开后需要用户输入两次
3. 如果输入错误，下次随机数会变化
4. 猜测成功能不退出
'''
