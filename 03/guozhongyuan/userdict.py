#encoding = utf-8

users = {}
keys = ['name','age','tel']
titl = '|{:>10}|{:>5}|{:>15}|'
head = titl.format(keys[0],keys[1],keys[2])
flag = False
print('--------------欢迎登陆用户管理系统-------------------')
while True:
	action = input('请输入您要进行的操作(delete/update/add/list/find/exit):')
	action = action.strip()
	if action == 'delete':
		user = input('请输入要删除的用户名：')
		user = user.strip()
		if users.pop(user,False):
			print('用户已删除')
		else:
			print('用户信息不存在')
	elif action == 'update':
		info = input('请输入要update的信息（格式： 用户名：年龄：电话）：')
		user_info = dict(zip(keys,info.split(':')))
		name = user_info.get('name')
		if name in users:
			users[name] = user_info
			print('用户‘'+name+'’的信息已更新')
		else:
			print('该用户不存在')
	elif action == 'add':
		info = input ('请输入要添加的用户信息（格式： 用户名：年龄：电话）：')
		user_info = dict(zip(keys,info.split(':')))
		name = user_info.get('name')
		if name in users:
			print ('用户'+name+'已存在，无法添加')
		else:
			users[name] = user_info
			print ('用户添加成功')
	elif action == 'list':
		print(head)
		for i in users.values():
			print (titl.format(i['name'],i['age'],i['tel']))
	elif action == 'find':
		user = input('请输入要查找的用户名：')
		if users.find(user) != -1 :
			print (users[user])
		#user = user.strip()
		#for i in list(users):
 		#	if user in str(i):
 		#		a = users[i]
 		#		print (titl.format(a['name'],a['age'],a['tel']))
 		#		flag = True
		#if flag == False :
		#	print ('用户'+user+'不存在')
	elif action == 'exit':
		print('系统已退出。。。。。。。。。。')
		break
	else:
		print ('输入错误请重新输入')


'''
功能ok，继续坚持，加油
1. 变量命名尽量见名知义，向a, i 这种尽量减少使用频次
2. 考虑line44, 45需要使用list和str转义吗
'''
