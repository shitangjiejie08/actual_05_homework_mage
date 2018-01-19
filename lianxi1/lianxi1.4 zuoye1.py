#enconding:utf-8
hang=0
while hang< 9:
    hang+=1
    lie = 1
    print('')
    while lie<=hang:
        print(lie ,'*' ,hang ,'=' ,hang*lie,end='\t')
        lie += 1
print('')



for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print(j,'*',i,'=',i*j,end='\t')
    print()


for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')
    print()




        
#encoding:utf-8
#hang=1
#while hang<=9:
 #   lie=hang
  #  while lie<=9:
   #     print(lie ,'*' ,hang ,'=' ,hang*lie,end='\t')
    #    lie+=1
    #hang+=1
    #print('')




#encoging:utf-8
import random
c=random.randint(0,100)
maxguss=5
guss=1
while True:
    n = input('please input a number you guss')
    n = int(n)
    if n==c:
        print('you are right')
        break
    elif n>c:
        print('too big')
    else:
        print('too small')
    if guss>=maxguss:
        print('game over,the rught answer is ',c)
        break
    print('you have only', maxguss-guss,'chance')
    guss+=1






