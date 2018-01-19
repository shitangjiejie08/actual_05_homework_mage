#encoding:utf-8

#插入排序
nums = [7, 4, 5, 9, 8, 10, 15, 18, 11]
for index in range(len(nums)):
    if nums[index-1] > nums[index]: #index 表示当前元素的位置
        tmp = nums[index] #tmp表示要排序插入的元素
        while index > 0  and  nums[index-1] > tmp: #index> 0，并且从nums[index-1]开始之前的所有的元素，都要大于tmp
            nums[index] = nums[index-1] #排序好后移一位
            index -= 1 #待插入元素的位置
        nums[index] = tmp
print(nums)


'''
功能ok, 继续加油
'''

#二分法查找
nums = [7, 4, 5, 9, 8, 10, 15, 18, 11]
nums = sorted(nums)
high = len(nums) - 1
low = 0
num_ = int(input("pzl a int num:"))
if num_ in nums:
    while low <= high:
        mid = (low + high) // 2
        if num_ < nums[mid]:
            high = mid - 1
        elif num_ > nums[mid]:
            low = mid + 1
        else:
            print(mid)
            print(nums[mid])
            break
else:
    print("the number not in list")

'''
功能ok，考虑下line22行是否有必要，line 23 ~ 32代码的意思在什么地方
考虑下没有line22行，怎么判断元素不在list中
'''
