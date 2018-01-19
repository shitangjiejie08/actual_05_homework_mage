#encoding:utf-8
'''
算法：
将搜索的数字与数组里中间的那个数字比较
如果中间的那个数字大于你搜索的那个数字，则将原来的数组减去一半，以原先中间那个数的前一个数为末尾重新组成数组
如果中间的那个数字小于你搜索的那个数字，则将原来的数组减去一半，以原先中间那个数的后一个数为开头重新组成数组
重复以上操作，直到搜索的数字等于中间数
'''
num_list=[1,2,10,5,7,8,9]
num=input('请输入你想查找的数字：')
num=int(num)
front=0
end=len(num_list)
while True:
    if front>end:
        print('数字不在数组里')
        break
    mid=int((front+end)/2)
    if num_list[mid]>num:
        end=mid-1
    elif num_list[mid]<num:
        front=mid+1
    elif num_list[mid]==num:
        print('找到了，是列表里的第',num_list.index(num)+1,'个数')
        break

'''
功能ok，继续加油
'''
