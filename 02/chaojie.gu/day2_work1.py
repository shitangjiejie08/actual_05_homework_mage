#encoding:utf-8
'''
插入排序：
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素列中从后向前扫描
3.如果该元素大于新元素，将该元素移到下一位置
4.重复步骤3，只到排序到小于或等于他的元素
5.将元素插入到该位置后
6.重复步骤2~5
'''
num_list=[8,7,10,4,2,1]
for i in range(1,len(num_list)):
    for j in range(1,len(num_list)):
        for j in range(i):
            if num_list[i]<num_list[j]:
                num_list[i],num_list[j]=num_list[j],num_list[i]
print(num_list)

'''
有点问题呢，考虑你第2步和代码的line14行是否有冲突

'''
