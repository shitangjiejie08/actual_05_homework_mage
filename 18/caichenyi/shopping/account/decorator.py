# encoding: utf-8
# Author: Cai Chenyi

from django.http import HttpResponse
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            rt = func(request, *args, **kwargs)
            return rt
        else:
            return HttpResponse("未登录")

    return wrapper