dictionary = {'a': 1, 'b': 2, 'c': 3} #创建字典
print(dictionary['a'])
student = [('name', '小猪'), ('code', 152897)]
detail = dict(student) #用dict方法创建字典
print("信息：", detail)
print('姓名：', detail['name'])
print('学号：', detail['code'])
detailA = dict(name='小智', code='15789') #注意这种方法创建
print('学生信息：', detailA)
print('学号：', detailA['code'])
xulin = dict(name='徐林', number='001', addr='北京市', com='yusys')
print('徐林信息：', xulin)
print('徐林姓名：', xulin['name'])
print('徐林号码：', xulin['number'])
print('徐林地址：', xulin['addr'])
print('徐林公司：', xulin['com'])
xulin['name'] = 'Xulin' #修改字典的value
xulin['age'] = '22' #添加键值对
print('徐林姓名：%s' % xulin['name'])
print('徐林姓名：%(name)s' % xulin) #注意这种输出方法
print('徐林年龄:%(age) s' % xulin)
yangxin = dict(name='YangXin', age=18, code='002')
print("杨鑫信息：", yangxin)
print("杨鑫姓名：%(name)s" % yangxin)
del xulin['number'] #删除key
print('徐林信息：', xulin)
print('徐林信息长度：%d' % len(xulin))
xulin.clear() #和del区别，一个是直接删除字典，一个是删除所有key
print("徐林信息：", xulin)
x = {}
y = x
x['name'] = '123'
m = {}
n = m
m = {'name': 123}
print(n) #注意区别，m重新指向新的内存地址，n指向原来的。x依然指向原来的，所以y也跟着改变
print(y)
x.clear()
print("x执行clear之后的Y：", y)
student = {'姓名': '小智', '五五开': ['开挂', '狒狒', 30]} #浅复制，原地修改复制后的值，原来的值也会改变
teacher = student.copy()
teacher['五五开'].remove('狒狒')
print('五五开是：%(姓名)s' % teacher)
print(student)
print(teacher)

