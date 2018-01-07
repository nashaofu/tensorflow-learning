class Class1(object):
    def __init__(self, name):
        self.name = name
        self.ddd = 1212121212
        self.kkkk = '00000'
    def run (self):
        print('Class1 run')

a = Class1('1111')
print(a.name)

class Class2(object):
    def __init__(self, name):
        self.__name = name # 私有属性
        self.kkkk = 12
    def run (self):
        print('Class2 run')
    def printClass2 (self):
        print(self.kkkk)
    
b = Class2('2222')
print(b._Class2__name)
b.__name = 12121 # 没有修改__name，只是添加了一个属性
print(b.__name) 
print(b._Class2__name)
b.run()

# 继承多个类,并且如果多个类都有相同的方法就会继承第一个的
# 属性只继承第一个类的，其他的类的属性不会被继承
class Class3(Class1, Class2):
    def print(self):
        print(self.ddd)
        print(self.kkkk)

c = Class3('121212')
c.run() # print Class1 run

print(c.name)
# c.print()
c.printClass2()

# 类属性
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

s = Student('name')
print(s.count, Student.count)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

print('迭代打印数据')
for n in Fib():
     print(n)