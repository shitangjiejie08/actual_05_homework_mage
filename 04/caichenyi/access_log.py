# encoding: utf-8
# Author: Cai Chenyi

'''
访问日志统计（加分项）
读取访问日志解析出IP，url，状态码，并统计出现次数，将出现次数最多的TOP 10数据写入到文件中
'''

log_file = 'www_access_20140823.log'
top_file = 'top.txt'
log_dict = {}
log_list = []
top_num = 10

with open(log_file, 'rt') as fhandler:
    for line in fhandler:
        if line.strip() != '':
            log_info = line.strip().split()
            log_key = log_info[0] + ',' + log_info[8] + ',' + log_info[10]
            if log_key in log_dict:
                log_dict[log_key] += 1
            else:
                log_dict[log_key] = 0

log_list = list(log_dict.items())
for i in range(len(log_list) - 1):
    for j in range(len(log_list) - 1 - i):
        if log_list[j][1] < log_list[j + 1][1]:
            log_list[j], log_list[j + 1] = log_list[j + 1], log_list[j]

with open(top_file, 'wt') as fhandler:
    for i in range(top_num):
        fhandler.write('{}\n'.format(log_list[i]))
