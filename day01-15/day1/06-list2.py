# 和字符串切片一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或将一部分取出来创新出新的列表，

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)  # apple strawberry waxberry

# 可以通过完整切片操作复制列表

# ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits3 = fruits2[:]
fruits4 = fruits[-3:-1]
print(fruits4)  # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)
