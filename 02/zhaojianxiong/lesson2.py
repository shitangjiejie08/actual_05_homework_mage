# enconding: utf-8
print('二分查找')
key = int(input('Please input a number: '))
l = [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 15]
low = 0
high = len(l)
mid = (high + low) // 2
while True:
    if key == l[mid]:
        print (mid)
        break
    elif key > l[mid]:
        low = mid + 1
        mid = (high + low) // 2
        if key < mid:
            high = mid - 1
            mid = (high + low) // 2
    elif key < l[mid]:
        high = mid - 1
        mid = (low + high) // 2
        if key > mid:
            low = mid + 1
            mid = (high + low) // 2

'''
测试一些不存在的元素比如11,16会出现什么现象，如何修改，加油
'''


print('插入排序')
l = [6, 5, 3, 1, 8, 7, 2, 4]
for i in list(range(1, len(l))):
    for j in list(range(i, 0, -1)):
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
print (l)

'''
功能ok，继续加油，注意变量命名尽量见名知意，l和1太相识避免这种命名方式
'''
