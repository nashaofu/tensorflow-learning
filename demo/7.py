# 累加
def fact(val=None):
    if (val != None):
        def f(v=None):
            if (v != None):
                return fact(val + v)
            else:
                return val
        return f

    return val


a = fact(1)(2)(3)
print(a)
print(a())
print(a(4))
print(a(4)())

l = list(range(101))
r = fact
for i in l[:100]:
    r = r(i)

print('r should is function %s' % r)
print(r())

tup = (1, 2, 3, 4)

k = fact
for i in tup[0:2]:
    k = k(i)

print('k() is %s' % k())