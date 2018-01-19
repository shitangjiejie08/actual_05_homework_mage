#encoding=utf-8



import random
count=1

#生成随机数
random_num=random.randint(0,100)
while count<=5:
    count += 1
    input_num = int(input('请输入一个0~100以内的数字:'))
    # 提示用户输入,并检查输入是否符合要求
    if input_num>100 or input_num<0:
        print('请按要求输入数字：')
        continue
    if input_num<random_num:
        print('小啦～继续猜吧！')
    elif input_num>random_num:
        print('大啦～还得继续！')
    elif input_num==random_num:
        print('恭喜你～终于猜对啦！')

#超过5次，在while之外输出结果
print('居然还没猜出来，也是醉了，不玩啦！')

