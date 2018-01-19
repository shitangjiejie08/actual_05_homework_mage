from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout  #  验证用户名和密码是否正确



def userlogin(request):
    if request.method == "GET":
        return render(request, template_name="user/login.html")
    elif request.method == "POST":
        username = request.POST.get("username", "")
        passwd = request.POST.get("passwd", "")
        user = authenticate(username=username, password=passwd)

        if user is not None:
            ## 用户名正确
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', "/"))
        else:
            #用户名密码错误
            return HttpResponse("登陆失败")
            pass
        print(request.get("POST"))
        return HttpResponse("执行登陆")


def userlogout(reuqest):
    logout(request=reuqest)
    return HttpResponse("已退出登陆")



#类视图