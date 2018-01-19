# encoding: utf-8
users = []
while True:
    command = input('Please input find/list/add/delete/update/exit: ')
    if command.strip() == 'add':
        is_bool = True
        name = input('Please input like name:age:tel style: ')
        name_temp = name.strip().split(':')
        for user in users:
            if name_temp[0] == user['name']:
                print(name_temp[0], ' is exited')
                is_bool = False
        if is_bool:
            users.append({'name': name_temp[0], 'age': name_temp[1], 'tel': name_temp[2]})
            print(name_temp[0], ' is added!')
    if command.strip() == 'delete':
        is_bool = True
        name = input('Please input a name: ')
        for user in users:
            if user['name'] == name.strip():
                users.remove(user)
                print ('user is deleted')
                is_bool = False
        if is_bool:
            print ('This\'s name is not exit.')
    if command.strip() == 'find':
        is_bool = True
        name = input('Please input a name: ')
        for user in users:
            if user['name'] == name.strip():
                i = list(user.values())
                print ('|{:<10}|{:<10}|{:<10}'.format('user', 'age', 'tel'))
                print ('|{0:<10}|{1:<10}|{2:<10}|'.format(i[0], i[1], i[2]))
                is_bool = False
        if is_bool:
            print('The name is not exit.')
    if command.strip() == 'exit':
        print ('exit now')
        break
    if command.strip() == 'list':
        print ('|{0:<10}|{1:<10}|{2:<10}|'.format('user', 'age', 'tel'))
        for user in users:
            print ('|{0:<10}|{1:<10}|{2:<10}|'.format(user['name'], user['age'], user['tel']))
    if command.strip() == 'update':
        is_bool = True
        name = input('Please input name:age:tel style : ')
        for user in users:
            if name.strip().split(':')[0] not in user.values():
                print('user is not exit')
                is_bool = False
        if is_bool:
            user.update({'age': name.strip().split(':')[1], 'tel': name.strip().split(':')[2]})
            print('update succeed')



'''
功能ok，可以再设置一条条件，进行练习, 继续坚持，加油
1. users如果修改为dict, 考虑下使用什么属性作为key，value如何存储，如何完成用户管理
2. 查询用户名只要存在查找的字符串就显示
3. 可以看看for else使用方法
'''
