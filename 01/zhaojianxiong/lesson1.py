# encoding: utf-8
import random
print('99乘法表')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list:
    if i - 1 > 0:
        print(i, '*', i, '=', i * i, end=' ')  # 下一次打印不会换行
    else:
        print(i, '*', i, '=', i * i)
    m = i
    while m > 1:
        m = m - 1
        if m == 1:
            print(i, '*', m, '=', i * m)
        else:
            print(i, '*', m, '=', i * m, end=' ')

'''
功能ok，继续加油

1. 考虑如何简化程序
2. 考虑打印上三角
3. 变量命名，明天上课看看list是什么
'''

print('Guess Number')
i = 1
random_num = random.randint(0, 100)
while i <= 5:
    number = int(input('Please input a number:'))
    if number < random_num:
        print('Guess small')
    elif number > random_num:
        print('Guess big')
    elif number == random_num:
        print('Guess right')
    i += 1
print('Too stupid')

'''
功能稍微有点问题，继续加油
1. 猜测成功后，为什么还要猜呢，如何退出
'''
