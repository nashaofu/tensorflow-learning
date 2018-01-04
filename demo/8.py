from collections import Iterable
from collections import Iterator

a = isinstance('abc', Iterable)  # str是否可迭代
print(a)

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
a = isinstance([], Iterator)
print(a)

a = isinstance(iter('abc'), Iterator)
print(a)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# K可以用下面的语句生成与L相同的列表

L2 = [x * x for x in range(1, 11)]
print(L2)

# 仅生成偶数的平方
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L3)

# 嵌套循环
L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L4)

import os  # 导入os模块，模块的概念后面讲到
dirs = [d for d in os.listdir('.')]
print(dirs)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L5 = [k + '=' + v for k, v in d.items()]
print(L5)

L6 = ['Hello', 'World', 18, 'Apple', None]
L7 = [s.lower() for s in L6 if isinstance(s, str)]
print(L7)
