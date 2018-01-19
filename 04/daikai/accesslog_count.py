#encoding:utf-8

'''
Author:daikai
功能：读取访问日志解析出IP，url，状态码，并统计出现次数，将出现次数最多的TOP 10数据写入到文件中
'''

access_log = 'www_access_20140823.log'
dst_file = 'top10_record.txt'
top_num = 10

stat_dict = {}

src_fhandler = open(access_log, 'r')
for line in src_fhandler:
    if line.strip() != '':
        info = line.strip().split(' ')
        key = '{ip} {url} {status}'.format(ip=info[0],url=info[6],status=info[8])
        stat_dict[key] = stat_dict.get(key,0) + 1
src_fhandler.close()

stat_list = list(stat_dict.items())
for i in range(1,len(stat_list)):
    for j in range(i,0,-1):
        if stat_list[j - 1][1] < stat_list[j][1]:
            stat_list[j - 1],stat_list[j] = stat_list[j],stat_list[j - 1]
        else:
            break

dst_fhandler = open(dst_file, 'w')
for index in range(top_num):
    dst_fhandler.write('{}\n'.format(stat_list[index]))
dst_fhandler.close()



