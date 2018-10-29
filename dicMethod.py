#fromkeys()方法
seq = ('name', 'age', 'height')
info = dict.fromkeys(seq)
print(info)
infoDetail = dict.fromkeys(seq,10)
print(infoDetail)
#get(方法)
print('小李身高为：%(name)s' % infoDetail)
print('小李年龄为：%s' % infoDetail.get('age', '不存在'))
#get方法不会获取不存在的key不会报错，默认返回None
#key in dict方法(返回值为boolean)
print("张三" in infoDetail)
#items()返回字典所有元组数组
student = {'张三': 'sb', '李四': 'SB'}
print(student.items())
#keys()返回所有key,以列表形式
print(student.keys())
#setdefault方法，输出key对应的value,若无key不报错
print(student.setdefault('张三'))
print(student['张三'])
print(student.setdefault('王五', 'we'))
#update方法，更新value值或者添加键值对
before = dict(name='小王', age=18, 张三='sb')
now = dict(height='160kg')
before.update(now)
print(before)
future = dict(name='小张')
before.update(future)
print(before)
#values方法，返回字典中所有value，List形式，可以有重复元素（value可以重复）
cus = dict(name='王二', age=19)
print(cus.values())
cust = dict(name=12)
cus.update(cust)
print(cus)
