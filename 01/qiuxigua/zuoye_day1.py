#encoding: utf-8

numbers = [1,2,3,4,5,6,7,8,9]
initidx = 1
for Cunumber in numbers:
    while initidx < Cunumber + 1:
        if initidx < Cunumber:
            if initidx * Cunumber <10:
                print(initidx,'x',Cunumber,'=',initidx * Cunumber,end='   ')
                initidx += 1
            elif initidx * Cunumber >=10 and initidx * Cunumber < 100:
                print(initidx,'x',Cunumber,'=',initidx * Cunumber,end='  ')
                initidx += 1
        elif initidx == Cunumber:
            print(initidx,'x',Cunumber,'=',initidx * Cunumber)
            initidx = 1
            break

print('\n\n\n')

import random
GuestResult = random.randint(0,3)
GuestTime = 1
while GuestTime <= 5:
    if GuestTime == 1:                      #优化建议，其实这个开始第一次显示的内容，可以放到while上面
        #print('\n这是一个猜字游戏，您可以猜测五次看您是否猜对！\n\n当前是您第',GuestTime,'次猜测!')
        #GuestNum = input('>>>请您输入一个数字：')
        GuestNum = input('\n\n这是一个猜字游戏，您可以猜测五次看您是否猜对！\n\n当前是您第{},次猜测\n>>>请您输入一个数字：'.format(GuestTime))       #使用这种方式调用变量，这个format目前还没学
    elif GuestTime > 1:
        print('\n\n当前是您第',GuestTime,'次猜测!')
        GuestNum = input('>>>请您再输入一个数字：')
    GuestNum = int(GuestNum)
    if GuestNum == GuestResult:
#还记得吗？你在这里纠结了半个多小时，还找人帮忙，以后一定要记得比较的数据类型要相同
#得出结论，if 做等值比较的时候，如果数据类型不一致，它不会报错，不会执行里面的子语句，这个很坑，一定要记住数据的类型。
        print('\n哇！恭喜您第',GuestTime,'次就猜对了!')
        break
    elif GuestNum < GuestResult:
        print('您猜得太小了！ 加油哦')
    elif GuestNum > GuestResult:
        print('''您猜得太大了！
        加油哦！''')                                  #三个单引号可以支持多行打印哦，input里面也是支持的
    GuestTime += 1

#下面是知识点，input里面是可以换行的
#num2 = int(input('''
#                祝你好运,在游戏开始，请输入0-100以内的任意整数：
#                     '''))
