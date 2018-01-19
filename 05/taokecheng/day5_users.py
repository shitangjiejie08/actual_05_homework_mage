#/bin/env python
#encoding:utf-8
import readline
import json

'''
完整课程知识整理
在用户管理功能中各功能修改为函数
登录验证、添加、修改、查询、列表、删除
用户信息文件读、写
使用json格式存储用户信息
列表展示排序:Sorted/list.sort
'''

def storeData(userFile,userData):
	fhandler = open(userFile,'w+')
	fhandler.write(json.dumps(userData))
	fhandler.close()

def locadData(userFile):
	fhandler = open(userFile)
	json_data = json.load(fhandler)
	return json_data



def Login():

	while True:
		choice = input('''
		>>欢迎来到用户管理系统，请选择：
				1) 登录;
				2) 注册用户;
				3) 退出。\n>>你的选择> '''
		               ).strip()
		if choice == '1':
			is_valid = False
			for i in range(3):
				loggin_name = input('\t>>请输入用户名： ')
				pwd = input('\t>>请输入密码： ')
				for user in user_dic.values():
					if user['name'] == loggin_name and user['passwd'] == pwd:
						is_valid = True
						break
				if is_valid:
					break
				else:
					print('用户名或密码错误!，请重新输入。')
			if not is_valid:
				print('已超过最大次数，程序退出！')
				break
			else:
				print('-' * 64)
				print('欢迎', loggin_name, '来到用户管理系统！')
				afterLogin()
		elif choice == '2':
			input_txt = input('请输入注册用户信息，格式为(用户名:密码:年龄:电话号码) >>  ').strip()
			if len(input_txt) > 0:
				input_dic = dict(zip(base_info, input_txt.split(':')))
				name = input_dic.get('name', None)
				if not user_dic.get(name, None):
					user_dic.setdefault(name, input_dic)
					print('')
					print('注册成功!')
				else:
					print('注册失败！', name, ' 已存在，请重新输入!')
			else:
				print('输入注册信息有误！')
		elif choice == '3':
			storeData(userFile,user_dic)
			print('系统已退出！')
			break
		else:
			print('输入错误，请重新输入。')



def afterLogin():
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
				print('用户添加成功!')
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
				print('%s 用户信息更新成功！' % name)
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
					                          '*' * len(user_dic[key]['passwd']),
					                          user_dic[key].get('age', None),
					                          user_dic[key].get('phone', None)
					                          ))
					print(print_line)
					sum += 1
			print('搜索的用户名总数为 ', sum, ' 条。')
		elif opt == 'delete':
			input_txt = input('请输入要删除的用户名： ')
			if not user_dic.pop(input_txt.strip(), None):
				print('')
				print('%s 用户不存在，删除失败！' % input_txt.strip())
			else:
				print('')
				print('删除用户 %s 成功！' % input_txt.strip())
		elif opt == 'list':
			while True:
				input_txt = input('请输入要排序字段(name/age/phone/back)>> ')
				if input_txt in ['name','age','phone'] :
					user_list = sortResult(user_dic,input_txt)
					printInfo(user_list)
				elif input_txt == 'back':
					break
				else:
					print('输入错误，请重新输入。')

		elif opt == 'back':
			break

		else:
			print('输入错误，请重新输入。')


def sortResult(userData,key):
	listData = list(userData.values())
	if key == 'name':
		listData.sort(key=lambda x:x[key])
	else:
		listData.sort(key=lambda x:int(x[key]))
	return listData



def printInfo(user_list):
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



if __name__ == '__main__':
	user_dic = {}
	print_format = '|{:<15}|{:<15}|{:<15}|{:<15}|'
	print_line = '+' + '-'*15+'+' + '-'*15+'+' + '-'*15+'+' + '-'*15+'+'
	user_info_header = print_format.format('Name','Password','Age','Phone')
	base_info = ('name', 'passwd','age', 'phone')
	#没有判断文件是否存在或者数据是否为空。。。
	userFile = 'user.dat'
	user_dic = locadData(userFile)
	#user_dic = {}
	Login()
#print(user_dic)



