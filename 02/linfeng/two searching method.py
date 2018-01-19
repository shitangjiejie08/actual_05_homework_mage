#encoding:utf-8

nums_list=[2,5,7,11,13,16,17]
find_num=int(input("请输入一个数字: "))
start_num = 0
end_num = len(nums_list) - 1
while True:
    mid_num = int((end_num + start_num) / 2)
    if find_num==nums_list[mid_num]:
        print('找到了，索引为: ',mid_num)
        break
    elif    find_num > nums_list[mid_num]:
        start_num=mid_num+1
        print('在后半段')
    else :
        print('在前半段')
        end_num=mid_num-1
    if start_num>end_num:
        print('找不到')
        break

'''
功能ok，继续加油
提高点:
1.注意编码风格，比如=, >, <, -, +, 等操作前后只有一个空格， :和else, 条件表达式中间不间隔空格等
2.文件的命名方式使用python变量的命名规范
养成一个好习惯很重要
'''
