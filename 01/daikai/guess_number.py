#encoding:utf-8

import random
random_num = random.randint(0,100)
print(random_num)

total_num = 5
use_times = 1

while use_times <= total_num:
    num = int(input("请输入0-100之间的数字:"))
    if num == random_num:
        print("恭喜您猜对了,一共猜了%d次"%use_times)
        break
    elif num < random_num:
        print("猜小了，您还有%d次机会"%(total_num - use_times))
        use_times += 1
    else:
        print("猜大了，您还有%d次机会"%(total_num - use_times))
        use_times += 1

if use_times == total_num + 1:
    print("%d次机会都已经用完。太笨了，下次再来猜吧!!!"%total_num)


'''
功能ok，继续加油
'''
