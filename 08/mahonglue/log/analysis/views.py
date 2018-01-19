from django.shortcuts import render

from . import models

from collections import OrderedDict

# Create your views here.
def index(request):
    stat_days, error_result = models.data()
    stat_day = OrderedDict()
    for _day, _stat in sorted(stat_days.items(), key=lambda x:x[0], reverse=True):
        stat_day.setdefault(_day,{})
        stat_day[_day].setdefault("hits",0)
        stat_day[_day]["hits"] += _stat["hits"]
        stat_day[_day].setdefault("vistors", 0)
        stat_day[_day]["vistors"] += len(_stat["vistors"])
        stat_day[_day].setdefault("bytes", 0)
        stat_day[_day]["bytes"] += _stat["bytes"]
        stat_day[_day].setdefault("status",{})
        stat_day[_day]["status"].update(_stat["status"])
    print(stat_day)

    statics_all = models.statics_all()
    ip_sum = len(statics_all["vistors"])
    status=OrderedDict()
    for _status, _cnt in sorted(statics_all["status"].items(), key=lambda x:x[0]):
        status[_status] = _cnt
    print(status)

    city=OrderedDict()
    statics_city = models.statics_city()
    print(statics_city)
    for c,n in sorted(statics_city.items(), key=lambda x:x[1], reverse=True):#字典是没有sorted和sort方法的
        city[c] = n
    context = {"statics_all":statics_all, "ip_sum":ip_sum, "stat_day":stat_day, "status":status, "city":city}
    return render(request, "analysis/index.html",context)

def detail(request,day):
    stat_days, error_result = models.data()
    day_detail = stat_days[day]


    context = {"day_detail":day_detail, "day":day,"stat_days":stat_days,}
    return render(request, "analysis/detail.html", context)