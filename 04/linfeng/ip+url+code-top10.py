#encoding: utf-8
src = 'www_access_20140823.log'
nodes = []
statistic_node = {}
fhandler = open(src,'r')
for line in fhandler:
    if len(line.strip().split()) > 0:
        linenode = line.strip().split()
        node = linenode[0] + ' ' + linenode[6] + ' ' + linenode[8]
        nodes.append(node)
for i in nodes:
    statistic_node[i] = statistic_node.setdefault(i,0) + 1
list_statistic = list(statistic_node.items())
for i in range(len(list_statistic)-1):
    for j in range(len(list_statistic)-i-1):
        if list_statistic[j][1] < list_statistic[j+1][1]:
            list_statistic[j],list_statistic[j+1] = list_statistic[j+1],list_statistic[j]
for i in range(10):
    print(list_statistic[i])
