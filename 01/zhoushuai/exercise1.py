# encoding : utf-8

left = 1
right = 1
max_num = 9
while right <= max_num:
    while left <= right:
        print(left, '*', right, '=', left*right, '\t', end='')
        if left == right:
            print('')
        left += 1
    left = 1
    right += 1

'''
功能ok， 继续加油
1. 考虑打印上三角
'''
