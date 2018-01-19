from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate #用户验证
from django.contrib.auth import login, logout #用户登录
from django.views.generic import ListView #分页显示
from django.contrib.auth.models import User

# Create your views here.

def hello(request):
    return HttpResponse('hello function')


class UserCreate(View):

    def get(self, request):
        return render(request, template_name="create.html")

    def post(self, request):
        User.objects.create_user(request.POST.get("username", ""),
                                 request.POST.get("email", ""),
                                 request.POST.get("password", "")) #添加用户
        return HttpResponseRedirect('/users/list/')


def userlogin(request):
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # 写cookie，写session
            return HttpResponseRedirect('/users/list/')
        else:
            return render(request, template_name='login.html', context={'error': '用户认证失败'})


def userlogout(request):
    logout(request)
    return render(request, template_name='login.html')


class UserList(ListView):
    template_name = "list.html"
    # context_object_name = "object_list" #循环遍历
    paginate_by = 10 #每一页显示条数
    model = User


class UserModify(View):

    def get(self, request):
        action = str(request).split('/')[2]
        _id = request.GET.get('id', '')
        if action == 'modify_info':
            return render(request, template_name="modify_info.html", context={'action': action, 'id': _id})
        elif action == 'modify_passwd':
            return render(request, template_name="modify_passwd.html", context={'action': action, 'id': _id})
        elif action == 'delete_user':
            user = User.objects.get(id__exact=str(_id))
            user.delete()
            return HttpResponseRedirect('/users/list/')
        else:
            return HttpResponse('action error')

    def post(self, request):
        action = request.POST.get('action', '')
        _id = request.POST.get('id', '')
        user = User.objects.get(id__exact=str(_id))
        if action == 'modify_info':
            user.username = request.POST.get('username', '')
            user.email = request.POST.get('email', '')
            user.save()
            return HttpResponseRedirect('/users/list/')
        elif action == 'modify_passwd':
            user.set_password(request.POST.get('password', ''))
            user.save()
            return HttpResponseRedirect('/users/list/')
        else:
            return HttpResponse('action error')