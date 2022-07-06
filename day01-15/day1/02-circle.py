# 输入半径，计算圆的周长和面积
import math
radius = float(input('请输入圆的半径: '))
perimeter = 2 * radius * math.pi
area = radius * radius * math.pi

print(f'周长：{perimeter:.2f}')
print(f'面积：{area:.2f}')
