#encoding: utf-8

i = 0
j = 0

for i in range(1,10):
    for j in range(1,i + 1):
        print("%d*%d=%d" % (i,j, i * j), end='\t')
    print('\t')


'''
功能ok，继续加油
1. 可以尝试去掉line3, 4看看有什么变化
2. 尝试打印上三角
'''
