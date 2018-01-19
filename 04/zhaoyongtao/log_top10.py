# encoding:utf-8
# 读取访问日志解析出IP，url，状态码，并统计出现次数，将出现次数最多的TOP 10数据写入到文件中

# 提取数据到字典中
file_path = './' #默认为当前目录

log_dict = {}

f = open(file_path + 'www_access_20140823.log', 'rt')
for line in f:
    line = line.split()
    if len(line) < 3:
        continue
    ip, url, state = line[0], line[6], line[8]
    key = ip + '-' + url + '-' + state  # 加上符号，后面输出的时候方便切割
    log_dict[key] = log_dict.get(key, 0) + 1
f.close()
list_temp = list(log_dict.items())

# 排序
for i in range(len(list_temp)):
    for j in range(len(list_temp) - i - 1):
        if list_temp[j][1] < list_temp[j + 1][1]:
            list_temp[j], list_temp[j + 1] = list_temp[j + 1], list_temp[j]

# 写入文件中
f = open(file_path + 'log_result.txt', 'wt')
for s in list_temp[:10]:
    ip, url, state = str(s[0]).split('-')
    line = 'IP:{ip:<18} URL:{url:<55} 状态:{state:<4} 次数:{count:<4}\n'.format(ip=ip, url=url, state=state, count=s[1])
    f.write(str(line))

f.close()
