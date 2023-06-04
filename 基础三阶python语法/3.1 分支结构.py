'''
if 条件：
    结果
elif 条件：
    结果
else:
    结果
'''
#例如
username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')


"""
实例1：
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
x = float(input('输入x值：'))
if x>1:
    y = 3*x - 5
elif -1<=x<=1:
    y = x + 2
else:
    y = 5*x + 3
print('f(%.2f)=%.2f' % (x, y))
'or'
x = float(input('输入x值：'))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
