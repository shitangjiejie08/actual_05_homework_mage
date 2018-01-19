#enconding: utf-8
#猜数游戏
import random
random_num = random.randint(1,100)
print("这是一个猜数游戏,一共有5次机会")
i = 1
while i < 6:
    num = input("请输入你猜的数字：")
    if int(num) < random_num:
        print("猜小了")
    elif int(num) > random_num:
        print("猜大了")
    elif int(num) == random_num:
        print("恭喜你猜对了")
        break
    i += 1

else:
    print("正确答案是:",random_num,",呜呜……下次再来吧")

'''
功能ok， 继续加油
'''
