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
