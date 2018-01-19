#encoding:utf-8


'''
二分查找
Author:daikai
'''
nums = [2,1,5,3,7,6,9,13,10,15]
nums.sort()
print(nums)
start_index = 0
end_index = len(nums) - 1
find_num = int(input("请输入需要查找的数字:"))

while True:
    middle_index = (start_index + end_index)//2
    if find_num == nums[middle_index]:
        print("你需要查找的数字{}已找到！".format(find_num))
        break
    elif find_num > nums[middle_index]:
        start_index = middle_index + 1
    else:
        end_index = middle_index - 1

    if start_index > end_index:
        print("未找到你需要查找的数字")
        break

'''
功能ok，继续加油
'''
