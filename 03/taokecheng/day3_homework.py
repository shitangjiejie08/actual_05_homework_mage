#/bin/env python
#encoding:utf-8

import readline

'''
让用户在控制台上输入”find/list/add/delete/update/exit”格式字符串
	如果输入add，则让用户继续输入”用户名:年龄:联系方式”格式字符串，
去除前后空字符，并使用:分隔用户数据，将用户数据放入dict中存储，
用户名作为key，value使用{name: 用户名, age: 年龄，tel:联系方式}，
在放入dict之前检查用户名不重复，如果重复，则提示用户已存在
zip: 矩阵组合，然后转换为字典，以少的为基准，多余的省略
'''

user_dic = {}
print_format = '|{:<20}|{:<20}|{:<20}|'
print_line = '+' + '-'*20+'+' + '-'*20+'+' + '-'*20+'+'
user_info_header = print_format.format('Name','Age','Phone')
base_info = ('name', 'age', 'phone')
print('欢迎还来到用户管理系统！')
print('-'*64)
while True:
	print('')
	opt = input('请输入(update/find/add/delete/list/exit): ')
	print('')
	opt = opt.strip().lower()
	if opt == 'add':
		add_text = input('请输入添加的用户，格式为(用户名:年龄:电话号码)： ')
		add_tuple = tuple(add_text.split(':'))
		add_dic = dict(tuple(zip(base_info,add_tuple)))
		if user_dic.get(add_tuple[0],0) == 0:
			user_dic.setdefault(add_tuple[0],add_dic)
			print('')
			print('用户添加成功，用户信息为：')
			print(print_line)
			print(user_info_header)
			print(print_line)
			print(print_format.format(user_dic[add_tuple[0]].get('name','Null'),user_dic[add_tuple[0]].get('age','Null'),user_dic[add_tuple[0]].get('phone','Null')))
			print(print_line)
		else:
			print('')
			print('用户名已存在！不需要重复添加，用户当前信息为：')
			print(print_line)
			print(user_info_header)
			print(print_line)
			print(print_format.format(user_dic[add_tuple[0]].get('name','Null'),user_dic[add_tuple[0]].get('age','Null'),user_dic[add_tuple[0]].get('phone','Null')))
			print(print_line)
	elif opt == 'update':
		update_text = input('请输入要更新的用户信息，格式为(用户名:年龄:电话号码)： ')
		update_tuple = tuple(update_text.split(':'))
		update_dic = dict(tuple(zip(base_info,update_tuple)))
		user_dic[update_tuple[0]] = update_dic
		print('')
		print('更新成功！用户当前信息为：')
		print(print_line)
		print(user_info_header)
		print(print_line)
		print(print_format.format(user_dic[update_tuple[0]].get('name', 'Null'), user_dic[update_tuple[0]].get('age', 'Null'),
		                          user_dic[update_tuple[0]].get('phone', 'Null')))
		print(print_line)
	elif opt == 'find':
		find_text = input('请输入要查找的用户名： ')
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
			if key.find(find_text) != -1:
				print(print_format.format(user_dic[key].get('name', 'Null'),
				                          user_dic[key].get('age', 'Null'),
				                          user_dic[key].get('phone', 'Null')))
				print(print_line)
				sum += 1
			elif len(user_dic) == n :
				print('搜索的用户名总数为 0 条。')
				continue
			n += 1
		print('搜索的用户名总数为 ', sum,' 条。')
	elif opt == 'delete':
		del_text = input('请输入要查找的用户名： ')
		if not user_dic.pop(del_text.strip(),False) :
			print('')
			print('%s 用户不存在，删除失败！'% del_text.strip())
		else:
			print('')
			print('删除用户 %s 成功！'% del_text.strip())
	elif opt == 'list':
		print('用户信息列表如下:')
		print(print_line)
		print(user_info_header)
		print(print_line)
		for key in user_dic.keys():
			print(print_format.format(user_dic[key].get('name', 'Null'),
			                          user_dic[key].get('age', 'Null'),
			                          user_dic[key].get('phone', 'Null')))
			print(print_line)
		print('当前用户总数是 ',len(user_dic),' 条。')
	elif opt == 'exit':
		break
	else:
		print('输入错误，请重新输入。')



'''
功能ok， 继续坚持，加油
1. 保证数据格式统一，如果没有找到就用None表示line 31
2. line29, 30去掉tuple尝试结果有什么变化
3. update中如果输入一个不存在的用户信息呢？
4. line72,98如果去掉keys()呢
5. python中没有Null，建议使用对应类型的默认值，比如'', 0等 
'''
