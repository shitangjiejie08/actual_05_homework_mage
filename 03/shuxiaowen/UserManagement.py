#encoding: utf-8

'''
让用户输入操作：add/delete/update/list/find/exit,使用.lower().strip()改正用户输入，
'''


users = {'test':{'name':'test','age':'100','tel':'18688886666'}}
user_info = ('name','age','tel')
user_display_format = ('\t|{0:^10}|{1:^5}|{2:^11}|')
user_display = (user_display_format.format('Name','Age','Tel'))

while True:
	ops = input('Please select (add/delete/update/list/find/exit): ').strip().lower()
	if ops == "add":
		user_input = input('Please input the user information as name:age:tel >').strip().split(':')
		if len(user_input) != 3 or len(user_input[0]) == 0:
			print('Please follow the format: name:age:tel, try again.')
			continue
		else:
			if user_input[0] not in users.keys():
				users[user_input[0]] = dict(zip(user_info,user_input))
				print('User {{ {name:^5} }} add success:'.format(name = user_input[0]))
				print(user_display,'\n',user_display_format.format(user_input[0],user_input[1],user_input[2]))

				continue
			else:
				print('User {{ {name:^5} }} is exist.'.format(name = user_input[0]))
				print(user_display,'\n',user_display_format.format(users[user_input[0]]['name'],users[user_input[0]]['age'],users[user_input[0]]['tel']))


	elif ops == 'delete':
		user_input = input('Please input the username to delete >').strip()
		pop_user = users[user_input]
		users.pop(user_input,'user {} do not exist'.format(user_input))
		print('The deleted user is:')
		print(user_display,'\n',user_display_format.format(pop_user['name'],pop_user['age'],pop_user['tel']))


	elif ops == 'list':
		print(user_display)
		for user in users:
			print(user_display_format.format(users[user]["name"],users[user]["age"],users[user]["tel"]))
		print('All Users above')

	elif ops == 'update':
		user_input = input('Please update the user information as name:age:tel >').strip().split(':')
		if len(user_input) != 3 or len(user_input[0]) == 0:
			print('Please follow the format: name:age:tel, try again.')
			continue
		else:
			if user_input[0] in users.keys():
				users[user_input[0]].update(dict(zip(user_info,user_input)))
				print('User {{ {0:^5} }} update success:'.format(user_input[0]))
				print(user_display,'\n',user_display_format.format(users[user_input[0]]['name'],users[user_input[0]]['age'],users[user_input[0]]['tel']))
			else:
				print('{{{0:^5}}} is not exist.'.format(user_input[0]))
				#continue

	elif ops == 'find':
		user_input = input('Please input the username to find >').strip().lower()
		is_exist = False
		for key in users:
			if key.lower().find(user_input) != -1:
				print(user_display,'\n',user_display_format.format(users[key]['name'],users[key]['age'],users[key]['tel']))
				is_exist = True
				continue
		if not is_exist:
			print('the name you input is not exist, try again')

	elif ops == 'exit':
		break
	else:
		print('Error, Try again')
		continue




'''
功能ok，可以再设置一些条件，进行练习, 继续坚持，加油
1. line10, 11非元组类型赋值减少使用()，当然没什么问题，但是容易导致误解
2. 可以了解下for else如何使用
'''
