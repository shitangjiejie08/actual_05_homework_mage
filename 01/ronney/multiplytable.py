#!encoding:utf-8
# 1.行数i<=9
# 2.每行依次打印，行号*遍历行号列表
# 3.如何同一行打印输出

i = 1
while (i <= 9): #循环，行数为9行
    j = 1
    while j <= i: #每行输出的个数
        x = 0
        x = i * j
        print(i,"x",j,"=",x,"\t",end="")  #end=“”使同一行打印输出
        j += 1
    print("\n")   #换行，同一行的元素输出完后换行
    i += 1

'''
功能ok，继续加油
1. while, if, elif 后的条件表达式可以不使用()
2. 编辑器修改为tab键用4个空格替换，禁止tab和空格混用
3. 考虑如何去除空行
4. 可以尝试打印上三角
'''
