#第八章
#8.3 爬虫的浏览器伪装技术实战
#设置cookie
import urllib.request
import http.cookiejar
cjar=http.cookiejar.CookieJar()
proxy= urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
#建立空列表，为了以指定格式存储头信息
headall=[]
#通过for循环遍历字典，构造出指定格式的headers信息
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
#将指定格式的headers信息添加好
opener.addheaders = headall
#将opener安装为全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/www/learn-python/venv/Scripts/spider/08/2.html","wb")
fhandle.write(data)
fhandle.close()

