#encoding:utf-8
users={}
tpl='|{0:^20}|{1:^10}|{2:^20}|'
keys=('name','age','tel')
header=tpl.format(keys[0],keys[1],keys[2])
while True:
    action=input('请输入操作(find/list/add/delete/update/exit):').strip()
    if action=='add':
        user_add=input('请输入用户信息(用户名:年龄:联系方式:):')
        user_dict=dict(zip(keys,user_add.split(':')))
        user_name=user_dict.get('name')
        if user_name in users:
            print('用户已存在')
        else:
            users[user_name]=user_dict
            print('添加成功')
    elif action=='delete':
        del_user=input('请输入你要删除的用户名:').strip()
        if users.pop(del_user,None):
            print('删除成功')
        else:
            print('用户不存在')
    elif action=='update':
        user_update=input('请输入要更新的用户信息(用户名:年龄:联系方式:)').strip()
        user_dict=dict(zip(keys,user_update.split(':')))
        user_name=user_dict.get('name')
        if user_name in users:
            users[user_name]=user_dict
            print('用户信息已更新')
        else:
            print('用户不存在')
    elif action=='list':
        print(header)
        for user in users.values():
            print(tpl.format(user['name'],user['age'],user['tel']))
    elif action=='find':
        name=input('请输入要查找的用户名:').strip()
        print(header)
        for user_name,user in users.items():
            print(tpl.format(user['name'],user['age'],user['tel']))
        else:
            print('用户不存在')
    elif action=='exit':
        print('退出程序')
        break
    else:
        print('输入错误')

'''
功能ok，非常棒，继续加油
1. 查询用户名只要存在查找的字符串就显示
2. 用户查找好像有点问题
'''
