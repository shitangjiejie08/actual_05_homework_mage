#encoding:utf-8
nums=[6,11,7,9,4,2,1]
n=len(nums)
for i in list(range(n)):
    for j in list(range(i,n)):
        if nums[i]>nums[j]:
            c=nums[j]
            nums[j]=nums[i]
            nums[i]=c
print(nums)

'''
功能ok, 继续加油
'''


#enconding:utf-8

print(max(nums))
print(min(nums))

a=max(nums)
b=min(nums)
end=n-1
star=0
q=input('please write a number ')
q=int(q)
while True:
    middle = (end + star) // 2
    if q<nums[middle]:
        end=middle-1
        middle=(star+middle)//2
    elif q>nums[middle]:
        star=middle+1
        middle=(end+middle)//2
    else :
        print(middle)
        break
    if star>end:
        print('no this')
        break

'''
功能ok，继续加油
改进，找下代码中的无意义的代码并删除
'''
