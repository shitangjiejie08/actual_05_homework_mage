#encoding: utf-8
def insert_sort(arg_list):
    for i in range(1,len(arg_list)):
        for j in range(i-1,-1,-1):
            if arg_list[i] < arg_list[j]:
                tmp=arg_list[i]
                arg_list[i]=arg_list[j]
                j-=1
                while j >= 0 and tmp < arg_list[j]:
                    arg_list[j+1]=arg_list[j]
                    j-=1
                arg_list[j+1]=tmp
    return


var_list=[20,397,1,2,71,22,6,9,100,200,6]

insert_sort(var_list)
print(var_list)

'''
功能ok，非常棒，加油
'''
