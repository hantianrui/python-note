#练习1：华氏温度转换为摄氏温度。
#提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
f = float(input('请输入华氏温度:'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
'''
在使用print函数输出时，也可以对字符串内容进行格式化处理，上面print函数中的字
符串%.1f是一个占位符，稍后会由一个float类型的变量值替换掉它。同理，如
果字符串中有%d，后面可以用一个int类型的变量值替换掉它，而%s会被字符串的值
替换掉。除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，其中
{f:.1f}和{c:.1f}可以先看成是{f}和{c}，表示输出时会用变量f和变量c的值替换掉这
两个占位符，后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字。
'''
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

#练习2：输入圆的半径计算计算周长和面积。
radius = float(input('请输入圆的半径：'))
circumference = 2*3.14*radius
area = 3.14*radius**2
print('圆的周长=', circumference, '\n', '\b圆的面积=', area)
'''
参考答案：
radius = float(input('请输入圆的半径: '))
circumference = 2 * 3.14 * radius
area = 3.14 * radius * radius
print('周长: %.2f' % circumference)
print('面积: %.2f' % area)
'''

#练习3：输入年份判断是不是闰年。
year = int(input('输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)
'''
说明：比较运算符会产生布尔值，而逻辑运算符and和or会对这些布尔值进行组合，最终
也是得到一个布尔值，闰年输出True，平年输出False。
'''