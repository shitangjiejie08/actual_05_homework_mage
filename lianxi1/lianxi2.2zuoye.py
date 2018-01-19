#enconding:utf-8
users=[]
users_xinxi='|{0:^10}|{1:^10}|{2:^15}|'
users_head=users_xinxi.format('name','age','tel')
while True:
    action=input('please input add,delete,find,update,exit,list')
    if action=='add':
        name=input('please input your name ')
        age=input('please input your age ')
        tel=input('please input your tel ')
        exit=False
        for user in users:
            if name==user[0]:
                print("can't add, yi cun zai ")
                exit=True
                break
        if not exit:  #11 hang bu yunxing zhuan 10 zai zhuan 15
            users.append((name,age,tel))#shuang kuo hao,xiang liebiao users tianjia yuanzu.
            print(name, age, tel)
            print(users)
    elif action=='delete':#ci wei str xing
        name = input('please input your name ')
        exit=False
        for user in users:
            if name == user[0]:
                exit=True
                users.remove(user)
                print('yishanchu')
        if not exit:
            print('bu cunzai')
    elif action=='find':#ci wei str xing
        name = input('please input your name ')
        exit=False
        print(users_head)
        for user in users:
            if name == user[0]:
                exit=True
                print(users_xinxi.format(user[0],user[1],user[2]))
        if not exit:
            print('bu cunzai')
    elif action=='update':#ci wei str xing
        name = input('please input your name')
        age = input('please input your age')
        tel = input('please input your tel')
        exit=False
        for user in users:
            if name == user[0]:
                exit=True
                users.remove(user)
                print('shanchu chenggong')
                break
        if exit:
            users.append((name, age, tel))  # shuang kuo hao,xiang liebiao users tianjia yuanzu.
            print('gengxinchenggong',users)#gaiwei user zuihao(xu zai zou jibu)
        else:
            print('gengxinshibai')
    elif action=='exit':
        break
    elif action == 'list':  # ci wei str xing
        print(users_head)
        for user in users:
            print(users_xinxi.format(user[0],user[1],user[2]))#yong user ba suoyou yonghu xie chulai







