#/usr/bin/py
#随机生成一个0到100的数字，提示用户在控制台上输入一个数字
#当用户输入数字小于生成的随机数，则打印猜小了
#当用户输入数字大于生成的随机数，则打印猜大了
#当用户输入数字等于生成的随机数，则打印猜对了，结束程序
#用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
#encoding:utf-8
#猜字游戏
import random
num = random.randint(0,100)
input_count = 5
while input_count >= 1:
    num1 = int(input('请输入1-100以的整数: '))
    if (num1 > num):
        print('你猜的数字大了，往小了猜!')
    elif (num1 < num):
        print('你猜的数字小了，再往大了猜!')
    elif (num1 == num):
        print('恭喜你,猜对了,下次再玩!')
        break
    input_count -= 1
else:
    print('太笨了,5次都没猜到,正确答案是',(num),'下次再来!')

'''
功能ok，继续加油
1. while, if, elif后的条件表达式可以不使用()

'''
