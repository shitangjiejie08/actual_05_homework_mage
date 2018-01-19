from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models
from pymysql.cursors import DictCursor
# Create your views here.

pool = models.ConnectionPool(host='172.16.129.143',
                          port=3306,
                          user='root',
                          passwd='password',
                          db='xiaozhi',
                          charset="utf8",
                          cursorclass=DictCursor)

def require_login(request):
    return render(request, 'user/login.html')


def login(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username, password)
    is_exists = False
    # rt = models.validate_login(username, password)
    # if rt:
    #     #return HttpResponse('success')
    #     return  HttpResponseRedirect('/user/list_user/')
    # else:
    #     context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
    #     return render(request, 'user/login.html', context)
    with pool() as db:

        db.execute("select username, password from userlist where username='{}' and password='{}'".format(username, password))
        for row in db.fetchall():
            if row['username'] and row['password']:
                is_exists = True
    if is_exists:
        return HttpResponseRedirect('/user/list_user/')
    context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
    return render(request, 'user/login.html', context)

def list_user(request):
    rt = {}
    # rt = models.list_user()
    # rt = list(rt.values())
    # context={'info':rt}
    # print(rt)
    # return  render(request, 'user/list.html', context)
    with pool() as db:
        db.execute("select username, password, age, tel from userlist")
        for row in db.fetchall():
            username = row['username']
            password = row['password']
            age = row['age']
            tel = row['tel']
            rt[username] = {"username":username, 'password':password, 'age':age, 'tel':tel}
        rt = list(rt.values())
        context={'info':rt}
        print(rt)
        return  render(request, 'user/list.html', context)



def delete_user(request):
    # username = request.GET.get('username', '')
    # print(username)
    # models.delete_user(username)
    # return  HttpResponseRedirect('/user/list_user/')
    username = request.GET.get('username', '')
    with pool() as db:
        db.execute("delete from userlist where username='{username}'".format(username=username))
    return  HttpResponseRedirect('/user/list_user/')



def add_user(request):
    # if request.method == "GET":
    #     return render(request, 'user/add.html')
    #
    # username = request.POST.get('username', '')
    # age = request.POST.get('age', '')
    # tel = request.POST.get('tel', '')
    # password = request.POST.get('password', '')
    # print(username, age, tel, password)
    # if username and age and tel and password:
    #     rt_status, rt_reason = models.validate_add_user(username, age, tel, password)
    #     if rt_status:
    #         models.add_user(username, age, tel, password)
    #         return HttpResponse('<a href="/user/list_user/">添加成功，点击跳转到显示页面</a>')
    #     else:
    #         print(rt_reason)
    # else:
    #     return HttpResponse('添加失败：用户名，密码，电话，密码都不能为空')
    if request.method == "GET":
        return render(request, 'user/add.html')

    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    password = request.POST.get('password', '')
    print(username, age, tel, password)
    is_exists = False
    if username and age and tel and password:
        with pool() as db:
            db.execute("select username from userlist where username='{username}'".format(username=username))
            for row in db.fetchall():
                name = row['username']
                if name:
                    is_exists = True
                    break
        if not is_exists:
            with pool() as db:
                db.execute(("insert into userlist(username, password, age, tel, create_date)"
                           " values('{username}','{password}','{age}', '{tel}', now());".format(username=username,
                                                                                             password=password,
                                                                                             age=age,
                                                                                             tel=tel)))
                print("insert into userlist(username, password, age, tel, create_date)"
                           " values('{username}','{password}','{age}', '{tel}', now());".format(username=username,
                                                                                             password=password,
                                                                                             age=age,
                                                                                             tel=tel))
                return HttpResponse('<a href="/user/list_user/">添加成功，点击跳转到显示页面</a>')
        else:
            return HttpResponse('<a href="/user/list_user/">添加失败：用户已经存在，点击跳转</a>')

    else:
        return HttpResponse('<a href="/user/list_user/">添加失败：用户名，密码，电话，密码都不能为空,点击跳转</a>')


def modify_user(request):
    # if request.method == "GET":
    #     username = request.GET.get("username", '')
    #     print(username)
    #     return render(request, 'user/modify.html', {'username':username})
    # username = request.POST.get('username', '')
    # age = request.POST.get('age', '')
    # tel = request.POST.get('tel', '')
    # password = request.POST.get('password', '')
    # print(username, age, tel, password)
    # info = username, age, tel, password
    # if username and age and tel and password:
    #     rt_status, rt_reason =models.validate_modify_user(username, age, tel, password)
    #     if rt_status:
    #         models.modify_user(username, age, tel, password)
    #         return HttpResponse('<a href="/user/list_user/">更新成功，点击跳转到显示页面</a>')
    #     else:
    #         return HttpResponse(rt_reason)

    if request.method == "GET":
        username = request.GET.get("username", '')
        is_exists = True

        with pool() as db:
            db.execute("select username from userlist where username={username}".format(username=username))
            for row in db.fetchall():
                name = row['username']
                if not name:
                    is_exists = False
                    break
                return HttpResponse('更新失败：用户已经存在')
        if is_exists:
            return render(request, 'user/modify.html', {'username':username})
    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    password = request.POST.get('password', '')
    print(username, age, tel, password)
    info = username, age, tel, password
    if username and age and tel and password:
         with pool() as db:
             db.execute("update userlist set password='{password}', age={age}, tel={tel}, create_date=now() "
                        "where username='{username}'".format(username=username, password=password, age=age, tel=tel))
         return HttpResponse('<a href="/user/list_user/">添加成功，点击跳转到显示页面</a>')


