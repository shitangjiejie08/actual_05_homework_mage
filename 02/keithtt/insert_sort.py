#!/usr/local/bin/python3
#
nums=[3,4,1,6,2,9,7,0,8,5]

for i in range(1,len(nums)):
	for j in range(i,0,-1):
		if nums[j] < nums[j-1]:
			nums[j-1],nums[j] = nums[j],nums[j-1]
		else:
			break
print(nums)

'''
功能ok，继续加油
考虑是否可以优化
提示
nums[j] > nums[j - 1]后还有在比较[j - 1]和j[j - 2]吗？以此类推
'''
