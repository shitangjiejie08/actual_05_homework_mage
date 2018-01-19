'''
用户管理
让用户在控制台上输入”find/dict/add/delete/update/exit”格式字符串
如果输入add，则让用户继续输入”用户名:年龄:联系方式”格式字符串，去除前后空字符，并使用:分隔用户数据，将用户数据放入dict中存储，用户名作为key，value使用{name: 用户名, age: 年龄，tel:联系方式}，在放入dict之前检查用户名不重复，如果重复，则提示用户已存在
如果输入delete，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在
如果输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找dcit中数据，若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在
如果用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据包含输入字符串的用户信息，并打印
如果用户输入dict，则打印所有用户信息
打印用户第一个行数据为用户信息描述，从第二行开始为用户数据
如果用户输入exit，则打印退出程序，并退出
'''
usr_dict = {}
while True:
    action = input("请输入操作(find/dict/add/delete/update/exit):")
    if action == "add":
        name = input("请输入用户名:")
        age = input("请输入年龄:")
        tel = input("请输入电话号码:")
        usr_infor = {name:{"name":name,"age":age,"tel":tel}}
        if name in usr_dict:
            print("用户已存在，无需添加")
        else:
            usr_dict.update(usr_infor)
    elif action =="delete":
        name = input("请输入用户名:")
        if name in usr_dict:
            usr_dict.pop(name)
            print("已删除")
        else:
            print(usr_dict.pop(name,"用户不存在"))
    elif action =="update":
        name = input("请输入用户名:")
        age = input("请输入年龄:")
        tel = input("请输入联系方式:")
        usr_infor = {name:{"name":name,"age":age,"tel":tel}}
        if name in usr_dict:
            usr_dict.update(usr_infor)
            print("已更新")
        else:
            print("您输入的用户不存在")
    elif action =="find":
        name = input("请输入用户名:")
        if name in usr_dict:
            print("姓名:",usr_dict[name]["name"],"年龄:",usr_dict[name]["age"],"电话号码:",usr_dict[name]["tel"])
        else:
            print("您输入的用户不存在")
    elif action =="dict":
        print("以下是所有用户信息:")
        print("{name:<15}    {age:<15}    {tel:<15}".format(name="name",age="age",tel="tel"))
        for k,v in usr_dict.items():
            print("{name:<15}    {age:<15}    {tel:<15}".format(name=v["name"], age=v["age"], tel=v["tel"]))
    elif action =="exit":
        break


'''
功能ok，可以再设置一些条件，进行练习, 继续坚持，加油
1. 比如用input接收一次提交用户输入的用户名，年龄，电话号码，练习下字符串分隔
2. 查询用户名只要存在查找的字符串就显示
'''
