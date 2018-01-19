#encoding:utf-8

import random
random_num = random.randint(1,100)
i = 1
input_num = int(input('Please guess the number!\n Give the ' + str(i) +' try :'))
while input_num != random_num:
	if i < 5:
		if input_num < random_num:
			print('try a bigger one')
		else:
			print('try a smaller one')
		i += 1
		input_num = int(input('Please give the ' + str(i) + ' try :'))
	else:
		print('What a pity! You missed the chance! Try next time!')
		exit()

print('Bingo!Congratulations!')

'''
功能ok， 继续加油
'''
