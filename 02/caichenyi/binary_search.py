# encoding: utf-8
# Author: Cai Chenyi

# 二分查找

nums = (5, 13, 19, 21, 37, 56, 64, 75, 80, 88, 92)
num_search = int(input('请输入需要查找的数字：'))
low, high = 0, len(nums) - 1

while low <= high:
    mid = (low + high) // 2
    if nums[mid] > num_search:
        high = mid - 1
    elif nums[mid] < num_search:
        low = mid + 1
    else:
        print('已经找到{}，在第{}位'.format(num_search, mid) )
        break
if low > high:
    print('未找到{}'.format(num_search))

'''
功能ok，继续加油
'''
