#转义字符
print('hello\npython') #\+转义功能首字母  n-->newline
print('hello\tpython') #\t=四个单元格hell为一组，o和三个空白单元格为一组，所以hello与python中有三个空格
print('helloooo\tpython') #hell为一组，oooo为一组。所以helloooo和python之间有\t四个空格
print('hello\rpython') #python将hello覆盖了
print('hello\bpython') #\b=backspace将o退掉了

print('http://www.baidu.com')
print('http:////www.baidu.com')
print('我说：\"大家好\"')

#原字符，不希望字符串中的转义字符起作用，就是使用原字符。就是在字符串之前加r或R
print(r'hello\npython')
print(R'hello\npython')
#print(r'hello\npython\')
#最后一个字符不能是反斜杠，但可以是两个反斜杠
print(r'hello\npython\\')
print(R'hello\npython\\')