#整数类型
#可以表示：正数、负数、0
n1=98
n2=-148
n3=0
print(n1)
print(n2)
print(n3)

n1=98
n2=-148
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数可以表达为二进制、八进制、十进制、十六进制
print('二进制',0b010111101)    #二进制以0b开头
print('八进制',0o1635)    #八进制以0o开头
print('十进制',174)    #计算机默认进制
print('十六进制',0x2848ECD)    #十六进制以0x开头

#浮点类型
a=3.14159265358979323846
print(a,type(a))

print(1.1+2.2)
#或
n4=1.1
n5=2.2
n6=2.1
print(n4+n5)
print(n4+n6)
#优化
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
#布尔值可以转成整数计算
print(f1+1)  #2 所以True转化成整数为1
print(f2+1)  #1 所以False转化成整数为0
'''
电脑中True为真输出为1，False为假，所以输出为0.
在运算中True电脑会转化为1，False转化为0
'''

#字符串类型(单引号和双引号只能在一行中实现，但三引号可以分为几行）
str1='少即是多'
str2="少即是多"
str3='''少即是多'''
str4="""少即是多"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))