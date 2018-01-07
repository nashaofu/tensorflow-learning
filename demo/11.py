class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

url = Chain().status.user.timeline.list
print(url)

# 实现可以使用一些固定的方法
class Api(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(path)
        if path == 'user':
            return lambda user: Api('%s/%s' % (self._path, user))
        return Api('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
    __repr__ = __str__

api = Api().status.user('kk').dd
print(api)

from enum import Enum, unique
# 枚举类型
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

from mypackage import test
# import mypackage as mpkg
a = test.Test('sss')
print(a)
print(a.getTestLength())
a.print()

# 导入相同的模块
import hi as hi
h = hi.Hi()
h.print()

from hi import Hi
h2 = Hi()
print(h2)
h2.print()


# 动态定义类
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))

h3 = Hello()
h3.hello()
print(type(h3))