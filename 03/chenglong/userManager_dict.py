# encoding: utf:8

users = []
tp1 = '|{:>10}|{:>5}|{:>15}|'
header = tp1.format('name', 'age', 'tel')

while True:
    try:
        action = input('请输入操作(find/dict/add/delete/update/exit):')
        action = action.strip()
        if action == 'add':
            str_data = input('请按格式输入信息，如  用户名：年龄：联系方式 （用英文:分割）').strip()
            name = str_data.split(":")[0]
            age = str_data.split(":")[1]
            tel = str_data.split(":")[2]
            # user_tuple = (name, age, tel)
            user_dict = {"name":name, "age": age, "tel":tel}
            is_exists = False
            for user in users:
                if user['name'] == name:
                    is_exists = True
                    print('用户已存在')
                    break

            if not is_exists:
                users.append(user_dict)
                print('添加成功')
        elif action == 'delete':
            name = input('请输入用户名：')
            is_exists = False
            for user in users:
                if name == user["name"]:
                    is_exists = True
                    users.remove(user)
                    print('已删除用户%s' % name)
                    break
            if not is_exists:
                print('用户不存在')
        elif action == 'update':
            str_data = input('请按格式输入信息，如  用户名：年龄：联系方式 （用英文:分割）')
            name = str_data.split(":")[0]
            is_exists = False
            for user in users:
                if user["name"] == user_dict["name"]:
                    users.remove(user)
                    is_exists = True
                    break
            if is_exists:
                age = str_data.split(":")[1]
                tel = str_data.split(":")[2]
                user_dict = {"name":name, "age":age, "tel":tel}
                users.append(user_dict)
                print("用户内容已更新")
            if not is_exists:
                print("用户信息不存在")
        elif action == 'find':
            name = input("请输入用户名：").strip()
            print(header)
            is_exists = False
            for user in users:
                if name in user["name"]:
                    print(tp1.format(user["name"], user["age"], user["tel"]))
                    is_exists = True
                    continue

            if not is_exists:
                print("用户不存在")
        elif action == 'dict':
            print(header)
            for user in users:
                print(tp1.format(user["name"], user["age"], user["tel"]))
        elif action == 'exit':
            print("程序已退出")
            break
    except:
        print("输入有误，请重新选择并按格式输入")


'''
功能ok，可以再设置一些条件，进行练习, 继续坚持，加油
1. split分隔后的元素直接复制给name, age, tel
2. users如果修改为dict, 考虑下使用什么属性作为key，value如何存储，如何完成用户管理
3. 查询用户名只要存在查找的字符串就显示
'''
