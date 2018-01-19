#!/bin/evn python
#encoding:utf-8
import random

random_num = random.randint(0,100)
sum = 0
print('游戏开始，有5次机会猜数字...')
guest_num = input('请输入你猜测的数字(0-100):  ')
while True:
	if len(guest_num.strip()) == 0 or not guest_num.strip().isdigit():
		print('-'*40)
		guest_num = input('错误! 只能输入数字,请重新输入，范围是(0-100)：')
		continue
	else:
		sum += 1
	guest_num = int(guest_num)
	if guest_num < random_num:
		print('\t猜小了！你还有 ',5-sum,' 次机会！')
	elif guest_num > random_num:
		print('\t猜大了！你还有 ',5-sum,' 次机会！')
	elif guest_num == random_num:
		print('\t猜对了，程序结束')
		break

	if sum == 5:
		print('-' * 40)
		print('5 次机会已经用完，游戏结束！')
		break
	else:
		guest_num = input('请输入你猜测的数字(0-100):  ')


'''
功能ok， 继续加油
'''
