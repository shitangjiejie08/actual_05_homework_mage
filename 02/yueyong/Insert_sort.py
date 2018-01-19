#encoding: utf-8

'''
插入排序：在已经排好的数据序列中插入一个数，从而得到一个新的，个数加一的有序数据，但要求插入后此数据系列任然有序
1.定义一个空list nums存储数据 nums = []
2.while True循环，输入要插入的数字
3.如果插入的是第一个数字，直接放入list中，通过len判断
4.当插入第二个数字时，前两个数字进行比较排序
4.当插入第三个数字时，继续进行比较，大的数字总是靠最右侧
5.当插入第N个数字后，依然保证是有序的
'''
nums = []
while True:
    num = int(input('Please enter the number you want to insert：'))
    if len(nums) == 0:
        nums.append(num)
        print(nums)
    elif num > nums[len(nums)-1]:
        nums.append(num)
        print(nums)
    else:
        nums.append(num)
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if nums[j] > nums[j + 1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        print(nums)



'''
排序使用的是冒泡排序，可以查阅下相关资料查找插入排序的概念
'''
