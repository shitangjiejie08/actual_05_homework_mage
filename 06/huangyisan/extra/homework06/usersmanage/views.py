from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'usersmanage/index.html')
@csrf_exempt
def usersinfo(request):
    info = models.get_messages()
    return render(request,'usersmanage/usersinfo.html',{'messages':info})

def home(request):
    return render(request, 'usersmanage/home.html')

def create(request):
    return render(request, 'usersmanage/create.html')

def delete(request):
    return render(request, 'usersmanage/delete.html')

def search(request):
    print('search_info')
    return render(request, 'usersmanage/search.html')

def save_create(request):
    user_name = request.GET.get('name')
    user_age = request.GET.get('age','')
    user_telephone = request.GET.get('telephone','')
    models.save_message(user_name,user_age,user_telephone)
    return HttpResponseRedirect('/usersmanage/usersinfo/')

def save_delete(request):
    user_name = request.GET.get('name')
    models.del_message(user_name)
    return HttpResponseRedirect('/usersmanage/usersinfo/')

def search_info(request):
    search_list=[]
    #print(request.GET,'get')
    user_name = request.GET.get('name')
    for dict_name in models.get_messages():
        if dict_name.find(user_name) != -1:
            user_info = {'name':dict_name,'age':models.get_messages().get(dict_name,'').get('Age',''),'telephone':models.get_messages().get(dict_name,'').get('Tel','')}
            search_list.append(user_info)
    return render(request,'usersmanage/searchinfo.html',{'messages':search_list})
