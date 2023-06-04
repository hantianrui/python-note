#python中的运算符
print(2+2)  #加法运算
print(2-2)  #减法运算
print(2*2)  #乘法运算
print(2/2)  #除法运算
print(11/2)  #除法运算
print(11//2)  #整除运算
print(11%2)  #取余运算
print(2**2)  #次方运算

print(9//4)  #2
print(-9//-4)  #2

print(-9//4)  #-3
print(9//-4)  #-3  一正一负的整数公式，向下取整

print(-9%4)  #3                              -9-4*(-3)=9-12-->3
print(9%-4)  #-3  公式：余数=被除数-除数*商    9-（-4）*（-3)=9-12-->-3

#赋值运算符    运算顺序从右到左
i=7+5
print(i)
a=b=c=20  #链式运算符
print(a,id(a))
print(b,id(b))
print(c,id(c))
#支持参数赋值
a=20
a+=30  #相当于a=a+30
print(a)
a-=10  #相当于a=a-10
print(a)
a*=2   #相当于a=a*2
print(a)
a/=3   #相当于a=a/3
print(a)
a//=3 #相当于a=a//3
print(a)
a%=3  #相当于a=a%3
print(a)
#解包赋值
a,b,c=34,62,91
print(a,b,c)
#两个变量的值
a,b=10,20
print('交换之前：',a,b)
a,b=b,a
print('交换之后：',a,b)

#比较运算符,运行结果为bool类型
a,b=10,20
print('a>b吗？',a>b) #False
print('a<b吗？',a<b) #True
print('a>=b吗？',a>=b) #False
print('a<=b吗？',a<=b) #True
print('a=b吗？',a==b) #False
print('a!=b吗？',a!=b) #True
'''
在python中，=是赋值运算符；==是比较运算符
一个变量由标识、类型、值
==比较的是标识还是值？  值
比较对象的标识用is
'''
a=10
b=10
print(a==b)  #True  说明他们value相等
print(a is b)  #True  说明他们id相等
#暂没学过
q=[11,22,33,44]
p=[11,22,33,44]
print(q==p)  #value-->True
print(q is p)  #id-->False
print(id(q))
print(id(p))
print(a is not b)  #False-->id不相等
print(q is not p)  #True

#bool运算中的and、or、not
'''
and 运算是与运算，只有所有都为 True，and 运算结果才是 True。
or 运算是或运算，只要其中有一个为 True，or 运算结果就是 True。
not 运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True。
not--1 and--2 or--3
'''
x,y,z = 1,0,0
print(x or y and not z)
#0=False 1=True
#not用法
print(not 0, not 1, not True, not False)
#and用法
print(1 and 2 and 0 and 4 and False)
print(1 and 2 and True and 4 and 6)
print(2 and 5 and True and 7 and True)
#or用法
print(0 or 0 or '' or 8 or 1)
print([] or 0 or '' or None or ())