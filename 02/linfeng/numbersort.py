#encoding:utf-8
nums=[2,5,7,4,6,1,3]
for i in range(1,len(nums)):
    for j in range(i,0,-1):
        if nums[j-1]>nums[j]:
            nums[j-1],nums[j]=nums[j],nums[j-1]
        else:
            break
print(nums)

'''
功能ok，非常棒，继续加油
'''
