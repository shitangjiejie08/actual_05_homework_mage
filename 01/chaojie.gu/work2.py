#encoding: utf-8
'''
猜数字游戏
随机生成一个0～100之间的数字，提示用户在控制台上输入一个数字
当用户输入的数字大于随机数，则打印猜大了
当用户输入的数字小于随机数，则打印猜小了
当用户输入的数字等于随机数，则打印猜对了
用户一共可以猜5次，如果5次都错误，则打印"太笨了，下次再来"
提示：生成随机数的方法
import random
random_num=random.randint(0,100)
'''
import random
random_num=random.randint(0,100)

count=5
user_input=input('请猜一个1到100之间的数:')
while count>=2:
    if user_input.isdigit():
        user_input=int(user_input)
        count=count-1
        if user_input>random_num:
            user_input=input('猜大了！你还有'+str(count)+'次机会\n请猜一个1到100之间的数：')
        elif user_input<random_num:
            user_input=input('猜小了！你还有'+str(count)+'次机会\n请猜一个1到100之间的数：')
        elif user_input==random_num:
            print('猜中了！恭喜你获得大奖！')
            break
    else:
        user_input=input('只能输入数字！\n请输入一个1到100之间的数字!')
else:
    print('你输入的次数太多，请下次再来！')


'''
可以多测试一下, 当猜正确时程序是否可以正确运行，原因是什么，如何修改
'''
