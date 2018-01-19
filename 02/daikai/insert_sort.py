#encoding:utf-8

'''
Author:daikai
插入排序
nums = [6,4,7,2,1,5]
index=1的元素(4)插入----->[4,6,7,2,1,5]
index=2的元素(7)插入----->[4,6,7,2,1,5]
index=3的元素(2)插入----->[4,6,2,7,1,5]
                        [4,2,6,7,1,5]
                        [2,4,6,7,1,5]
index=4的元素(1)插入----->[2,4,6,1,7,5]
                        [2,4,1,6,7,5]
                        [2,1,4,6,7,5]
                        [1,2,4,6,7,5]
index=5的元素(5)插入----->[1,2,4,6,5,7]
                        [1,2,4,5,6,7]
'''

# 方法一
nums = [6,4,7,2,1,5]
for i in range(1,len(nums)):
    insert_num = nums[i]
    j = i-1
    while j >= 0:
        if nums[j] > insert_num:
            nums[j+1] = nums[j]
            nums[j] = insert_num
        else:
            break
        j -= 1
print(nums)

# 方法二
nums2 = [6,4,7,2,1,5]
for i in range(1,len(nums2)):
    for j in range(i,0,-1):
        if nums2[j-1] > nums2[j]:
            nums2[j-1],nums2[j] = nums2[j],nums2[j-1]
        else:
            break
print(nums2)

'''
功能ok，非常棒，继续加油
'''
