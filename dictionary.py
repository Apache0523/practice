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