# -*- coding: utf-8 -*-
import scrapy
from mymultispd.items import MymultispdItem

class Myspd1Spider(scrapy.Spider):
    name = 'myspd1'
    start_urls = (
        'https://sz.lianjia.com/ershoufang/',
    )

    def parse(self, response):
        item = MymultispdItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题")
        print(item["urlname"])