"""
面向对象高级编程

使用__slots__
Python 允许在定义 class 的时候，定义一个特殊的__slots__变量，来限制该 class 实例能添加的属性
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
"""
class Student(object):
 __slots__ = ('name', 'age') # 用 tuple 定义允许绑定的属性名称

 """
 使用@property
 
 把一个 getter 方法变成属性，只需要加上@property 就可以了，此时，@property 本身又创建了另一个装饰器@score.setter，
 负责把一个 setter 方法变成属性赋值
 还可以定义只读属性，只定义 getter 方法，不定义 setter 方法就是一个只读属性
 """

 class Student(object):

     @property
     def score(self):
         return self._score

     @score.setter
     def score(self, value):
         if not isinstance(value, int):
             raise ValueError('score must be an integer!')
         if value < 0 or value > 100:
             raise ValueError('score must between 0 ~ 100!')
         self._score = value


     @property
     def level(self):
         if self._score > 90:
            return 'a'
         elif self._score > 80:
             return 'b'
         else:
             return 'c'


 s = Student()
 s.score = 60
 print('s.score =', s.score)
 # ValueError: score must between 0 ~ 100!
 s.score = 9999

 """
 多重继承
 
 让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。这种设计通常称之为 MixIn。
 只允许单一继承的语言（如 Java）不能使用 MixIn 的设计。
 
 __str__()
 
 __repr__()
 
 __iter__
 如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python 的 for
循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环

__getitem__
与之对应的是__setitem__()方法，把对象视作 list 或 dict 来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

__getattr__
当调用不存在的属性时，比如 score，Python 解释器会试图调用__getattr__(self, 'score')来尝试获得属性
链式调用 ????

__call__
Python 中，任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
 """

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s.' % self.name)

print(Student('Michael'))

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[5])
print(f[100])
print(f[0:5])
print(f[:10])


"""
使用枚举类
@unique 装饰器可以帮助我们检查保证没有重复值。
Enum 可以把一组相关常量定义在一个 class 中，且 class 不可变，而且成
员可以直接比较。
"""
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


"""
使用元类
type()
metaclass，直译为元类，简单的解释就是：当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。?????
metaclass 是 Python 面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用 metaclass 的情况，所以，看不懂也没关系，因为基本上你不会用到。
"""

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 指示使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)

"""
ORM 全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作 SQL 语句。
"""
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()


"""
错误、调试和测试
调用堆栈
记录错误
抛出错误
raise 抛出错误
"""
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')
    print('END')

main()
print('END')

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

"""
调试
断言
凡是用 print()来辅助查看的地方，都可以用断言（assert）来替代：

logging
把 print()替换为 logging 是第 3 种方式，和 assert 比，logging 不会抛出错误，而且可以输出到文件

pdb
第 4 种方式是启动 Python 的调试器 pdb，让程序以单步方式运行，可以随时查看运行状态。

pdb.set_trace()
这个方法也是用 pdb，但是不需要单步执行，我们只需要 import pdb，然后，在可能出错的地方放一个 pdb.set_trace()，就可以设置一个断点

IDE
如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的 IDE。目前比较好的 Python IDE 有 PyCharm
"""
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

import pdb
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

"""
单元测试
TDD：Test-Driven Development  测试驱动开发”

setUp 与 tearDown
可以在单元测试中编写两个特殊的 setUp()和 tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
"""
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()

"""
运行单元测试
一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在 mydict_test.py 的最后加上两行代码：
if __name__ == '__main__':
 unittest.main()
 
这样就可以把 mydict_test.py 当做正常的 python 脚本运行：$ python3 mydict_test.py

另一种方法是在命令行通过参数-m unittest 直接运行单元测试：$ python3 -m unittest mydict_test
"""


"""
文档测试（doctest）
"""
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

"""
IO 编程

IO 编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
Input Stream 就是数据从外面（磁盘、网络）流进内存，Output Stream 就是数据从内存流到外面去。对于浏览网页来说，
浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。

第一种是 CPU 等着，也就是程序暂停执行后续代码，等 100M 的数据在 10 秒后写入磁盘，再接着往下执行，这种模式称为同步 IO；
另一种方法是 CPU 不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称
为异步 IO。

回调模式,轮询模式

with 语句
"""
from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

"""
StringIO 和 BytesIO
StringIO 顾名思义就是在内存中读写 str
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
"""
from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())


"""
操作文件和目录

Python 的 os 模块封装了操作系统的目录和文件操作，要注意这些函数有的在 os 模块中，有的在 os.path 模块中。
"""
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))



"""
序列化
我们把变量从内存中变成可存储或传输的过程称之为序列化，在 Python中叫 pickling，
在其他语言中也被称之为 serialization，marshalling，flattening 等等，都是一个意思。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即 unpickling。

JSON
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如 XML，但更好的方法是序列化为 JSON，
因为 JSON 表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON 不仅是标准格式，并且比 XML 更快，而且可以直接在 Web 页面中读取，非常方便。

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合 Web 标准，就可以使用 json 模块。
json 模块的 dumps()和 loads()函数是定义得非常好的接口的典范。
"""
import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)




import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)







































































































































































































































