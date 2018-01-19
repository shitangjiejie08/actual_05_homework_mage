#encoding: utf-8



a=[5,7,3,10,25,6,4,100]
a.sort()
print(a)
tar=int(input("请输入查找的数字： "))
left=0
right=len(a)-1

while left <= right:
    mid = (left + right) // 2
    if tar > a[mid]:
        left = mid+1
    elif tar < a[mid]:
        right = mid-1
    else:
        print(tar,"存在")
        break
else:
    print(tar,"不存在")

'''
功能ok，非常棒，坚持
'''
