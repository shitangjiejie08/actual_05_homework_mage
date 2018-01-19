from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from pymysql.cursors import DictCursor


def index(requset):
    ret = models.list(200)
    data = {'info':ret}
    return render(requset, "index.html", data)