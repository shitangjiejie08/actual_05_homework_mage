#enconding: utf-8
print('1',end='')
print('2',end='')
print('3')

print(type(print(1)))

import random
c = random.randint(0,100)
print(type(c))
#print(c)
n=input('please write a namber')
print(type(n))
i=1
if int(n)==c:
    print('you are right')


while int(n)!=c:
    i+=1
    if i==6:
        break
    if int(n) == c:
        print('you are right')
    if int(n)>c:
        print('too big')
        n=input('n=')
    else:
        print('too small')
        n = input('n=')
if int(n)==c:
    print('you are right')
else:
    print('sorry',c)










print('1',end='')
print('2',end='')
print('3')


num=[1,2,3,4,5,6,7,8,9]
print(type(num[0]))
i=0
while i <= 8:
    j=i
    i+=1
    s=i*num[j]
    print(i,end='')
    print('*',num[j],end='')
    print('=',s)
    while j <= 7:
        j+=1
        s=i*num[j]
        print(i, end='')
        print('*', num[j], end='')
        print('=', s)



