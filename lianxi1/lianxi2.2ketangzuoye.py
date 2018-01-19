#encoding:utf-8
task=[]
while True:
    n = input('plese write a mingling or do')
    if n!='do':
        task.append(n)
    else:
        c=len(task)
        if c==0:
            print('no task')
            break
        else:
            v  = task.pop(0)
            print('the task is',v)


#encoding:utf-8
#number1=input('please write a list',[])
#number2=input('please write a list',[])
num1=[1,2,3,0,6,3,7,8,9]
num2=[1,5,6,7,8,2,3,4]
result=[]
for i in num1:
    if i in num2:
        if i not in result:#shi daima bu chongfu
            result.append(i)
print(result)


#name='wupeng'
print('''i'm{},and i'm{} years old'''.format('wupeng',24))#format qian wei dian


name='wupeng'
print('''i'm{},and i'm{} years old'''.format(name,24))

name='wupeng'
print('''i'm{0},and i'm{1} years old'''.format(name,24))

print('''i'm{name},and i'm{age} years old'''.format(name='wupeng',age=24))

#name:10 name zhan yong 10 ge zifu,mo ren zuo dui qi
print('''i'm{name:10},and i'm{age} years old'''.format(name='wupeng',age=24))
print('''i'm[{name:<10}],and i'm{age} years old'''.format(name='wupeng',age=24))
#you dui qi
print('''i'm[{name:>10}],and i'm{age} years old'''.format(name='wupeng',age=24))
#ju zhong
print('''i'm[{name:^10}],and i'm{age} years old'''.format(name='wupeng',age=24))