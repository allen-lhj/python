# ord()函数回获取字符的整数表示
print(ord('A'))
# chr() 函数把编码转换为对应的字符
print(chr(66))

# len() 计算字符串的长度
print(len('abc'))
"""
格式化字符串
%d   整数
%f   浮点数
%s   字符串
%x   16进制整数
"""
print('hello %s, you have $%d' % ('jack', 1000))

# 格式化整数和浮点数还可以指定补0的位数
print('%.2f' % 3.12313)
# *运算符来重复一个字符串的内容
s1 = 'hello ' * 3
print(s1)
s2 = 'world'
# +号拼接字符串
s1 += s2
print(s1)
# in not in判断一个字符串是否包含另一个字符串
print('ll' in s1)
print('wor' not in s1)
# 从字符串中取出指定位置的字符(下标运算)

str2 = 'abc123456'
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[0:3])
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
