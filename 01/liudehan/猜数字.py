#envcoding: utf-8
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
1. while, if, elif 后的条件表达式可以不用()括起来
'''
