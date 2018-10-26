a = ['hello', 'world']
print(list(a))
b = 'hello'
print(list(b))
m = [1, 2, 3]
print(list(m))
c = ('hello', 'world')
print(tuple(c))
d = 'hello'
print(tuple(d)) #list或者tuple一个字符串，得到的都是list或者tuple类型的分隔开的list或者tuple,list或者tuple一个list或者tuple，返回原来的
f = tuple(a) #tuple一个list,将其转换为tuple
print(f)
a = (1, 2, 3, 4)
print(max(a))
print(min(a))