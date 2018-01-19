'''
访问日志统计
读取访问日志解析出IP，url，状态码，并统计出现次数，将出现次数最多的TOP10数据写入到文件中
'''

'''
>>> line='61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"'
>>> line.split()
['61.159.140.123', '-', '-', '[23/Aug/2014:00:01:42', '+0800]', '"GET', '/favicon.ico', 'HTTP/1.1"', '404', '\\', '"-"', '"Mozilla/5.0', '(Windows', 'NT', '5.1)', 'AppleWebKit/537.36', '(KHTML,', 'like', 'Gecko)', 'Chrome/29.0.1547.66', 'Safari/537.36', 'LBBROWSER"', '"-"']
>>> nodes=line.split()
>>> nodes
['61.159.140.123', '-', '-', '[23/Aug/2014:00:01:42', '+0800]', '"GET', '/favicon.ico', 'HTTP/1.1"', '404', '\\', '"-"', '"Mozilla/5.0', '(Windows', 'NT', '5.1)', 'AppleWebKit/537.36', '(KHTML,', 'like', 'Gecko)', 'Chrome/29.0.1547.66', 'Safari/537.36', 'LBBROWSER"', '"-"']
>>> nodes[0]
'61.159.140.123'
>>> nodes[6]
'/favicon.ico'
>>> nodes[8]
'404'
'''

'''
修改日志统计脚本为函数
输入分析日志文件路径，TOPN，统计输出文件位置
'''

'''
访问日志统计排序修改为使用sorted()或list.sort()
'''

#encoding: utf-8

def accesslog(path,rt_path,topn):

    fhandler = open(path, 'rt')

    stat = {}

    #统计次数
    for line in fhandler:
        nodes = line.split()
        if len(nodes) < 9:
            continue       
        key = (nodes[0], nodes[6], nodes[8])
        if key in stat:
            stat[key] += 1
        else:
            stat[key] = 1   

    fhandler.close()

    #list.sort()排序
    stat_list = list(stat.items())
    stat_list.sort(key=lambda x:x[1])

    #将top10写入文件
    fhandler = open(rt_path, 'wt')
    for line in stat_list[-1:-topn-1:-1]:
        fhandler.write('{0},{1},{2},{3}\n'.format(line[0][0], line[0][1], line[0][2], line[1]))
    fhandler.close()

path = 'www_access_20140823.log'
rt_path = 'stat_result.txt'
topn = 10
accesslog(path,rt_path,topn)

