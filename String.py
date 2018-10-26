print('study %s boring' % 'is')   #格式化字符串
print('圆周率是：%.2f' % 3.14)
print('12%')
print('%d%%' % 12)
print(('今年是%d年，中国女排夺得本届奥运会%s,共获得%d枚金牌)' % (2018, '冠军', 56)))
print('圆周率是:%10f' % 3.1415926)
print('圆周率是:%010.2f' % 3.14159)
print('圆周率是:%-10.2f' % 3.14159) #-号用于左对齐
print(('对齐正负数：%5d' % 10) + '\n' + ('对齐正负数：%5d' % -10))
print(('正负数都表示符号：%+5d' % 10) + '\n' + ('正负数都表示符号：%+5d' % -10)) #+号格式化字符串表示正负数都加符号
string = 'YangXin is a Sb'
print(string.find('YangXin'))
print(string.find('ang', 0, 2)) #输出-1表示没找到
dirs = ('home', 'data', 'clearlove')
print('/'.join(dirs))
data = ['2018', '10', '24'] #join的必须是字符串之间，不然会报错
print('-'.join(data))
result = 'XULIN IS A SB'
resultL = result.lower()
print(resultL)
resultH = resultL.upper()
print(resultH)
print(result.find('xulin'))
print(result.lower().find('Xulin'))
print(result.lower().find('Xulin'.lower())) #检索字符和查找对象都转换为小写，不区分大小写的实现
print(result.upper().find('Xulin'.upper()))
newString = 'YangXin is a Sb'
print(newString.swapcase()) #交换大小写，原字符串值均不改变
print(newString.replace('YangXin', 'Xulin', 1)) #替换，原字符，替换后字符，替换次数
print(newString.split()) #不写参数，默认按空格分隔，分割结果为list列表
print(newString.split('a', newString.count('a')))
print((newString.strip('Y')) + '\n' + (newString.strip('b')))

intab = 'ilkerog'
outtab = '1234567'
trantab = str.maketrans(intab, outtab) #注意函数里输入和输出的位置，不能反。
st = 'i like rock and roll'
print(st.translate(trantab))
iq = (132-100)/100
print('智商提升了：%d%%' % 32)