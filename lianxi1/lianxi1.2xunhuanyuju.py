#conding=utf-8
i=1
s=0
while i<=100:
    s=s+i
    i=i+1
print('s=',s)


num=input('please write anumber,or you can write exit')
i=0
s=0
while num != 'exit':
    print(type(num))
    i +=1
    s += int(num)
    num=input('please write another number,or wite exit')
    #int(s)
    #int(i)
if i==0:
    print('s=',0 , 's/i=',0)
else :
    print('pingjushu=',s/i,'s=',s)


#for    yongfa
user=['wp','fjn','bab']
print(user[0],user[1])
for user in user:
    print(user)


