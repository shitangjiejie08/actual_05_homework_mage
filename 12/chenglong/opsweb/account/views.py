from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required  ###验证登陆
from django.views.generic import View, TemplateView, ListView  ### 定义类视图
from django.contrib.auth.models import User
from  django.core.paginator import Paginator
# Create your views here.

@login_required
def hello(request):
    return HttpResponse("hello")



class UserView(View):

    def get(self, request):
        return render(request, template_name="user/create.html")


    def post(self, request):


        username= request.POST.get("username", "")
        passwd = request.POST.get("passwd", "")
        email = request.POST.get("email","")
        User.objects.create_user(username=username, password=passwd, email=email)
        return HttpResponse("post")


    def put(self, request):
        return HttpResponse("put")

    def head(self, request):
        return HttpResponse("head")

    def patch(self, request):
        return HttpResponse("patch")

    def trace(self, request):
        return HttpResponse("trace")


    def other(self, request):
        return HttpResponse("other")


class UserListView(TemplateView):
    template_name = "user/userlist.html"

    # def get(self, request, *args, **kwargs):
    #     userlist = User.objects.all()
    #     userlist_dict = {"userlist":userlist}
    #     return render(request, self.template_name, userlist_dict)
    def get_context_data(self, **kwargs):
        #这个方法可以将变量传递到模板，而不用上面的方法
        context = super(UserListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get("page", "1"))
        except:
            page = 1
        # end = page * 10
        # start = end -10
        # context["userlist"] = User.objects.all()[start:end]   ###这个每次是不是去查询全部，而是从数据哭取一部分
        paginator = Paginator(User.objects.all(), 10)    ###每页显示10条数据   paginatior实现
        cur_page = paginator.page(page)
        context["userlist"] = cur_page.object_list
        if cur_page.has_previous():
            context["pre_page"] = cur_page.previous_page_number
        else:
            context["pre_page"] = 1
        if cur_page.has_next():
            context["next_page"] = cur_page.next_page_number
        else:
            context["next_page"] = paginator.num_pages
        context["cur_page"] = page
        context["pages"] = paginator.page_range
        context["first_page"] = 1
        context["end_page"] = paginator.num_pages

        return context

class UserListAsView(ListView):
    template_name = "user/userlist_listview.html"
    context_object_name = "object_list"
    paginate_by = 10
    model = User
