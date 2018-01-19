#encoding:utf-8

'''
用户管理version 1.0
Author:daikai

1、用户在控制台上输入”find/list/add/delete/update/exit”格式字符串
2、如果用户输入add，则让用户继续输入用户名、年龄、联系方式等数据，将用户数据(用户名，年龄，联系方式)，
   放入list中存储，在放入list之前检查用户名不重复，如果重复，则提示用户已存在
3、如果用户输入delete，则让用户输入”用户名”字符串，根据用户名查找list中数据，若存在数据则将该数据移除，
   若用户数据不存在，则提示不存在
4、如果用户输入update，则让用户分别输入用户名、年龄、联系方式等数据，根据用户名查找list中数据，
   若存在数据则将改数据更新为新的(用户名, 年龄，联系方式)，若用户数据不存在，则提示不存在
5、如果用户输入find，则让用户输入”用户名” ，根据用户名查找list中数据用户名等于字符串的用户信息，并打印
6、如果用户输入list，则打印所有用户信息。打印用户第一个行数据为用户信息描述，从第二行开始为用户数据
7、如果用户输入exit，则打印退出程序，并退出
'''
user_data = []
user_info_tpl = '|{0:>15}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name','age','telephone')
while True:
    action = input("请输入你的操作(find/list/add/delete/update/exit):")
    if action == 'add':
        name = input('请输入用户名：')
        age = input('请输入年龄：')
        tel = input('请输入电话号码：')
        is_exists = False
        for user in user_data:
            if name == user[0]:
                print('用户名已存在')
                is_exists = True
                break

        if not is_exists:
            user_data.append((name,age,tel))
            print('添加用户成功')
        # print(user_data)
    elif action == 'delete':
        name = input("请输入需要删除的用户名：")
        is_exists = False
        for user in user_data:
            if name == user[0]:
                is_exists = True
                user_data.remove(user)  #user此时是一个元组，即某个用户的完整信息
                print('用户删除成功')
                break

        if not is_exists:
            print('删除用户失败，原因：用户不存在')
        # print(user_data)
    elif action == 'update':
        #这里的更新操作使用先删除后添加方法
        name = input("请输入需更改信息的用户名：")
        is_exists = False
        for user in user_data:
            if name == user[0]:
                is_exists = True
                user_data.remove(user)
                break

        if not is_exists:
            print('需更新信息的用户不存在')
        else:
            age = input("请输入需更改信息的用户年龄：")
            tel = input("请输入需更改信息的用户电话：")
            user_data.append((name,age,tel))
            print("更新用户信息成功")
        # print(user_data)
    elif action == 'find':
        name = input("请输入要查找的用户名：")
        is_exists = False
        for user in user_data:
            if name == user[0]:
                print(user_info_header)
                print(user_info_tpl.format(user[0], user[1], user[2]))
                is_exists = True
                break

        if not is_exists:
            print("待查找的用户名不存在")
    elif action == 'list':
        if len(user_data) == 0:
            print("没有用户信息可以展示")
        else:
            print(user_info_header)
            for user in user_data:
                print(user_info_tpl.format(user[0],user[1],user[2]))
    elif action == 'exit':
        print("退出程序")
        break
    else:
        print("操作命令错误！")


'''
加油，可以自己学习下for  else， while  else用法，看看能不能改进if not is_exists条件及其子语句
'''
