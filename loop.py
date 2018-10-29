import sys
print('python搜索路径是 %s' % sys.path)
#from import 语句
from math import pi
print(pi)
import math
print(math.sin(1))
#导包取别名
import math as m
print(m.pi)
#逗号输出
a = 'hello everybody大家好!'
b = '我是帅气的卢本伟,'
c = '退役战神55开。'
print(a, b, c)
#同时赋值多个变量
a, b, c = 1, 'hehe', 2
print(a, b, c)
#快速交换
x, y = 1, 2
print('x=', x, '\n' "y=", y)
y, x = x, y
print('x=', x, '\n' "y=", y)
#序列解包
num = (1, 2, 3)
m, n, o = num
print(m)
student = {'name': '小李', 'age': 18}
name, age = student.popitem()
print(name, age)
#链式赋值
x = y = z = 10
print(y)
#增量赋值
w = 9
w += 1
print(w)
field = 'hello'
field += ' world'
print(field)