#!/user/bin/python3.5
#encoding: utf-8
#插入排序

nums=[6, 11, 7, 9, 4, 2, 1]

for count in range(len(nums)):
    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1]:
            nums[index],nums[index + 1] = nums[index + 1],nums[index]

print(nums)

'''
功能是冒泡排序，考虑line8~10是否是每次将最大的元素放在list的后面保证list最后的元素始终有序
'''
