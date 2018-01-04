# 创建generator
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
print(next(g))
for k in g:
    print(k)

# 斐波拉契数列
def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


print(fibonacci(6))

# 斐波拉契数列改为generator
def gfibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = gfibonacci(6)
print(f)
for k in f:
    print(k)
# 获取返回值
while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角

def triangles(n):
    r = 1
    row = [1]
    while r <= n:
        yield row
        r2 = [1]
        for i, value in enumerate(row):
            index = i + 1
            val = value
            if index < len(row):
                val += row[index]
            r2.append(val)
        row = r2
        r += 1

    return 'done'

result = triangles(20)

print(result)

for g in result:
    print(g)