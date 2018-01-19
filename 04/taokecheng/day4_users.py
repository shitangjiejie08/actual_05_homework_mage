#/bin/env python
#encoding:utf-8
import readline

user_dic = {}
print_format = '|{:<15}|{:<15}|{:<15}|{:<15}|'
print_line = '+' + '-'*15+'+' + '-'*15+'+' + '-'*15+'+' + '-'*15+'+'
user_info_header = print_format.format('Name','Password','Age','Phone')
base_info = ('name', 'passwd','age', 'phone')
user_data = ('user.dat')
load_user_dat = open(user_data)
for user in load_user_dat:
	tmp = dict(zip(base_info,user.strip().split(':')))
	# print(tmp)
	user_dic[tmp['name']]=tmp
load_user_dat.close()

#print(user_dic)

while True:
	choice =  input('''
>>欢迎来到用户管理系统，请选择：
		1) 登录;
		2) 注册用户;
		3) 退出。\n>>你的选择> '''
	 ).strip()
	if choice == '1':
		is_valid = False
		for i in range(3):
			loggin_name = input('\t>>请输入用户名： ' )
			pwd = input('\t>>请输入密码： ')
			for user in user_dic.values():
				if user['name'] == loggin_name and user['passwd'] == pwd:
					is_valid = True
					break
			if is_valid :
				break
			else:
				print('用户名或密码错误!，请重新输入。')
		if not is_valid:
			print('已超过最大次数，程序退出！')
			break
		else:
			print('-' * 64)
			print('欢迎', loggin_name, '来到用户管理系统！')
			while True:
				print(' ')
				opt = input('请输入(update/find/add/delete/list/back): ')
				print('')
				opt = opt.strip().lower()
				if opt == 'add':
					input_txt = input('请输入添加的用户，格式为(用户名:密码:年龄:电话号码) >>  ')
					input_dic = dict(zip(base_info, input_txt.split(':')))
					name = input_dic.get('name', None)
					if not user_dic.get(name, None):
						user_dic.setdefault(name, input_dic)
						print('')
						print('用户添加成功，用户信息为：')
						print(print_line)
						print(user_info_header)
						print(print_line)
						print(print_format.format(user_dic[name].get('name', None), '*' * len(user_dic[name]['passwd']), user_dic[name].get('age', None),
						                          user_dic[name].get('phone', None)
						                         ))
						print(print_line)
					else:
						print('')
						print('添加失败！用户名已存在。')

				elif opt == 'update':
					input_txt = input('请输入添加的用户，格式为(用户名:密码:年龄:电话号码) >>  ')
					input_dic = dict(zip(base_info, input_txt.split(':')))
					name = input_dic.get('name', None)
					if name in user_dic:
						user_dic[name] = input_dic
						print('')
						print('更新成功！用户当前信息为：')
						print(print_line)
						print(user_info_header)
						print(print_line)
						print(print_format.format(user_dic[name].get('name', None), '*' * len(user_dic[name]['passwd']),user_dic[name].get('age', None),
						                          user_dic[name].get('phone', None)
						                          ))
						print(print_line)
					else:
						print('更新失败，%s 用户不存在！' % name)
				elif opt == 'find':
					input_txt = input('请输入要查找的用户名： ')
					print('')
					print('查找到的结果如下：')
					print(print_line)
					print(user_info_header)
					print(print_line)
					if len(user_dic) == 0:
						print('搜索到的用户名总数为 0 条。')
						continue
					sum = 0
					for key in user_dic.keys():
						n = 1
						if key.find(input_txt) != -1:
							print(print_format.format(user_dic[key].get('name', None),
							                          '*' * len(user['passwd']),
							                          user_dic[key].get('age', None),
							                          user_dic[key].get('phone', None)
							                          ))
							print(print_line)
							sum += 1
						elif len(user_dic) == n:
							print('搜索的用户名总数为 0 条。')
							continue
						n += 1
					print('搜索的用户名总数为 ', sum, ' 条。')
				elif opt == 'delete':
					input_txt = input('请输入要查找的用户名： ')
					if not user_dic.pop(input_txt.strip(), None):
						print('')
						print('%s 用户不存在，删除失败！' % input_txt.strip())
					else:
						print('')
						print('删除用户 %s 成功！' % input_txt.strip())
				elif opt == 'list':
					while True:
						input_txt = input('请输入要排序字段(name/age/phone/back)>> ')
						user_list = list(user_dic.values())
						if input_txt in [ 'age','name','phone']:
							for i in range(len(user_list) - 1):
								for j in range(len(user_list) - 1 - i):
									if input_txt == 'age':
										user_list[j][input_txt] = int(user_list[j][input_txt])
										user_list[j + 1][input_txt] = int(user_list[j + 1][input_txt])
									if user_list[j][input_txt] > user_list[j + 1][input_txt]:
										temp = user_list[j]
										user_list[j] = user_list[j + 1]
										user_list[j + 1] = temp
							print('用户信息列表如下:')
							print(print_line)
							print(user_info_header)
							for user in user_list:
								print(print_line)
								print(print_format.format(user.get('name', None),
								                          '*' * len(user['passwd']),
								                          user.get('age', None),
								                          user.get('phone', None)
									                          ))
							print(print_line)
							print('当前用户总数是 ', len(user_list), ' 条。')
						elif input_txt == 'back':
							break
						else:
							print('输入错误，请重新输入。')

				elif opt == 'back':
					break

				else:
					print('输入错误，请重新输入。')


	elif choice == '2':
		input_txt = input('请输入注册用户信息，格式为(用户名:密码:年龄:电话号码) >>  ')
		input_dic = dict(zip(base_info,input_txt.split(':')))
		name = input_dic.get('name',None)
		if not user_dic.get(name,None) :
			user_dic.setdefault(name,input_dic)
			print('')
			print('注册成功!')
		else:
			print('注册失败！',name,' 已存在，请重新输入!')
	elif choice == '3':
		user_data = ('user.dat')
		load_user_dat = open(user_data,'wt')
		for user in user_dic.values():
			load_user_dat.write('{}:{}:{}:{}\n'.format(user.get('name', None),
				                               user.get('passwd', None),
				                               user.get('age', None),
				                               user.get('phone', None)))
		load_user_dat.close()
		print('系统已退出！')
		break
	else:
		print('输入错误，请重新输入。')
