# encoding: utf-8
'''
1.打印乘法口诀
'''
#问题一：
'''
rows=1 每次加一行
乘法从1开始知道和行数相等
'''
'''
#方法一：
rows = 0
i = 1
while rows <9:
	rows += 1
	while i < rows:
		#print('%s * %s =',i*rows,end='  ')%(i,rows)
		print(str(i)+'*'+str(rows),'=',i*rows,end='  ')
		i += 1
	if i == rows:
		#print('%s * %s =',i*rows)%(i,rows)
		print(str(i)+'*'+str(rows),'=',i*rows)
		i = 1
'''
#方法二：
rows = 0
i = 1
while rows <9:
	rows += 1
	while i <= rows:
		#print('%s * %s =',i*rows,end='  ')%(i,rows)
		print(str(i)+'*'+str(rows),'=',i*rows,'  ',end='')
		i += 1
	i = 1
	print()

'''
功能ok，继续加油
1. 可以尝试打印一个上三角
'''
#-------------------------------------------------------------------------------------------------------
'''
2.猜数游戏：
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最多可猜测5次，如果五次都错误，则打印"太笨了，下次再来"，并结束程序
'''
'''
思路：
1.先用random模块生成一个随机数：random.randint(0,100)
并且猜测次数为5  while循环
2.根据二分法的思路判断，当相等的时候直接结束，if语句
3.当猜测的数字小于随机数，打印出猜小了，elif语句
4.当猜测的数字大于随机数，打印出猜大了，elif语句
5.如果五次都没猜出来，打印"太笨了，下次再来"，并结束程序
'''
import random
panduan = True
while panduan:
	ran_num = random.randint(0,100)
	i = 1
	print('随机数：',ran_num)
	while i < 6:
		num = input("请输入一个猜测数字，数字取值范围是0到100:")
		if (len(num) == 0) or (not num.strip().isdigit()):
			print('输入值不能为空或不是数字，请重新输入')
			i = i-1
		elif int(num) == ran_num:
			print("恭喜你，猜对了!")
			exit()
		elif int(num) < ran_num:
			if (5-i) == 0:
				print("太笨了，下次再来")
				break
			else:
				print("不好意思，你猜的小了,你还有"+str(5-i)+"次机会")
		else:
			if (5-i) == 0:
				print("太笨了，下次再来")
				break
			else:
				print("不好意思，你猜的大了,你还有"+str(5-i)+"次机会")
		i += 1
	play = input("是否继续游戏？")
	if play == "是":
		panduan = True
	else:
		panduan = False


'''
功能ok，继续加油
1. 考虑如果成功后，想要继续玩怎么办
'''
