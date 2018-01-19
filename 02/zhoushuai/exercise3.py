# encoding: utf-8

'''
1. 循环获取用户的输入的数字
2. 输出用户的输入
3. 执行排序
4. 输入排序之后的数据
'''

print('输入你想排序(自小到大)的数字，每次一个，\'end\'表示结束')

nums = []
while True:
    input_str = input('第' + str(len(nums)+1) + '个数据： ')
    if input_str == 'end':
        break
    input_num = int(input_str)
    nums.append(input_num)

print('你输入的数值列表是' + str(nums))

sorted_nums = []

# 使用两个list
# for num in nums:
#     if len(sorted_nums) < 1:
#         sorted_nums.append(num)
#     else:
#         for index in list(range(len(sorted_nums))):
#             tmp = sorted_nums[index]
#             if tmp > num:
#                 sorted_nums.insert(index, num)
#                 break
#             if index == len(sorted_nums)-1:
#                 sorted_nums.append(num)

# 使用一个list
if len(nums) > 1:
    unsorted_index = 1
    while unsorted_index <= len(nums)-1:
        for index in list(range(unsorted_index)):
            if nums[index] > nums[unsorted_index]:
                nums.insert(index, nums.pop(unsorted_index))
        unsorted_index += 1

sorted_nums = nums

'''
功能ok，继续加油
'''

print('排序后的结果：' + str(sorted_nums))
print('输入你想找的数字, 输入 exit 结束程序')

while True:
    looking_for = input('你想找的数字: ')
    if looking_for == 'exit':
        break
    looking_for_num = int(looking_for)
    before_index = 0
    mid_index = 0
    after_index = len(sorted_nums)-1

    while before_index <= after_index:
        mid_index = (before_index + after_index) // 2
        if looking_for_num < sorted_nums[mid_index]:
            after_index = mid_index - 1
        elif sorted_nums[mid_index] < looking_for_num:
            before_index = mid_index + 1
        elif sorted_nums[mid_index] == looking_for_num:
            mid_index += 1
            break

    if mid_index != 0:
        print('所寻找的数字为第' + str(mid_index) + '个')
    else:
        print('未寻找到你想要的数字')

print('程序结束')

'''
功能ok， 非常棒，继续加油，坚持啊
'''
