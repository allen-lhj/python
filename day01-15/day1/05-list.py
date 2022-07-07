list1 = [1, 3, 5, 7, 100]
print(list1)

list2 = list1 * 3
print(list2)

print(len(list1))
# 下标(索引)运算
print(list1[0])  # 1
print(list1[4])  # 100
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

# 添加元素

list1.append(200)
list1.insert(1, 400)
# 合并两个表
list1 += [1000, 2000]

# 先通过成员运算符判断元素是否在列表中，如果存在就删除该元素

if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)

# 从指定位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)

# 清空列表元素
list1.clear()
