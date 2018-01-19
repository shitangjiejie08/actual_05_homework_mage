#!/user/bin/python3.5
#encoding: utf-8

user_list = {}
tpl = '|{:>10}|{:>10}|{:>15}|'
keys = ('name','age','tel')
header = tpl.format(keys[0],keys[1],keys[2])

while True:
        ACTION = input('请输入你需要的操作(find/dict/add/delete/update/exit): ')
        ACTION = ACTION.strip()
        if ACTION == 'add':
                user_text = input('请输入用户信息(用户名:年龄:联系方式)：')
                user_text = user_text.strip()
                user_dict = dict(zip(keys,user_text.split(':')))
                user_name = user_dict.get('name')
                if user_name in user_list:
                        print('用户已存在')
                else:
                        user_list[user_name] = user_dict
                        print('添加成功')


        if ACTION == 'delete':
                name = input('请输入需要删除的用户名:')
                if user_list.pop(name.strip(),None):
                        print('已删除')
                else:
                        print('用户不存在')


        if ACTION == 'update':
                user_text = input('请输入用户信息(用户名:年龄:联系方式)：')
                user_text = user_text.strip()
                user_dict = dict(zip(keys,user_text.split(':')))
                user_name = user_dict.get('name')
                if user_name in user_list:
                        user_list[user_name] = user_dict
                        print('已更新')
                else:
                        print('用户不存在')


        if ACTION == 'find':
                name = input('请输入需要删除的用户名:')
                name = name.strip()
                if name in user_list:
                        print(header)
                        print(tpl.format(user_list[name]['name'],user_list[name]['age'],user_list[name]['tel']))
                else:
                        print('用户不存在')


        if ACTION == 'dict':
                print(header)
                for i in user_list:
                        print(tpl.format(user_list[i]['name'],user_list[i]['age'],user_list[i]['tel']))


        if ACTION == 'exit':
                print('退出')
                break





'''
功能ok，可以再设置一些条件，进行练习, 继续坚持，加油
1. 注意编辑器使用，缩进使用4个空格
2. 查询用户名只要存在查找的字符串就显示
3. 注意检查用户输入
'''
