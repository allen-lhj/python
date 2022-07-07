# 元组是一种与列表类似的容器数据类型，可以用一个变量来存储多个数据，不同之处在于元组的元素不能修改
# 定义元组
t = ('jack', 38, True, '四川成都')
print(t)
# 获取元组中的元素

print(t[0])
# 遍历元组中的值
for member in t:
    print(member)
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('luca', 20, True, 'USA')
# 将元组转换为列表
person = list(t)
# 列表转为元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
