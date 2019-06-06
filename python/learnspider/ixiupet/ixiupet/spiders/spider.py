from scrapy import Spider, Request
import re
from lxml import etree
import json
from urllib.parse import quote
from ixiupet.items import StoreItem, StorePictureItem
from copy import deepcopy

class Ixiupet_spider(Spider):
    name = 'ixiupet'
    allowed_domains = ['meituan.com']
    classifys = {
        'c21151': '购宠',
        # 'c21150': '宠物食品',
        # 'c20692': '宠物店'
    }

    def start_requests(self):
        for classify in list(self.classifys.keys()):
            for i in range(1):
                url = "https://sz.meituan.com/chongwu/{}/pn{}/".format(classify, str(i + 1))
                yield Request(url=url, callback=self.parse, meta={'classify': classify})

    def parse(self, response):
        selector = etree.HTML(response.text)
        stores = selector.xpath("//div[@class='common-list-main']/div[@class='abstract-item clearfix']")
        for store in stores:
            item = StoreItem()
            url = store.xpath(".//a[@class='item-title']/@href")[0][2:-1].replace("www.","sz.")
            item['classify'] = self.classifys.get(response.meta['classify'])
            item['name'] = store.xpath(".//a[@class='item-title']/text()")[0].encode('utf-8')
            item['score'] = store.xpath(".//div[@class='item-eval-info clearfix']/span[1]/text()")[0].encode('utf-8')
            item['comment_num'] = store.xpath(".//div[@class='item-eval-info clearfix']/span[1]/text()")[0].encode(
                'utf-8')
            item['area'] = store.xpath(".//div[@class='item-site-info clearfix']/span[1]/text()")[2].encode('utf-8')
            item['address'] = store.xpath(".//div[@class='item-site-info clearfix']/span[2]/text()")[0].encode('utf-8')
            perCapita = store.xpath(".//div[@class='item-price-info']/span[1]/text()")
            if len(perCapita) == 2:
                item['per_capita'] = perCapita[1].encode('utf-8')
            else:
                item['per_capita'] = 0.00
            item['meitun_url'] = url.encode('utf-8')

            print("门店[%s],门店链接[%s]" % (item['name'],item['meitun_url']))

            # 请求详情页
            yield Request(item['meitun_url'],callback=self.parse_detail,meta={"item": item})

    def parse_deail(self, response):
        selector = etree.HTML(response.text)
        item = response.meta['item']
        item['phone'] = selector.xpath(".//div[@class='seller-info-body']/dev[2]/span[2]/text()")[0].encode('utf-8')
        item['business_hours'] = selector.xpath(".//div[@class='seller-info-body']/dev[3]/span[2]/text()")[0].encode('utf-8')
        yield item

