#encoding:utf-8
import random
random_num = random.randint(1,100)

guess_count = 5
print('欢迎参加猜数字游戏，共有5次猜数字机会，加油！',end = '')
while guess_count > 0:

	guess = input('请猜一个数字: ')
	try:
		guess = int(guess)
	except ValueError:
		print('请遵守规则，输入0到100的数字！',end = '')
		continue
	guess_count -= 1
	if guess == random_num:
		print('真是天才，你答对了！')
		break
	elif guess > random_num:
		print('你猜得太大了，还有',guess_count,'次机会, ',end = '')
	elif guess < random_num:
		print('你猜得太小了，还有',guess_count,'次机会, ',end = '')

else:
	print('你的机会用完了，太笨了，5次都猜不出来！')
	print('游戏结束！再见！')

'''
功能ok， 加油
'''
