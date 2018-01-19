#conding=utf-8

boy=False
girl=True

#print(True*True)
print(int(True))
print(bool('False'))
print('a'<'b')
print('a'<='ab')
print('ad'>'bc')#zifuchuan   cong di yi ge bu xiang deng de kai shi bi jiao    zhi hou bu xiang xia bi jiao

#show=input('mai yi ji bao kan jian xi gua mai yi jin xi gua')
#if show=='kjlxg':      #if hou jia mao hao      liang  ge ==wei deng yu, yi ge wei fu zhi
#    print('mlxg')
#else:                  #else hou you mao hao
#    print('mai yi jin bao zi')

fenshu=input('fs')
fenshu=float(fenshu)
if fenshu>=90:
    print('great')
elif fenshu>=80:
    print('middle')
elif fenshu>=60:
    print('jige')
else:
    print('bujige')

nianfen=input('nianfen')
nianfen=int(nianfen)
if nianfen%4==0 and nianfen%100!=0  or nianfen%400==0:
    print('shiyunnian')

else:
    print('feirunnian')


