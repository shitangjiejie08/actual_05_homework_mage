# encoding: utf:8

l = [5, 6, 9, 11, 34, 66, 6, 8, 7]

def insertionSort(l):            ###插入排序
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):    #####循环判断得出依次次最小直的索引
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]  ####l[i] 中存放最小的值aa
    return l

a = twoPointSearch(l)
print(a)


####冒泡排序
'''
>>> list(range(10,0,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''

def bubble_Sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(len(l)-1):
            if l[j] > l[i]:
                l[i],l[j] = l[j],l[i]   ###### l[i] 中存放的循环判断后依次次最大直,先赋值的是最后一个元素
    return l

b = bubble_Sort(l)
print(b)