#encoding: utf-8


def fhandler_r():
    l_dict = {}

    f = open('www_access_20140823.log')
    for line in f:
        if len(line.split())>0:
            l = line.split()
            t =','.join ((l[0],l[6],l[8]))
            if t in l_dict:
                l_dict[t] += 1
            else:
                l_dict[t] = 1

    f.close()
    l = list(l_dict.items())
    l_top = insertionSort(l=l)
    f = open("top10.log", "w")
    for i in range(0,10):
        f.write(str(l_top[i]))
        f.write("\n")
    f.close()


def insertionSort(l):            ###插入排序
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):    #####循环判断得出依次次最小直的索引
            if l[min_index][1] < l[j][1]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]  ####l[i] 中存放最小的值aa
    return l



a = fhandler_r()



