#!/user/bin/python3.5
#encoding: utf-8
#二分查找

NUMS = [5,13,19,21,37,56,64,75,80,88,92]
KEY = 21

LOW = 0
HIGH = len(NUMS) - 1

while LOW <= HIGH:
	MID = (LOW + HIGH) // 2
	MID_VAL = NUMS[MID]

	if MID_VAL > KEY:
		HIGH = MID - 1
	elif MID_VAL < KEY:
		LOW = MID + 1
	else:
		print('Yes,the key is {0}.The index is {1}.'.format(KEY,MID))
		break

'''
功能ok，坚持，继续加油
'''
