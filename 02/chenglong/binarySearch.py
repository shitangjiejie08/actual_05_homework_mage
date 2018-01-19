# encoding: utf-8
'''
二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好；其缺点是要求待查表为有序表，且插入删除困难。
因此，折半查找方法适用于不经常变动而查找频繁的有序列表。
首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；
否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
'''




l = list(range(16))
num = 3


def binarySearch(lists, select):
    is_found = False
    if lists != []:
        mid_id = int(len(lists) / 2)    ######中间数下标
        mid_value = lists[mid_id]  # 列表中间的数
        lt_list= lists[0:mid_id]   ###比找的数小的list
        gt_list = lists[mid_id + 1:]  ###比找的数大的list

        if mid_value == select:  # 如果正好是中间的数，返回
            return True
        elif select < mid_value:  # 如果要查找的数小于中间的数
            is_found = binarySearch(lt_list, select)  # 去左边的列表继续查找
            if not is_found:  # 如果没有找到，就去右边的列表查找
                return binarySearch(lt_list, select)
            return True  # 如果找到了，返回True
        elif mid_value < select:  # 如果要查找的大于中间的数
            is_found = binarySearch(lt_list, select)  # 如右边的列表查找
            if not is_found:  # 如果没有找到，就去左侧的列表查找
                return binarySearch(gt_list, select)
            return True
    else:
        return False


a = binarySearch(l, num)
if a:
    print("%s is found in list" % num)
    print(l)
else:
    print("%s is found in list" % num)
    print(l)

'''
功能ok，使用了函数的递归，继续加油
但是需要优化代码，考虑
看看29行代码和30行代码怎么一样呢
line34行返回的是否永远都是false

'''
