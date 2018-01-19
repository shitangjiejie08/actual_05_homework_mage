#encoding=utf-8
#猜字游戏test.py
#aft(曾庆章）于2017.3.24)
print('猜字游戏，游戏开始了，祝你好运！')
import random
count=0


#生成随机数
a=random.randint(0,100)
#b=input_num
print(a)
#提示用户输入数字
b=float(input('请输入一个0～100的数字：'))
#进行数字比较
while count<=5:
    count+=1
    # 对数字范围进行判断：
    while True:
        if b < 0:
            print('您猜的数字太小了！')
            b = float(input('请输入一个0～100的数字：'))
        elif b > 100:
            print('你猜太大了！')
            b = float(input('请输入一个0～100的数字：'))
        else:
            break
    if count==5:
        print('大笨了，下次再来！')
        break
    if b==a and count==1:
        print('第一次就猜对了，真厉害！')
        break
    elif b>a:
        print('猜大了，继续猜吧～')
        b = float(input('请输入一个0～100的数字：'))

    elif b<a:
        print('猜小了，继续猜吧～')
        b = float(input('请输入一个0～100的数字：'))

    else:
        print('终于猜对了，恭喜！')
        break

'''
功能ok， 继续加油
1. float在编程语言中常常使用近似值，一般不进行==比较，养成良好编码习惯
'''
