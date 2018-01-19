from django.db import models

# Create your models here.
from geoip2.database import Reader
from datetime import datetime
from collections import OrderedDict

def city():
    geoip2_reader = Reader('GeoLite2-City.mmdb')
    geoip2_reader.city()

def data():
    stat_days = {}
    fhandler = open('access.log.10','r',encoding="utf8")
    error_result = []

    for line in fhandler:
        try:
            _nodes = line.split()
            if len(_nodes) <12:
                continue
            # ip     datetime     method       url       status       bytes
            #print(_nodes[0], _nodes[3][1:]), _nodes[5][1:], _nodes[6], _nodes[8], _nodes[9]
            # _date = datetime.strptime(_nodes[3][1:], "%d/%b/%Y:%H:%M:%S") #strptime()是将字符串类型转化为时间类型，记住格式"18/Sep/2013:06:49:18"和"%d/%b/%Y:%H:%M:%S"需要保持一致
            _date = datetime.strptime(_nodes[3][1:], "%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d")
            stat_days.setdefault(_date,{"hits":0, "vistors":{}, "status":{}, "bytes":0})
            stat_days[_date]["vistors"].setdefault(_nodes[0],0)
            stat_days[_date]["status"].setdefault(_nodes[8],0)

            stat_days[_date]["hits"] += 1
            stat_days[_date]["vistors"][_nodes[0]] += 1
            stat_days[_date]["status"][_nodes[8]] += 1
            stat_days[_date]["bytes"] += int(_nodes[9]) if _nodes[9].isdigit() else 0 #三目表达式

        except BaseException as e:
            error_result.append("log error :{}".format(line))

    fhandler.close()
    # print(stat_days)
    return stat_days,error_result

def statics_all():
    """统计总数据"""
    stat_all={"hits":0, "vistors":{}, "status":{}, "bytes":0}
    stat_days, error_result = data()
    for _day, _stat in stat_days.items():
        stat_all["hits"] += _stat["hits"]
        stat_all["bytes"] += _stat["bytes"]

        for _ip, _cnt in _stat["vistors"].items():
            stat_all["vistors"].setdefault(_ip, 0)
            stat_all["vistors"][_ip] += _cnt

        for _status, _cnt in _stat["status"].items():
            stat_all["status"].setdefault(_status, 0)
            stat_all["status"][_status] += _cnt

    return stat_all

def statics_city():
    """统计区域数据"""
    city={}
    geoip2_reader = Reader("GeoLite2-City.mmdb")
    for _ip, _cnt in statics_all()["vistors"].items():
        _city_name = "Unknow"
        try:
            _city = geoip2_reader.city(_ip)
            # _city_name = "{}/{}".format(_city.country.names.get("en","").encode("utf8"),_city.city.names.get("en","").encode("utf8"))
            _city_name = "{}/{}".format(_city.country.names.get("zh-CN",""),_city.city.names.get("zh-CN",""))
        except BaseException as e:
            print(e)
            pass
        city.setdefault(_city_name,0)
        city[_city_name] += _cnt
    return city



