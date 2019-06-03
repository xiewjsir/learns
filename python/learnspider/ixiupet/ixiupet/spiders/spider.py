from scrapy import Spider, Request
import re
from lxml import etree
import json
from urllib.parse import quote
from ixiupet.items import StoreItem


class Ixiupet_spider(Spider):
    name = 'ixiupet'
    allowed_domains = ['sz.meituan.com/chongwu']
    classifys = {
               'c21151': '购宠',
               #'c21150': '宠物食品',
               #'c20692': '宠物店'
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
            item['classify'] = self.classifys.get(response.meta['classify'])
            item['name'] = store.xpath(".//a[@class='item-title']/text()")[0]
            item['score'] = store.xpath(".//div[@class='item-eval-info clearfix']/span[1]/text()")[0]
            item['comment_num'] = store.xpath(".//div[@class='item-eval-info clearfix']/span[1]/text()")[0]
            item['area'] = store.xpath(".//div[@class='item-site-info clearfix']/span[1]/text()")[2]
            item['address'] = store.xpath(".//div[@class='item-site-info clearfix']/span[2]/text()")[0]
            perCapita = store.xpath(".//div[@class='item-price-info']/span[1]/text()")
            if len(perCapita) == 2:
                item['per_capita'] = perCapita[1]
            else:
                item['per_capita'] = ''
            item['phone'] = ''
            item['business_hours'] = ''
            yield item

    def parse_content(self, response):
        selector = etree.HTML(response.text)
        cj_list = selector.xpath("//ul[@class='listContent']/li")

        for cj in cj_list:
            item = StoreItem()
            item['classify'] = self.classifys.get(response.meta['classify'])
            href = cj.xpath('./a/@href')
            if not len(href):
                continue
            item['href'] = href[0]

            content = cj.xpath('.//div[@class="title"]/a/text()')
            if len(content):
                content = content[0].split()  # 按照空格分割成一个列表
                item['name'] = content[0]
                item['style'] = content[1]
                item['area'] = content[2]

            content = cj.xpath('.//div[@class="houseInfo"]/text()')
            if len(content):
                content = content[0].split('|')
                item['orientation'] = content[0]
                item['decoration'] = content[1]
                if len(content) == 3:
                    item['elevator'] = content[2]
                else:
                    item['elevator'] = '无'

            content = cj.xpath('.//div[@class="positionInfo"]/text()')
            if len(content):
                content = content[0].split()
                item['floor'] = content[0]
                if len(content) == 2:
                    item['build_year'] = content[1]
                else:
                    item['build_year'] = '无'

            content = cj.xpath('.//div[@class="dealDate"]/text()')
            if len(content):
                item['sign_time'] = content[0]

            content = cj.xpath('.//div[@class="totalPrice"]/span/text()')
            if len(content):
                item['total_price'] = content[0]

            content = cj.xpath('.//div[@class="unitPrice"]/span/text()')
            if len(content):
                item['unit_price'] = content[0]

            content = cj.xpath('.//span[@class="dealHouseTxt"]/span/text()')  # 返回的是一个字符串列表
            if len(content):
                for i in content:
                    if i.find("房屋满") != -1:  # 找到了返回的是非-1得数，找不到的返回的是-1
                        item['fangchan_class'] = i
                    elif i.find("号线") != -1:
                        item['subway'] = i
                    elif i.find("学") != -1:
                        item['school'] = i
            yield item
