'''
二分查找的思路：
如果要查找的值在列表里面：
1.判断要查找的值和列表中间的元素比较，如果相等，则找到
2.判断要查找的值和列表中间的元素比较，如果要找的元素大于中间值，则在后半段找，即start = mid +1
3.判断要查找的值和列表中间的元素比较，如果要找的元素小于中间值，则在前半段找，即end = mid -1
如果要查找的值不在列表里面：
判断要查找的值和列表中间的元素比较，然后类似于前面两种情况，如果end小于start，即没找到

要查找的值在列表里面：
nums = [1,3,4,5,6]
find_num = 1
start = 0 (0)
end = len(nums)-1 (4)
mid = (start+end)//2 (2)
find_num < mid 前半段
start = 0 (0)
end = mid -1 (1)
mid = (start+end)//2 (0)
find_num == mid 找到

nums = [1,3,4,5,6]
find_num = 6
start = 0 (0)
end = len(nums)-1 (4)
mid = (start+end)//2 (2)
find_num > nums[mid] 后半段
start = mid+1 (3)
end = len(nums)-1 (4)
mid = (start+end)//2 (3)
find_num < nums[mid] 后半段
start = mid +1 (4)
mid = (start+end)//2 (4)
find_num == nums[mid]

要查找的值不在列表里面：
nums = [1,3,4,5,6]
find_nums =2
start = 0 (0)
end = len(nums)-1 (4)
mid = (start+end)//2 (2)
find_num < nums[mid] 前半段
end = mid-1 (1)
mid = (start+end)//2 (0)
find_nums > nums[mid] 后半段
start = mid +1 (1)
mid = (start+end)//2 (1)
find_num < nums[mid] 前半段
end = mid -1 (0)
end < start 序列不存在，要找的元素不在列表中
代码如下：
'''
# 第一种方法
nums = [1,3,4,5,6]
start = 0
end = len(nums)-1
find_num = 8
while True:
    mid = (start+end)//2
    if find_num == nums[mid]:
        print("索引是：",mid)
        break
    elif find_num < nums[mid]:
        end = mid-1
    else:
            start = mid +1
    if start > end:  # 利用两个if语句判断
        print("要查找的元素不在列表中")
        break

 # 第二种方法
nums = [1,3,4,5,6]
start = 0
end = len(nums)-1
find_num = 2
while True:
    mid = (start+end)//2
    if start > end:
        print("要查找的元素不在列表中")
        break
    else:
        if find_num == nums[mid]:
            print("索引是：",mid)
            break
        elif find_num < nums[mid]:
            end = mid-1
        else:
            start = mid +1

'''
功能ok，非常棒，继续加油
注意编码格式，缩进使用4个空格，保持统一
'''
