#encoding:utf-8
#zengqingzhang于2017.4
#filename=user.py
#用户管理

users = {}
tpl = '|{:>15}|{:>10}|{:>20}|'
keys = ('name', 'age', 'tel')
header =  tpl.format(keys[0], keys[1], keys[2])

while True:
	action=input('请输入操作 \n（find/list/add/delete/update/exit):')
	action=action.strip()
#add
	if action=='add':
		user_text=input('请分别输入你的信息（用户名、年龄、联系方式）')
		name=input('你的名字:')
		age =input('你的年龄:')
		tel =input('你的联系方式:')
		user_dict={'name':name,'age':age,'tel':tel}
		is_exists=False
		if user_name in users:
			print('用户已存在')
		else:
			users[user_name]=user_dict
			print('添加成功')
#delete
	elif action=='delete':
		name=input("请输入查找用户名：")
		if users.pop(name.strip(), None):
			print('已删除')
		else:
			print('用户信息不存在')
	elif action=='update':
		user_text=input('请分别输入你的信息（用户名、年龄、联系方式）')
		name=input('你的名字:')
		age =input('你的年龄:')
		tel =input('你的联系方式:')
		user_dict={'name':name,'age':age,'tel':tel}
		is_exists=False
		user_name=user_dict.get('name')
		if user_name in users:
			users[user_name] =user_dict
			print('已更新')
		else:
			print('用户信息不存在')
#find
	elif action=='find':
			name=input('请输入查找用户名：')
			name=name.strip()
			print(header)
			for user_name,user in users.items():
				if user_name.find(name) != -1:
					print(tpl.format(user['name'], user['age'], user['tel']))
#list
	elif action=='list':
			print(header)
			for user in users.values():
				print(tpl.format(user['name'],user['age'], user['tel']))
	elif action=='exit':
			print('退出程序')
			break
