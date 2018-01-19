# _*_ coding: utf-8 _*_
"""
人员管理 增删改查
"""
peoples = []
# peoples = [{'hug': {'age': '12', 'name': 'hug', 'tel': '13'}}, {'had': {'age': '1', 'name': 'had', 'tel': '2'}}]
user_info_split = '-' * 60
user_info_tpl = '|{name:20} |{age:20} |{tel:20}'
user_info_tpl_format = user_info_tpl.format(name='name', age='age', tel='tel')

while True:
    action = input("find/list/add/delete/update/exit:")
    if action == "add":
        input_people = input("name:age:tel >>")
        try:
            name, age, tel = input_people.split(':')
        except:
            print("数据格式错误,请重新输入！")
            continue
        exist_people = [people for people in peoples if name in people]

        if exist_people:
            print("同名用户[{}]已存在: ".format(name))
            print(user_info_tpl_format)
            print(user_info_split)
            print(user_info_tpl.format(name=exist_people[0][name]['name'], age=exist_people[0][name]['age'], tel=exist_people[0][name]['tel']))
        else:
            peoples.append({name: {'name': name, 'age': age, 'tel': tel}})

    elif action == "delete":
        delete_user = False
        name = input("delete user name:")
        for people in peoples:
            if name in people:
                delete_user = True
                peoples.remove(people)
                print("删除用户[{}]成功".format(name))
        if not delete_user:
            print("用户不存在！")

    elif action == "update":
        update_people = False
        input_people = input("name:age:tel >>")
        try:
            name, age, tel = input_people.split(':')
        except:
            print("数据格式有误,请重新输入!")
        for index in range(len(peoples)):
            if name in peoples[index]:
                update_people = True
                peoples[index] = {name: {'name': name, 'age': age, 'tel': tel}}

        if not update_people:
            print("这个用户不存在")

    elif action == "find":
        name = input("find name:")
        find_peoples = []
        for index in range(len(peoples)):
            for key in peoples[index]:
                if name in key:
                    find_peoples.append(peoples[index])

        if find_peoples:
            print(user_info_tpl_format)
            print(user_info_split)
            for people in find_peoples:
                for key, value in people.items():
                    print(user_info_tpl.format(name=value['name'], age=value['age'], tel=value['tel']))
        else:
            print("用户不存在")

    elif action == "list":
        print(user_info_tpl_format)
        print(user_info_split)
        for people in peoples:
            for key, value in people.items():
                print(user_info_tpl.format(name=value['name'], age=value['age'], tel=value['tel']))

    elif action == "exit":
        break
    else:
        print("请正确输入")



'''
功能ok, 继续坚持，加油
1. users如果修改为dict, 考虑下使用什么属性作为key，value如何存储，如何完成用户管理
2. 考虑find代码能否简化
'''
