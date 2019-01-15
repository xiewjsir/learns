"""
Web 开发

mvc

MVVM优点编辑
MVVM模式和MVC模式一样，主要目的是分离视图（View）和模型（Model），有几大优点
1. 低耦合。视图（View）可以独立于Model变化和修改，一个ViewModel可以绑定到不同的"View"上，当View变化的时候Model可以不变，当Model变化的时候View也可以不变。
2. 可重用性。你可以把一些视图逻辑放在一个ViewModel里面，让很多view重用这段视图逻辑。
3. 独立开发。开发人员可以专注于业务逻辑和数据的开发（ViewModel），设计人员可以专注于页面设计，使用Expression Blend可以很容易设计界面并生成xml代码。
4. 可测试。界面素来是比较难于测试的，而现在测试可以针对ViewModel来写。

目前 HTTP 协议的版本就是 1.1，但是大部分服务器也支持 1.0 版本，主要区别在于 1.1 版本允许多个 HTTP 请求复用一个 TCP连接，以加快传输速度

方法：GET 还是 POST，GET 仅请求资源，POST 会附带用户数据；

响应代码：200 表示成功，3xx 表示重定向，4xx 表示客户端发送的请求有错误，5xx 表示服务器端处理时发生了错误；

World Wide Web，简称 WWW

WSGI 接口：Web Server Gateway Interface。
"""
#hello.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

#do_wsgi
from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()

"""
使用 Web 框架
Flask

除了 Flask，常见的 Python Web 框架还有：
x Django：全能型 Web 框架；
x web.py：一个小巧的 Web 框架；
x Bottle：和 Flask 类似的 Web 框架；
x Tornado：Facebook 的开源异步 Web 框架
"""
#pip install flask
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()


"""
Flask 通过 render_template()函数来实现模板的渲染。和 Web 框架类似，Python 的模板也有很多种。Flask 默认支持的模板是 jinja2，
在 Jinja2 模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在 Jinja2 中，用{% ... %}表示
指令。
比如循环输出页码：
{% for i in page_list %}
 <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}


除了 Jinja2，常见的模板还有：
x Mako：用<% ... %>和${xxx}的一个模板；
x Cheetah：也是用<% ... %>和${xxx}的一个模板；
x Django：Django 是一站式框架，内置一个用{% ... %}和{{ xxx }}
的模板。
"""
#pip install jinja2

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

"""
异步 IO
可以想象如果按普通顺序写出的代码实际上是没法完成异步 IO 的：
do_some_code()
f = open('/path/to/file', 'r')
r = f.read() # <== 线程停在此处等待 IO 操作结果
# IO 操作完成后线程才能继续执行:
do_some_code(r)
所以，同步 IO 模型的代码是无法实现异步 IO 模型的。
异步 IO 模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：
loop = get_event_loop()
while True:
 event = loop.get_event()
 process_event(event)

栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。这一端被称为栈顶，相对地，把另一端称为栈底。
向一个栈插入新元素又称作进栈、入栈或压栈，它是把新元素放到栈顶元素的上面，使之成为新的栈顶元素；从一个栈删除元素又称作出栈或退栈，
它是把栈顶元素删除掉，使其相邻的元素成为新的栈顶元素。

协程
在学习异步 IO 模型前，我们先来了解协程。协程，又称微线程，纤程。英文名 Coroutine。

协程最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，
线程数量越多，协程的性能优势就越明显。第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。因为协程是一个线程执行，那怎么利用多核 CPU 呢？
最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。Python 对协程的支持是通过 generator 实现的。

子程序就是协程的一种特例。
"""
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


"""
asyncio
asyncio 是 Python 3.4 版本引入的标准库，直接内置了对异步 IO 的支持。asyncio 的编程模型就是一个消息循环。我们从 asyncio 模块中
直接获取一个 EventLoop 的引用，然后把需要执行的协程扔到 EventLoop 中执行，就实现了异步 IO。
"""
#1 sync_hello
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


#2 sync_wget
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
async/await
用 asyncio ᨀ供的@asyncio.coroutine 可以把一个 generator 标记为coroutine 类型，然后在 coroutine 内部用 yield from 调用另一个 coroutine实现异步操作。
为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和 await，可以让 coroutine 的代码更简洁易读。

请注意，async 和 await 是针对 coroutine 的新语法，要使用新的语法，只需要做两步简单的替换：
1. 把@asyncio.coroutine 替换为 async；
2. 把 yield from 替换为 await。
"""
#sync_hello2
import threading
import asyncio

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



"""
aiohttp
asyncio 可以实现单线程并发 IO 操作。如果仅用在客户端，发挥的威力不大。如果把 asyncio 用在服务器端，例如 Web 服务器，由于 HTTP 连
接就是 IO 操作，因此可以用单线程+coroutine 实现多用户的高并发支持。

asyncio 实现了 TCP、UDP、SSL 等协议，aiohttp 则是基于 asyncio 实现的 HTTP 框架。
"""
#pip install aiohttp
__author__ = 'Michael Liao'

'''
async web application.
'''

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

"""
搭建开发环境

python3 --version  查看python版本

异步框架 aiohttp：
pip3 install aiohttp

前端模板引擎 jinja2：
pip3 install jinja2

MySQL 的 Python 异步驱动程序 aiomysql：
pip3 install aiomysql
"""
















































































































































































































































































































































































































