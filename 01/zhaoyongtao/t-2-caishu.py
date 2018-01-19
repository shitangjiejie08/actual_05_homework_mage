#encoding:utf-8
'''
 猜数游戏
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
'''
import random
count=5

#生成随机数
rand=random.randint(1,100)

while count:
    count=count-1
    user_input = int(input('请输入1-100之间的数字：'))
    if user_input==rand:
        print('好厉害，这都被你猜到了！')
        break
    elif user_input>rand:
        print('大了，大了，往小了猜猜。\t你还有'+str(count)+'次机会')
    elif user_input<rand:
        print('小了，小了，往大了猜猜。\t你还有'+str(count)+'次机会')
else:
    print('你太笨了！正确答案是 '+str(rand)+' 没猜到吧！')

'''
功能ok，继续加油，流程图画的不错
'''
