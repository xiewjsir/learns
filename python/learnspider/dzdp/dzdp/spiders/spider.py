from scrapy import Spider, Request
import re
from lxml import etree
import json
from urllib.parse import quote
from dzdp.items import StoreItem, StorePictureItem
from copy import deepcopy

class Dzdp_spider(Spider):
    name = 'dzdp'
    allowed_domains = ['dianping.com']
    classifys = {
        'c21151': '购宠',
        # 'c21150': '宠物食品',
        # 'c20692': '宠物店'
    }

    def start_requests(self):
        for classify in list(self.classifys.keys()):
            for i in range(100):
                url = "http://www.dianping.com/shenzhen/ch95/g25147p{}".format(str(i+1))
                yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = etree.HTML(response.text)
        stores = selector.xpath("//div[@class='shop-list J_shop-list shop-all-list']/ul/li")
        for store in stores:
            print(store)
            name = store.xpath(".//div[@class='tit']/a/@title")
            print(name)







