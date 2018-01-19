#encoding: utf-8

#调用随机数
import random
#生成随机数
real_num = random.randint(0,100)

#定义剩余次数变量
count = 5

while count:
    print('总共5次机会，当前还剩下%s次机会' %count)
    #捕获非整数输入的错误。
    guess_num = (input('请输入一个1-100的整数：'))
    if(len(guess_num) == 0):
            print('输入值不能为空，请重新输入')
    elif int(guess_num) == real_num:
            print("恭喜你，猜对了")
            exit()
    elif int(guess_num) < real_num:
            count -= 1
            print("不好意思，你猜的小了，你还有"+str(count)+"次机会")
    else:
            count -= 1
            print("不好意思，你猜的大了，你还有"+str(count)+"次机会")
else:
    print("太笨了，下次再来！正确答案是：" + str(real_num))


'''
功能ok， 继续加油
'''
