#homework by ...
#encoding: utf-8
import random
#按条件生成列表
random_list = []
while True:
	action = input('1:生成随机列表/2:添加一个数字/3:列出列表/4:自动排序/5:二分法找索引/6:退出')
	action = int(action)
	ifaction = False
	if action == 1:
		
		randon_counrt = input('请输入生成随机数的个数: ')
		randon_counrt = int(randon_counrt)
		count = 0
		while count < randon_counrt:
			random_number = random.randint(0,100)
			if random_number not in random_list:
				random_list.append(random_number)
			count += 1
		print('添加随机数字成功')
	elif action == 2:
		
		action_manual = input('请输入要添加的数字:   ')
		#action_manual = int(action_manual)
		if int(action_manual) in random_list:
			print('数字',action_manual,'重复')
			
		else:
			for number in action_manual:
				try:
					number = int(number)
					random_list.append(number)
					print('success to add',number)
				except:
					print('字符非法')
	elif action == 3:
		print(random_list)
	
	elif action == 4:
		action_4 = input('1:正顺|2:逆序')
		action_4 = int(action_4)
		if action_4 == 1:
			for j in range(len(random_list)):
				for i in range(len(random_list) - 1):
					if random_list[i] > random_list[i + 1]:
						tmp = random_list[i]
						random_list[i] = random_list[i + 1]
						random_list[i + 1] = tmp
			print(random_list)
		if action_4 == 2:
			for j in range(len(random_list)):
				for i in range(len(random_list)-1):
					if random_list[i] < random_list[i + 1]:
						tmp = random_list[i]
						random_list[i] = random_list[i + 1]
						random_list[i + 1] = tmp
			print(random_list)
	elif action == 5:
		start_int = 0
		end_int = len(random_list) - 1
		find_number = input('请输入要查找的数字：')
		find_number = int(find_number)
		while start_int <= end_int:
			mid_int = (start_int + end_int) // 2
			mid_num = random_list[mid_int]
			if mid_num > find_number:
				end_int = mid_int - 1
			elif mid_num < find_number:
				start_int = mid_int + 1
			else:
				print('已经找到{}在列表中的位置为{}'.format(find_number,mid_int))
				break
		else:
			print('没哟找到')
	elif action == 6:
		print('退出')
		break
	else:
		print('请输入正确的命令：1:生成随机列表/2:添加一个数字/3:列出列表/4:自动排序/5:二分法找索引/6:退出')
