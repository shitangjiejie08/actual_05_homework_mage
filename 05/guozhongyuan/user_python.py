#encoding: utf-8
import json

user_list = {}
tpl = '|{:>10}|{:>10}|{:>15}|{:>10}'
keys = ('name','age','tel','passwd')
header = tpl.format(keys[0],keys[1],keys[2],keys[3])
path = r'C:\Users\Administrator\Desktop\day3\test.txt'
path_json = r'C:\Users\Administrator\Desktop\day3\json_user.txt'

fhandler = open(path,'r')
for line in fhandler:
    name,age,tel,passwd = line.strip().split(':')
    user_list[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}
fhandler.close()

def read_users():
    fhandler = open(path,'r')
    for line in fhandler:
        name, age, tel, password = line.strip().split(':')
        user_list[name] = {'name' : name, 'age' : age, 'tel' : tel, 'passwd' : password}
    fhandler.close()
#用户增加
def USER(action):
    if action == 'add':
        user_text = input('请输入  用户名:年龄:联系方式:密码（使用 ：隔开）')
        user_text = user_text.strip()
        user_dict = dict(zip(keys,user_text.split(':')))
        user_name = user_dict.get('name')
        if user_name in user_list:
            print('用户已存在')
        else:
            user_list[user_name] = user_dict
            print('添加成功')

    elif action == 'delete':
        name = input('请输入需要删除的用户名:')
        if user_list.pop(name.strip(),None):
            print('已删除用户')
        else:
            print('用户不存在')

    elif action == 'update':
        user_text = input('请输入更新的用户信息(用户名:年龄:联系方式:密码)：')
        user_text = user_text.strip()
        user_dict = dict(zip(keys,user_text.split(':')))
        user_name = user_dict.get('name')
        if user_name in user_list:
            user_list[user_name] = user_dict
            print('已更新')
        else:
            print('用户不存在')

    elif action == 'find':
        name = input('请输入需要查找的用户名:')
        name = name.strip()
        if name in user_list:
            print(header)
            print(tpl.format(user_list[name]['name'],user_list[name]['age'],user_list[name]['tel'],'*' * len(user_list[name]['passwd'])))
        else:
            print('用户不存在')

    elif action == 'list':
        print(header)
        for i in user_list:
            print(tpl.format(user_list[i]['name'],user_list[i]['age'],user_list[i]['tel'],'*' * len(user_list[i]['passwd'])))

    elif action == 'exit':
        fhandler = open(path_json,'w')
        #for line in user_list.values():
        #    json.dumps(fhandler.write('{0}:{1}:{2}:{3}\n'.format(line['name'],line['age'],line['tel'],line['passwd'])))
        json_data = json.dumps(user_list)
        fhandler.write(json_data)
        fhandler.close()
        print('退出并保存成功')
    else:
        print('输入指令错误')
#user mamager
def user_manager(name,password):
	#is_valid = False
	for user in user_list.values():
		if user['name'] == name and user['passwd'] ==  password:
			return True

count = 1
while count <= 3:
	passname = input('请输入用户名: ')
	password = input('请输入用户密码: ')
	read_users()
	if user_manager(passname,password) == True:
		print('login success')
		action = input(('|添加用户********{}\n|删除用户********{}\n|修改用户********{}\n|查找用户********{}\n|显示用户********{}\n|保存退出********{}\n'.format('add','delete','update','find','list','exit')))
		USER(action)
	else:
		print('用户名或密码错误')