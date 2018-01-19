#encoding:utf-8
users = {}
user_info_tpl = '|{0:^10}|{1:^5}|{2:^15}|'
keys = ('name','age','tel')
user_info_header = user_info_tpl.format(keys[0],keys[1],keys[2])
while True:
    action = input('please input(find/list/add/delete/update/exit):')
    action = action.strip()
    if action == 'add':
        user_text = input('请输入用户信息（用户名:年龄:联系方式）：')
        user_dict = dict(zip(keys,user_text.split(':')))
        user_name = user_dict.get('name')
        if user_name in users.keys():
                print('用户名已存在')
        else:
            users[user_name] = user_dict
            print('添加成功')
    elif action == 'delete':
        user_name = input('请输入用户名:')
        if user_name in users.keys():
                users.pop(user_name)
                print('删除成功')
        else:
            print('删除用户失败，原因:用户名不存在')
    elif action == 'update':
        user_text = input('请输入用户信息（用户名:年龄:联系方式）：')
        user_dict = dict(zip(keys,user_text.split(':')))
        user_name = user_dict.get('name')
        if user_name in users.keys():
            users[user_name] = user_dict
            print('更新用户成功')
            print(users[user_name])
        else:
            print('更新失败,原因:用户名不存在')
    elif action == 'find':
        user_name = input('请输入用户名:')
        if user_name in users.keys():
            print(user_info_tpl.format(users[user_name]['name'],users[user_name]['age'],users[user_name]['tel']))
        else:
            print('没有该用户信息')
    elif action == 'list':
        print(user_info_header)
        for user_name in users.keys():
            print(user_info_tpl.format(users[user_name]['name'],users[user_name]['age'],users[user_name]['tel']))
    elif action == 'exit':
            break
    else:
        print('命令错误')


'''
功能ok，, 继续坚持，加油
1. 查询用户名只要存在查找的字符串就显示
2. 考虑line13, 20, 2937, 43 需要keys函数吗
'''
