#!/usr/local/bin/python3
#
users=[]
user_info_tpl='|{0:^20}|{1:^10}|{2:^20}|'
user_info_header=user_info_tpl.format('name','age','tel')
while True:
	action=input('Please input(add/delete/find/update/list/exit): ')
	if action == 'add':
		name=input('请输入用户名：')
		age=input('请输入年龄：')
		tel=input('请输入电话号码：')
		is_exists=False
		for user in users:
			if name == user[0]:
				print('用户已存在')
				is_exists=True
				break
		if not is_exists:
			users.append((name,age,tel))
			print('添加用户成功')
			print(users)		
	elif action == 'delete':
		name=input('请输入要删除的用户名：')
		is_exists=False
		for user in users:
			if name == user[0]:
				is_exists=True
				users.remove(user)
				print('删除用户成功')
				break
		if not is_exists:
			print('用户不存在')
		print(users)			
	elif action == 'update':
		name=input('请输入用户名：')
		age=input('请输入年龄：')
		tel=input('请输入电话号码：')
		is_exists=False
		for user in users:
			if name == user[0]:
				is_exists=True
				users.remove(user)
				break
		if is_exists:
			users.append((name,age,tel))
			print('更新用户成功.')
			print(users)
		else:
			print('用户不存在')			
	elif action == 'find':
		name=input('请输入用户名：')
		is_exists=False
		print(user_info_header)
		for user in users:
			if name == user[0]:
				is_exists=True
				print(user_info_tpl.format(user[0],user[1],user[2]))
		if not is_exists:
			print('用户不存在')		
	elif action == 'list':
		print(user_info_header)
		for user in users:
			print(user_info_tpl.format(user[0],user[1],user[2]))
	elif action == 'exit':
		break
	else:
		print('输入错误')
