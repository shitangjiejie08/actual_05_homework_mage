#enconding: ntf-8
import random
num=random.randint(1,100)
time=4
guess=0
while guess!=num and time>=0:
    guess=int(input("*数字区间0-100，请输入你猜的数字:"))
    print("你输入数字是：",guess)
    if guess==num:
        print("猜对了，真厉害")
    else:
        if guess<num:
            print("你的猜数小于正确答案")
        else:
            print("你的猜数大于正确答案")
        print("太遗憾了，你猜错了，你还有",time,"次机会")
    time-=1
print("游戏结束")

'''
功能ok，继续加油
'''
