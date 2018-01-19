#/bin/env python
#encoding:utf-8


filepath = 'www_access_20140823.log'
fhandler = open(filepath)

result_dic = {}
for line in fhandler:
	if len(line.split()) > 0:
		sline = line.split()
		key = ','.join([sline[0],sline[6],sline[8]])
		if key not in result_dic:
			result_dic.setdefault(key,1)
		else:
			result_dic[key] += 1

fhandler.close()

list_rest = list(result_dic.items())
#排序
for i in range(len(list_rest) - 1):
	for j in range(len(list_rest) - 1 - i):
		if list_rest[j][1] < list_rest[j + 1][1]:
			temp = list_rest[j]
			list_rest[j] = list_rest[j + 1]
			list_rest[j + 1] = temp


top10 = ('top10.log')
wformat  = '{:<20}{:<60}{:^8}{:^8}\n'
fhandler = open(top10,'w')
fhandler.write(wformat.format('IP','URL','StCode','Count'))
print(wformat.format('IP','URL','StCode','Count'))
for i in range(10):
	#写入文件，str格式
	pl = list_rest[i][0].split(',')+[str(list_rest[i][1])]
	print(wformat.format(pl[0],pl[1],pl[2],pl[3]),end='')
	fhandler.write(wformat.format(pl[0],pl[1],pl[2],pl[3]))
fhandler.close()