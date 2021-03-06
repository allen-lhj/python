# 将华氏温度转换为摄氏温度
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
"""
在使用`print`函数输出时，也可以对字符串内容进行格式化处理，
上面`print`函数中的字符串`%.1f`是一个占位符，稍后会由一个`float`类型的变量值替换掉它。
同理，如果字符串中有`%d`，后面可以用一个`int`类型的变量值替换掉它，而`%s`会被字符串的值替换掉。
除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，
其中`{f:.1f}`和`{c:.1f}`可以先看成是`{f}`和`{c}`，
表示输出时会用变量`f`和变量`c`的值替换掉这两个占位符，后面的`:.1f`表示这是一个浮点数，小数点后保留1位有效数字。
"""
