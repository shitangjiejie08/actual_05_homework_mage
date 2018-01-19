# coding:utf-8

log_dict = {}
count_num = []
with open('www_access_20140823.log','r') as f:
    for line in f.readlines():
        ip,url,status = line.strip().split()[0],line.strip().split()[6],line.strip().split()[8]
        info = 'IP:{0} URL:{1} STATUS:{2}'.format(ip,url,status)
        log_dict[info] = log_dict.get(info,0) + 1

for count in log_dict:
    count_num.append(log_dict[count])  

count_num = sorted(list(set(count_num)),reverse = True)

with open('count_log','w') as fw:
    c = 0
    for num in count_num:
        for key in log_dict:
            if log_dict[key] == num and c < 10:
                fw.write('{0}访问{1}times\n'.format(key,num))
                c += 1
            


    
        
