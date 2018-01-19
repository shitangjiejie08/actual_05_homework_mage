number=[2,8,9,3,6]
zuida=number[0]
i=0
while i<4:
    i+=1
    if zuida < number[i]:
        zuida=number[i]
else:
    print(zuida)



number=[0,1,1,2,9,8,5]
zuida=None
for i in number:
    if zuida is None or zuida <i:
        zuida=i
print(zuida)



number=[0,1,1,2,9,8,5]
n=len(number)
for j in range(n-1):
    for i in range(len(number)-1):
            if number[i]>number[i+1]:
                c=number[i]
                number[i]=number[i+1]
                number[i+1]=c
print(number)




a,b,c=1,2,3
print(a,b,c)
a,b=b,a
print(a,b)

m=(0,1,2,9,8,5)
print(max(m))
print(min(m))


num=[0,1,2,9,8,5]
print(max(num))
print(min(num))
