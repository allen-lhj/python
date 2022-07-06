# 输入一个数，判断是不是素数
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))

is_prime = True
# 只能被1和自身整除
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num:d} 是素数')
else:
    print(f'{num:d} 不是素数')
