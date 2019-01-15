# -*- coding: utf-8 -*-
import scrapy
from myFirstSpider.items import MyfirstspiderItem

class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    # 此时虽然还在此定义了start_urls属性，但不起作用，因为在构造方法进行了重写
    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
        'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
    )

    # 重写初始化方法__init__()，并设置参数myurl
    def __init__(self, myurl=None, *args, **kwargs):
        super(WeisuenSpider, self).__init__(*args, **kwargs)
        # 通过split()将传递进来的参数以“|”为切割符进行分隔，分隔后生成一个列表并赋值给myurllist变量
        myurllist = myurl.split("|")
        # 通过for循环遍历该列表myurllist，并分别输出传进来要爬取的各网址
        for i in myurllist:
            print("要爬取的网址为：%s" % i)
        # 将起始网址设置为传进来的参数中各网址组成的列表
        self.start_urls = myurllist

    def parse(self, response):
        item = MyfirstspiderItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题")
        print(item["urlname"])