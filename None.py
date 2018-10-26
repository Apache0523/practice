a = list('hello')
print(a)
# 在a后面加上新的list
a[len(a):] = list('-world')
print(a)
m = a.index('o')
a = a.insert(2, '1')
print(m)
print(a)