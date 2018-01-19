#encoding: utf-8
from datetime import datetime

stat_days = {}

# 统计每天数据
fhandler = open('access.log.10', 'rt')
for line in fhandler:
    try:
        _nodes = line.split()
        #跳过可能错误的字段
        if len(_nodes) < 12:
            continue
        #         ip         datetime       method         url       status    bytes
        #print(_nodes[0], _nodes[3][1:], _nodes[5][1:], _nodes[6], _nodes[8], _nodes[9])
        _day = datetime.strptime(_nodes[3][1:], '%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d')
        # 设置每天的默认值
        stat_days.setdefault(_day, {'hits' : 0, 'vistors' : {}, 'status' : {}, 'bytes' : 0})
        # 设置每出现的IP的访问次数默认为0
        stat_days[_day]['vistors'].setdefault(_nodes[0], 0)
        # 设置每天出现的状态码默认值为0 
        stat_days[_day]['status'].setdefault(_nodes[8], 0)


        #统计数据
        stat_days[_day]['hits'] += 1
        stat_days[_day]['vistors'][_nodes[0]] += 1
        stat_days[_day]['status'][_nodes[8]] += 1
        stat_days[_day]['bytes'] += int(_nodes[9]) if _nodes[9].isdigit() else 0
        
    except BaseException as e:
        print('log error: %s' % line)

fhandler.close()

stat_all = {'hits' : 0, 'vistors' : {}, 'status' : {}, 'bytes' : 0}
# 统计总数据
for _day, _stat in stat_days.items():
    stat_all['hits'] += _stat['hits']
    stat_all['bytes'] += _stat['bytes']
    for _ip, _cnt in _stat['vistors'].items():
        stat_all['vistors'].setdefault(_ip, 0)
        stat_all['vistors'][_ip] += _cnt

    for _status, _cnt in _stat['status'].items():
        stat_all['status'].setdefault(_status, 0)
        stat_all['status'][_status] += _cnt
        

#统计区域数据
stat_all['city'] = {}

from geoip2.database import Reader

geoip2_reader = Reader('GeoLite2-City.mmdb')
for _ip, _cnt in stat_all['vistors'].items():
    _city_name = 'unknow'
    try:
        _city = geoip2_reader.city(_ip)
        _city_name = '{}/{}'.format(_city.country.names.get('en', ''), _city.city.names.get('en', ''))
        #_city_name = '{}/{}'.format(_city.country.names.get('zh-CN', ''), _city.city.names.get('zh-CN', ''))
    except BaseException as e:
        print(e)
        pass
    stat_all['city'].setdefault(_city_name, 0)
    stat_all['city'][_city_name] += _cnt

geoip2_reader.close()

# 打印结果

print('=' * 70)
print('|1. 概览{:>61}|'.format(''))
print('-' * 70)
print('| 总点击量 |{hits:^8d}| 总访问者量 |{vistors:^10d}| 总流量 |{fbytes:^15d}|'.format(hits=stat_all['hits'], vistors=len(stat_all['vistors']), fbytes=stat_all['bytes']))
print('=' * 70)
print('|2. 状态码分布{:>55}|'.format(''))
print('-' * 70)
for _status, _cnt in sorted(stat_all['status'].items(), key=lambda x: x[1], reverse=True):
    print('|{status:>20s}|{count:^47d}|'.format(status=_status, count=_cnt))
print('=' * 70)
print('|3. 每天的点击量{:>53}|'.format(''))
print('-' * 70)
for _day, _stat in sorted(stat_days.items(), key=lambda x: x[0], reverse=True):
    print('|{day:>15}|{hits:^52d}|'.format(day=_day, hits=_stat['hits']))
print('=' * 70)
print('|4. 每天的访问者量{:>51}|'.format(''))
print('-' * 70)
for _day, _stat in sorted(stat_days.items(), key=lambda x: x[0], reverse=True):
    print('|{day:>15}|{vistors:^52d}|'.format(day=_day, vistors=len(_stat['vistors'])))
print('=' * 70)
print('|5. 每天的流量{:>55}|'.format(''))
print('-' * 70)
for _day, _stat in sorted(stat_days.items(), key=lambda x: x[0], reverse=True):
    print('|{day:>15}|{fbytes:^52d}|'.format(day=_day, fbytes=_stat['bytes']))
print('=' * 70)
print('|6. 访问来源{:>57}|'.format(''))
print('-' * 70)
for _city, _cnt in sorted(stat_all['city'].items(), key=lambda x: x[1], reverse=True)[:21]:
    print('|{city:>47}|{count:^20d}|'.format(city=_city, count=_cnt))
print('=' * 70)
