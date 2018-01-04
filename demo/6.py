def getX(x, y=0):
    print(x, y)
    return x + y


a = int(input('please input a number:'))

print(getX(a))

b = int(input('please input a number as b:'))

print(getX(x=b, y=a))
