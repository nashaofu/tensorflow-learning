for i in range(2):
    a = input('please input a number:')

    b = [a]
    print('b is %s' % (b))
    print(b)

d = {'a': 12, 'b': [1, 2, 3]}

print(d)
a = [d]

print(a)
d['b'][0] = '@@@'
print(a)