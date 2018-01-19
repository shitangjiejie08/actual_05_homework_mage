#encoding: utf-8

i = 1
while i < 10:                                        #第 i 行(1 => 9)
    j = 1
    while j < 10:                                    #第 j 列 (1 => 9)
        if i <= j:                                   #控制显示上三角
            print(i, '*', j, '=', i * j, end=' ')    #打印 i * j = r, 每行数据不换行
        j += 1                                       #计算 j + 1列
    i += 1                                           #计算第 i + 1行
    print('')                                        #打印换行

i = 1
while i < 10:                                        #第 i 行(1 => 9)
    j = 1
    while j < 10:                                    #第 j 列 (1 => 9)
        if i >= j:                                   #控制显示上三角
            print(i, '*', j, '=', i * j, end=' ')    #打印 i * j = r, 每行数据不换行
        j += 1                                       #计算 j + 1列
    i += 1                                           #计算第 i + 1行
    print('')                                        #打印换行
