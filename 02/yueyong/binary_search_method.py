#encoding: utf-8

'''
二分查找法：
在一段数字内，找到中间值，判断要找的值和中间值大小比较，
如果中间值大一些，则在中间值的左侧区域继续按照上述的方式查找；
如果中间值小一些，则在中间值的右侧区域继续按照上述方式查找；
直到找到所要找的数字。
1.首先有一个有序的序列（从小到大）中查找一个元素，需要每次将查找的元素和索引中间的元素进行比较
2.查找 == 中间，找到了
3.查找 > 中间，在右半部分
4.查找 < 中间，在左半部分
'''
nums = [2, 3, 5, 7, 8, 11, 14, 16, 19, 30, 42]
start = 0
end = len(nums)-1
find_num = int(input('please input a num:'))

while True:
    midd = (start + end) //2
    if find_num == nums[midd]:
        print('找到了，索引位置为：',midd)
        break
    elif find_num > nums[midd]:
        start = midd + 1
        print('在后半部分')
    else:
        end = midd -1
        print('在前半部分')
    if start > end:
        print('找不到，你要找的数字不在序列中')
        break

'''
功能ok，继续加油
'''
