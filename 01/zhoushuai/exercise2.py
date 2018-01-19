# encoding : utf-8

tryTimes = 5
print('猜数字游戏')
print('规则：系统生成一个1-100之间的数字，你有至多' + str(tryTimes) + '次猜测的机会，如果猜错系统会给你大或小的提示，如果最终都没答对，系统会公布最终答案')
result = 12  # 生成随机数
count = 1
while count <= tryTimes:
    guessNumber = input('请输入你猜的数字: ')
    guessNumber = int(guessNumber)
    if guessNumber == result:
        print('猜中了，请你吃糖')
        break
    else:
        if count < tryTimes:
            if guessNumber < result:
                print('小了')
            else:
                print('大了')
        else:
            print('没有机会了，最终答案是', result)
    count += 1
print('游戏结束')


'''
功能ok，但是随机数呢？太会作假了
'''
