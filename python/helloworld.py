#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this a test


"""
list  : classmates = ['Michael', 'Bob', 'Tracy']
tuple : classmates = ('Michael', 'Bob', 'Tracy')  元组  不可变
dict  : classmates = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  字典 key必须是不可变对象
set   : s = set([1, 2, 3])
"""

classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Adam')
classmates.insert(1, 'Jack')
classmates.pop()
classmates.pop(1)

'''
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改.因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple,
只有1个元素的tuple定义时必须加一个逗号，来消除歧义.list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
t = (1,)
'''
classmates = ('Michael', 'Bob', 'Tracy')

for name in classmates:
	print(name)

#条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。
age = 3
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')


'''
dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Thomas' in d
二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

和list比较，dict有以下几个特点：
1. 查找和插入的速度极快，不会随着key的增加而增加；
2. 需要占用大量的内存，内存浪费多。
而list相反：
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
if('Thomas' in d):
	print('exist')
else:
	print('no exist')

print(d.get('Thomas'))
print(d.get('Thomas', -1)) #不存在则输出-1，默认输出none
print(d['Michael'])
d.pop('Bob')
print(d)

"""
set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果
"""
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1,2,3,4])
s2 = set([3,4,5,6])

print(s1 & s2)
print(s1 | s2)

# s3 = set((4,5,[2, 3]))


'''
定义函数
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
数据类型检查可以用内置函数isinstance()实现：
'''
import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

print(move(10,12,2,30))

def nop():
	pass

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('ban operand type')
	if x>=0:
		return x
	else:
		return -x

print(my_abs(-10))


def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print(calc((1,2,3)))

"""
可变参数
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
如果已经有一个list或者tuple，要调用一个可变参数怎么办？前面加一个*号，把list或tuple的元素变成可变参数传进去,
"""
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print(calc(1,2,3))

list = [1,2,3]
print(calc(*list))

"""
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
"""
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('awei',30,city='Shenzhen',job='Engineer')
dict = {'身高':'171cm','体重':'63kg'}
person('awei',30,**dict)

"""
命名关键字参数
要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
"""
def person(name,age,*,city,job):
	print(name,age,city,job)

person('awei',30,city='leiyang',job='phper')

"""
参数组合
请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict
"""
def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None,ext2='cc')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
f2(*args, **kw)

"""
解决递归调用栈溢出的方法是通过尾递归优化
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
"""
def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)

def fact2(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print(fact(10))

"""
切片

"""
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack','Plus','Windy']
print(L[0:2])
print(L[:3])
print(L[-2:-1])
print(L[-1:])
print(L[0:6:2])#前6个，每两个取一个

"""
迭代
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
"""
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,v)

for ch in "abc":
	print(ch)

"""
如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
"""
from collections import Iterable
print(isinstance("abc",Iterable))
print(isinstance(['a','b','c'],Iterable))
print(isinstance(('a','b','c'),Iterable))
print(isinstance({'1':'a','2':'b'},Iterable))
print(isinstance(123,Iterable))

"""
如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素
"""
for i,val in enumerate(['A','B','C']):
	print(i,val)

for x,y in ([1,2],[2,4],[4,16]):
	print(x,y)

"""
列表生成式即List Comprehensions，
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？：
"""
L = []
for x in range(1, 11):
	L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])


sum = 0
for x in range(101):
	sum = sum + x
print(sum)

L = ['hello','world',18,'apple']

for s in L:
	if(isinstance(s,str)):
		print(s.upper())
'''
生成器   generator
'''
def fib(max):
	n,a,b=0,0,1
	while n < max:
		print(b)
		n,a,b=n+1,b,a+b
	return 'done'

#fib(6)

"""
上面的函数和 generator 仅一步之遥。要把 fib 函数变成
generator,只需要把 print(b)改为 yield b 就可以了.
如果一个函数定义中包含 yield 关
键字,那么这个函数就不再是一个普通函数,而是一个 generator:
"""
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		n,a,b=n+1,b,a+b
	return 'done'

o = fib(6)
print(next(o))
print(next(o))


"""
调用 generator 时,发现拿不到 generator 的 return 语句 的返回值。如果想要拿到返回值,必须捕获 StopIteration 错误,返回值 
包含在 StopIteration 的 value 中:
请注意区分普通函数和 generator 函数,普通函数调用直接返回结果:
generator 函数的“调用”实际返回一个 generator 对象:
"""
while True:
	try:
		print(next(o))
	except StopIteration as e:
		print('Generator return value',e.value)
		break


n= 0
for t in triangles():
	print(t)
	n =n + 1
	if(n == 10):
		break


"""
迭代器
可以被 next()函数调用并不断返回下一个值的对象称为迭代器: Iterator。

凡是可作用于 for 循环的对象都是 Iterable 类型;
凡是可作用于 next()函数的对象都是 Iterator 类型,它们表示一个惰性 计算的序列;
集合数据类型如 list、dict、str 等是 Iterable 但不是 Iterator,不过可 以通过 iter()函数获得一个 Iterator 对象。
"""
isinstance([],Iterator)
isinstance(Iter([]),Iterator)

"""
函数式编程

函数式编程的一个特点就是,允许把函数本身作为参数传入另一个函
数,还允许返回一个函数!
"""

"""
高阶函数
一个函数就可以 接收另一个函数作为参数，这种函数就称之为高阶函数
"""
def add(x, y, f):
    return f(x) + f(y)

"""
map/reduce
map()函数接收两个参数，一个是函数，一个是 Iterable， map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回。
reduce 把一个函数作用在一个序列[x1, x2, x3, ...] 上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元 素做累积计算，其效果就是:
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""

"""
filter
filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还 是 False 决定保留还是丢弃该元素。
"""
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

"""
sorted
sorted()函数也是一个高阶函数，它还可以接收一个 key 函数来 实现自定义的排序，例如按绝对值大小排序:
"""
sorted([36, 5, -12, 9, -21], key=abs)
#[5, 9, -12, -21, 36]

"""
返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
在这个例子中，我们在函数 lazy_sum 中又定义了函数 sum，并且，内部 函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 返 回函数 sum 时，相关参数和变量都保存在返回的函数中，
这种称为“闭包 (Closure)”的程序结构拥有极大的威力。
"""
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
return sum

"""
闭包
注意到返回的函数在其定义内部引用了局部变量 args，所以，当一个函 数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包 用起来简单，实现起来可不容易。
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后
续会发生变化的变量。
"""
def count():
	def f(j):
		def g():
			retun j*j
		 return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1,f2,f3 = count()
f1()
f2()
f3()

"""
匿名函数
关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写 return，返回值就是该表达式的结果.
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
"""
f = lambda x:x*x
f(6)

"""
装饰器(decorator)
"""
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper

@log  #把@log 放到 now()函数的定义处，相当于执行了语句：now = log(now)
def now():
	print('2017-12-26')


"""
偏函数
简单总结 functools.partial 的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""
def int2(x,base=2):
	return int(x,base)

int2('1010101')

import functools
int3 = functools.partial(int,base=2)
int3('1010101')


"""
模块、包
在 Python 中，一个.py 文件就称之为一个模块（Module）
每一个包目录下面都会有一个__init__.py 的文件，这个文件是必须存在的，否则，Python 就把这个目录当成普通目录，而不是一个包。
"""

"""
安装第三方库

一般来说，第三方库都会在 Python 官方的 pypi.python.org 网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者 pypi 上
搜索，比如 Pillow 的名称叫 Pillow，因此，安装 Pillow 的命令就是：pip install Pillow
"""
import sys
print(sys.path)

"""
OOP
类和实例
封装
"""
class student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

	def print_score(self):
		print('%s,%s'%(self.name,self.score))

"""
注意到__init__方法的第一个参数永远是 self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到 self，因为 self
就指向创建的实例本身。有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但 self 不需要传，
Python 解释器自己会把实例变量传进去：
"""

"""
访问限制
在 Python 中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问,Python 本身没有任何机制阻止你干坏事，一切全靠自觉。
"""
class student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print('%s,%s'%(self.__name,self.__score))



"""
继承和多态
静态语言 vs 动态语言
"""
class Animal(Object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	pass

class Cat(Animal):
	pass

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()

print('d is Cat?', isinstance(dog, Cat))

run_twice(c)

"""
获取对象信息
使用 type()

使用 isinstance()
对于 class 的继承关系来说，使用 type()就很不方便。我们要判断 class的类型，可以使用 isinstance()函数。

使用 dir()
如果要获得一个对象的所有属性和方法，可以使用 dir()函数，它返回一个包含字符串的 list
"""
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())

"""
在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是
当你删除实例属性后，再使用相同的名称，访问到的将是类属性
"""
"""test"""














