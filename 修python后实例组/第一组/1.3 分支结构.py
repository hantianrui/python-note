#练习1：英制单位英寸与公制单位厘米互换。
value = float(input('输入长度：'))
unit = input('单位：')
if unit == 'in' or '英寸':
    print('%.2f英寸=%.2f厘米' % (value, value*2.54))
elif unit == 'cm' or '厘米':
    print('%.2f厘米=%.2f英寸' % (value, value/2.54))
else:
    print('请输入有效单位')

#练习2：百分制成绩转换为等级制成绩。
'''
要求：如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
'''
point = float(input('输入成绩：'))
if 100>=point>=90:
    grade = 'A'
    print('对应的等级是：', grade)
elif 90>point>=80:
    grade = 'B'
    print('对应的等级是：', grade)
elif 80>=point>70:
    grade = 'C'
    print('对应的等级是：', grade)
elif 70>=point>60:
    grade = 'D'
    print('对应的等级是：', grade)
elif 60>=point>=0:
    grade = 'E'
    print('对应的等级是：', grade)
else:
    print('您输入的成绩有误：')

#练习3：输入三条边长，如果能构成三角形就计算周长和面积。
a = float(input('a边长：'))
b = float(input('b边长：'))
c = float(input('c边长：'))
if a+b>c>a-b or a+b>c>b-a:
    circumference = a+b+c
    p = circumference/2
    area = ((p-a)*(p-b)*(p-c))**0.5
    print('该三角形的周长为%.2f，面积为%.2f' % (circumference, area))
else:
    print('错误')
'''
参考答案：
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
'''