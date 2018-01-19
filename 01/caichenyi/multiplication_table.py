# encoding: utf-8
# Author: Cai Chenyi

# 打印乘法口诀
print('''乘法口诀表
0：退出系统
1-9：循环次数
''')
while True:
    loop = int(input('请输入你的选择：'))
    if loop == 0:
        print('退出系统，谢谢使用。')
        break
    elif loop > 0 and loop <= 9:
        for i in range(1, loop + 1):
            for j in range(1, i + 1):
                print('%d * %d = %d\t' % (j, i, j * i), end='')
            print('')
    else:
        print('你的输入有误，请重新输入')

'''
功能ok，继续加油
'''
