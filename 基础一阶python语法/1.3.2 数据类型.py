name='韩天睿'
age=13

print(type(name),type(age))  #name和age的类型不一样
#print('我叫'+name+'今年，'+age+'岁')  #当将str类型和int类型连接时会报错。解决方案：类型转换
print('我叫'+name+'今年，'+str(age)+'岁')  #将int类型通过str()函数转成了str类型

#str()将其他类型转换成str类型
a=16
b=18.343
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

#int()将其他类型转换成int类型
s1='128'
f1=98.7
s2='76.77'
f2=True
sf='hello'
print(type(s1),type(f1),type(s2),type(f2),type(sf))
print(int(s1),type(int(s1)))  #将str类型转换成int类型，字符串必须为数字串
print(int(f1),type(int(f1)))  #float类型转换成int类型只截取整数部分，去尾法去掉所以小数部分
#print(int(s2),type(int(s2)))  #因为它是小数串，所以不能转化成int类型
print(int(f2),type(int(f2)))
#print(int(sf),type(int(sf)))  #将str类型转化成int类型必须是数字串（整数），hello为英文，所以转换不成int类型

#float()将其他类型转换成float类型
d='128.98'
e='76'
f=True
g='hello'
h=98
print(type(d),type(e),type(f),type(g),type(h))
print(float(d),type(float(d)))
print(float(e),type(float(e)))
print(float(f),type(float(f)))
#print(float(g),type(float(g)))  #字符串中的数据如果不是数字串，则不能转换
print(float(h),type(float(h)))