# encoding:utf-8

# 二分查找
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
find_num = int(input('请输入一个数字：'))
start = 0
end = len(l) - 1

while True:
    middle = (start + end) // 2
    if find_num == l[middle]:
        print('找到了！索引是：', middle)
        break
    elif find_num > l[middle]:
        start = middle + 1
    elif find_num < l[middle]:
        end = middle - 1
    if start > end:
        print('没找到!', find_num)
        break

'''
功能ok，非常棒，继续加油，坚持
'''
