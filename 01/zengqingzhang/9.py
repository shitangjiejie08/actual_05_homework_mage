#encoding utf-8
#打印九九乘法表9.py
#aft 于2017.3.22
print('九九乘法表')
a=1
b=1
for a in range(1,10):
        for b in range(1,a+1):
                print(a,'X',b,'=',a*b,'\t',end='')
        print()


'''
功能ok， 继续加油
1. 养成良好编码习惯，缩进使用4个空格，修改编辑器tab键为4个空格替换 
2. 尝试删除line5,6
3. 尝试打印上三角
'''
