#encoding:utf-8



#在列表内使用字典存储信息
users = []
user_info_tpl = '|{0:^15}|{1:^10}|{2:^15}|'
user_info_header = user_info_tpl.format('姓名','年龄','电话')
while True:
	action = input('请输入以下命令(add/del/find/update/list/exit):')
	if action == 'add':
		user_input = input('请按照以下格式输入(姓名:年龄:电话):')
		name,age,tel = user_input.split(':')
		for user in users:
			if name in user.values():
				print('错误!用户已存在!')
				break
		else:
			users.append({'姓名':name,'年龄':age,'电话':tel})
			print('添加用户成功!')

	elif action == 'del':
		name = input('请输入需要删除的用户名:')
		for user in users:
			if name in user.values():
				users.remove(user)
				print('删除用户信息成功!')
				break
		else:
			print('错误!用户不存在!')
			break

	elif action == 'find':
		name = input('请输入要查找的用户:')
		print(user_info_header)
		for user in users:
			if user.get('姓名') == name:
				print(user_info_tpl.format(user['姓名'],user['年龄'],user['电话']))
				break
		else:
			print('错误!用户不存在!')

	elif action == 'update':
		user_input = input('请按以下格式输入要修改的信息(姓名:年龄:电话):')
		name,age,tel = user_input.split(':')
		for user in users:
			if user.get('姓名') == name:
				user['姓名'] = name
				user['年龄'] = age
				user['电话'] = tel
				print('用户信息修改成功!','\n',user)
				break
		else:
			print('错误!用户不存在!')

	elif action == 'list':
		print(user_info_header)
		for user in users:
			print(user_info_tpl.format(user['姓名'],user['年龄'],user['电话']))

	elif action == 'exit':
		break

	else:
		print('错误的命令!请重新输入!')








