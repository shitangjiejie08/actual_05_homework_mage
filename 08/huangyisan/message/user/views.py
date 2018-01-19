from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.
def require_login(request):
    return render(request, 'user/login.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    rt = models.validate_login(username, password)
    print(rt)
    if rt:
        #session
        request.session['user'] = rt
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error':'用户名或密码错误','username':username,'password':password}
        return render(request,'user/login.html',context)

def list_user(request):
    '''
    if login_user == '':
        return unauth_error(request)
    else:
        action = request.POST.get('action','None')
        #add功能再list页面展现，所以需要知道当时具体是什么行为，action=add为add功能按钮所致
        if action == 'add':
            #直接递交给add_user(request)函数，并且返回，让add_user(request)函数判断后进行传递其HttpResponse
            return add_user(request)
        else:
    '''
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    context = {'messages':models.get_messages()}
    return render(request, 'user/list.html',context)

def delete_user(request):
    #if len(models.get_messages()) == 1:
    #    return handle_error(request,'无法删除最后一个用户','func_error','user/list.html')
    #else:
    print(models.get_exist_users_count())
    if models.get_exist_users_count() == 1:
        context = models.get_messages()
        print(43,context)
        return handle_error(request,'无法删除最后一个用户', 'func_error','user/list.html',context)
        print('无法删除最后一个用户')
    else:
        username = request.GET.get('username','')
        models.delete_user(username)
        return HttpResponseRedirect('/user/list_user/')

def edit_user(request):
    #if login_user == '':
    #    return unauth_error(request)
    #else:
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    username = request.GET.get('username','')
    user_info = models.get_single_message(username)[0]
    age = user_info.get('age')
    tel = user_info.get('tel')
    password = user_info.get('password')
    user_info = {"username":username,"age":age,"tel":tel,"password":password}
    return render(request,'user/edit.html',{'messages':user_info})

def modify_user(request):
    user_info = request.POST
    username = user_info.get('username')
    age = request.POST.get('age')
    age = int(age)
    tel = request.POST.get('tel')
    password = request.POST.get('password')
    print(username,age,tel,password)
    context = {'username':username, 'age':age, 'tel':tel, 'password':password}
    #models.modify_user(age,tel,password,username)
    if age < 0 or age > 150:
        return handle_error(request,'这年龄很诡异，添加信息失败','data_error','user/edit.html',context)
    if len(tel) != 11:
        return handle_error(request,'这手机号码很诡异，添加信息失败','data_error','user/edit.html',context)
    if len(password) < 6:
        return handle_error(request,'密码设置过于简单，请重新设置','data_error','user/edit.html',context)
    else:
        #models.modify_user(name=username,age=age,tel=tel,password=password,users=models.get_messages())
        models.modify_user(age,tel,password,username)
        return HttpResponseRedirect('/user/list_user/')

def add_func(request):
    username = request.POST.get('username','Null')
    age = request.POST.get('age','-1')
    age = int(age)
    tel = request.POST.get('tel','')
    password = request.POST.get('password','')
    #组织context信息，传递给handle_error函数，用于错误的时候用用户信息+错误信息对页面渲染
    context = {'username':username, 'age':age, 'tel':tel, 'password':password}
    if models.judege_user_exist(username):
        print('已经存在的用户')
        return handle_error(request,'已经存在的用户,添加信息失败','data_error','user/add.html',context)
    if age < 0 or age > 150:
        print('年龄异常')
        return handle_error(request,'年龄异常,添加信息失败','data_error','user/add.html',context)
    if len(tel) != 11:
        print('手机号码异常')
        return handle_error(request,'手机号码异常,添加信息失败','data_error','user/add.html',context)
    if len(password) < 6:
        print('密码过短')
        return handle_error(request,'密码过短,添加信息失败','data_error','user/add.html',context)
    else:
        models.add_user(username,age,tel,password)
        return HttpResponseRedirect('/user/list_user/')

def add_user(request):
    return render(request,'user/add.html')

def handle_error(request,error_message,kind_error,url,context):
    #不同context类型，进行不同操作。
    if type(context) is dict:
        context[kind_error] = error_message
        context={'messages':context}
    elif type(context) is tuple:
        context[0][kind_error] = error_message
        context={'messages':context}
        print(context)
    return render(request,url,context)

def unauth_error(request):
    return render(request,'user/unauth.html')

def exit_user(request):
    global login_user
    login_user = ''
    return HttpResponseRedirect('/user/')
