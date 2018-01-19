# encoding: utf-8
fhandler = open('www_access_20140823.log', 'r+')
test_dict = {}
while True:
    is_bool = True
    scv = fhandler.readline()
    if scv == '':
        break
    elif scv == '\n':
        is_bool = False
    elif is_bool:
        info = scv.split(' ')
        if test_dict.get(info[0], None):
            test_dict[info[0]] += 1
        else:
            test_dict[info[0]] = 1
fhandler.close()
value = list(test_dict.values())
value.sort()
value.reverse()
fhandler = open('IP.txt', 'wt')
for i in value[:10]:
    for k, v in test_dict.items():
        if i == v:
            print ('出现的次数为 ', i, ' IP为: ', k)
            fhandler.write('次数:{0} IP:{1}\n'.format(i, k))
fhandler.close()
print('写入到文件IP.txt中')
