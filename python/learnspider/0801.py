#第八章
#8.3 爬虫的浏览器伪装技术实战
#(1)
import urllib.request
import http.cookiejar
url= "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"
cjar=http.cookiejar.CookieJar()
proxy= urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/www/learn-python/venv/Scripts/spider/08/1.html","wb")
fhandle.write(data)
fhandle.close()
