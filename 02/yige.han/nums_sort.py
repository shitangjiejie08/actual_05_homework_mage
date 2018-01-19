# coding:utf-8
"""
对数字序列排序
"""

def bubble_sort(nums):
    """
    冒泡排序
    """
    if not isinstance(nums, list):
        raise "Not list error"
    for j in range(0, len(nums)-1 ):
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

'''
加油，坚持
'''

def insertion_sort(nums):
    """
    插入排序
    """
    if not isinstance(nums, list):
        raise "Not list error"

    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break
    return nums

'''
功能ok，继续加油，坚持
'''

def binary_search(nums, num, start, end):
    """
    二分查找
    """
    middle = (start + end) // 2
    if start > end:
        return None
    elif nums[middle] == num:
        return middle
    elif num <nums[middle]:
        return binary_search(nums, num, start, middle-1)
    elif num > nums[middle]:
        return binary_search(nums, num, middle+1, end)
    else:
        return None

'''
功能ok，考虑line54~55是否需要
'''
nums = [1, 3, 9, 8, 7, 4, 0, 2, 6]

print(bubble_sort(nums.copy()))
print(insertion_sort(nums))
print(binary_search(nums, num=9, start=0, end=len(nums)-1))
