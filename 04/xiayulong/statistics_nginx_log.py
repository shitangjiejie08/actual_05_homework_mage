# encoding: utf-8


def insert_sort(arg_list):
    for i in range(1,len(arg_list)):
        for j in range(i-1,-1,-1):
            if arg_list[i][1] < arg_list[j][1]:
                tmp=arg_list[i]
                arg_list[i]=arg_list[j]
                j-=1
                while j >= 0 and tmp[1] < arg_list[j][1]:
                    arg_list[j+1]=arg_list[j]
                    j-=1
                arg_list[j+1]=tmp
    return







stat = {}
'''
 {
    "IP-URL-STATUS":num,...
 }
'''

access_log = open("www_access_20140823.log","r")

for line in access_log:
    if line.strip() != '':
        info = line.split()
        key = "-".join((info[0],info[6],info[8]))
        if key not in stat:
            stat[key] = 0
        stat[key] += 1
access_log.close()


stat_list = list(stat.items())
insert_sort(stat_list)


save = open("result.txt","w")
txt = [element[0] + ": " + str(element[1]) + "\n" for element in stat_list[-1:-10:-1]]
save.writelines(txt)
save.close()
print(stat_list[-1:-10:-1])
