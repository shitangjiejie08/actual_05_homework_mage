#!/usr/bin/env python3
cxt_dict={}
cxt_num=[]
c = 0
f=open('www_access_20140823.log','r')
for line in f:
    ip,url,status = line.split()[0],line.split()[6],line.split()[8]
    info = 'IP:{0} URL:{1} STATUS:{2}'.format(ip,url,status)
    cxt_dict[info]=cxt_dict.get(info,0)+1
for count in cxt_dict:
    cxt_num.append(cxt_dict[count])
cxt_num=sorted(list(set(cxt_num)),reverse=True)
cxt=open('count_log','w')
for num in cxt_num:
    for key in cxt_dict:
        if cxt_dict[key] == num and c < 10:
            cxt.write('{0},count is {1}\n'.format(key,num))
            c+=1
cxt.close()
