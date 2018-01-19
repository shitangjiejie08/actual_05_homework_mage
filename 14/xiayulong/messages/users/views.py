from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import users
from .models import *
from .form import createuserinfoForm
from .form import *
from django.db.models import Q
# Create your views here.


def require_login(request):
    if request.session.get('user') is not None:
        return HttpResponseRedirect("/users/list_users/")
    f = loginForm()
    return render(request,"users/require_login.html",{"f":f})

def login(request):
    f = loginForm(request.POST)
    if f.is_valid():
        cleaned_data = f.clean()
        if auth_user_v2(cleaned_data["name"],cleaned_data["passwd"]):
            request.session['user'] = cleaned_data["name"]
            return HttpResponseRedirect("/users/list_users/")
    context = { "error": "用户名或密码错误", "username":request.POST.get("name"), "password":request.POST.get("passwd"), "f": f}
    #return render(request,"users/require_login.html",context)
    return render(request, "users/require_login.html", {"f":f})

def list_users(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/users/require_login/")
    users = show_users()
    context = {"users":users}
    return render(request,"users/list_users.html",context)

def delete_users(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/users/require_login/")
    name = request.GET.get("name")
    print(request.session.get("user") != name)
    if request.session.get("user") == name:
        info = 'Suiciding is not allowed!'
    else:
        del_user(name)
    return HttpResponseRedirect("/users/list_users/")

def view_users(request):
    name = request.GET.get("name")
    context = {"name": find_user_v2(name)}
    f = modifyuserbasicinfoForm(initial={"name":name})
    context["f"] = f
    print("xxxxxx")
    return render(request,"users/view_user.html",context)

def view_users_passwd(request):
    name = request.GET.get("name")
    context = {"name": find_user_v2(name)}
    f = modifyuserpasswdinfoForm(initial={"name":name})
    context["f"] = f
    return render(request,"users/view_user_passwd.html",context)

def modify(request):
    f = modifyuserbasicinfoForm(request.POST)
    if f.is_valid():
        name = f.cleaned_data.get("name")
        tel = f.cleaned_data.get("tel")
        age = f.cleaned_data.get("age")
        user_info = {}
        user_info["name"] = name
        if tel != '':
            user_info["tel"] = tel
        if age != '':
            user_info["age"] = age
        update_user_v2(user_info)
        return HttpResponseRedirect("/users/list_users/")
    else:
        return render(request,"users/view_user.html",{"f": f, "name": request.POST.get("name")})
    

def modify_passwd(request):
    name = request.POST.get("name")
    f = modifyuserpasswdinfoForm(request.POST)
    if f.is_valid():
        old_passwd = f.cleaned_data.get("old_passwd")
        new_passwd = f.cleaned_data.get("new_passwd")
        confirm = f.cleaned_data.get("confirm")
        if auth_user_v2(name,old_passwd) == False:
            info = "旧密码不正确"
            print(info) 
            return render(request,"users/view_user_passwd.html",{"f": f, "name": request.POST.get("name"),"info":info})
        else:
            user_info = dict(zip(("name","old_passwd","new_passwd"),(name,old_passwd,new_passwd)))
            update_user_passwd(user_info)
            return HttpResponseRedirect("/users/list_users/")
    else:
        #return HttpResponseRedirect("/users/view_users_passwd/?name="+name)
        return render(request,"users/view_user_passwd.html",{"f": f, "name": request.POST.get("name")})


def edit_user_info(request):
    f = createuserinfoForm()
    return render(request,"users/edit_user_info.html",{"f":f})

def create_users(request):
    f = createuserinfoForm(request.POST)
    if f.is_valid():
        name = f.cleaned_data.get("name")
        password = f.cleaned_data.get("passwd")
        tel = f.cleaned_data.get("tel")
        age = f.cleaned_data.get("age")
        user_info = {"name":name,"tel":tel,"age":age,"passwd":password}
        add_user_v2(user_info)
        return HttpResponseRedirect("/users/list_users/")
    else:
        return render(request,"users/edit_user_info.html",{"f":f})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/users/require_login/")

def get_list_ajax(request):
    users_list = users.objects.all()
    data = [ user.as_dict()  for user in users_list]
    return JsonResponse({"status": 200, "result": "successfully","data":data})

def createuser_ajax(request):
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    age = request.POST.get("age","")
    tel = request.POST.get("tel","")
    #f = createuserinfoForm(username=username,passwd=password,age=age,tel=tel)
    f = createuserinfoForm(data={"name":username,"passwd":password,"age":age,"tel":tel})
    if f.is_valid():
        new = users(name=username,passwd=password,age=age,tel=tel)
        new.save()
        return JsonResponse({"status":200,"result":"successfully"})
    return JsonResponse({"status":400,"result":"","errors":json.loads(f.errors.as_json())})

def edituserbasicinfo_ajax(request):
    username = request.POST.get("username", "")
    age = request.POST.get("age", "")
    tel = request.POST.get("tel", "")
    f = createuserinfoForm(data={"name": username, "age": age, "tel": tel})
    f.is_valid()
    if f.cleaned_data.get("tel") is not None:
        users.objects.filter(Q(name=username)).update(tel=tel)
    if f.cleaned_data.get("age") is not None:
        users.objects.filter(Q(name=username)).update(age=age)
    return JsonResponse({"status": 200, "result": "successfully"})
    # return JsonResponse({"status": 400, "result": "", "errors": json.loads(f.errors.as_json())})

def edituserpasswordinfo_ajax(request):
    name = request.POST.get("username")
    old_passwd = request.POST.get("old-password")
    new_passwd = request.POST.get("new-password")
    confirm = request.POST.get("confirm")
    f = modifyuserpasswdinfoForm({"name":name,"old_passwd":old_passwd,"new_passwd":new_passwd,"confirm":confirm})
    if f.is_valid():
        users.objects.filter(Q(name=name)).update(passwd=new_passwd)
        return JsonResponse({"status": 200, "result": "successfully"})
    return JsonResponse({"status":400,"result":"","errors":json.loads(f.errors.as_json())})