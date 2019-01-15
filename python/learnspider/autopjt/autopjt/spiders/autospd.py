# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = "autospd"
    allowed_domains = ["sz.lianjia.com"]
    start_urls = (
        'https://sz.lianjia.com/ershoufang/',
    )

    def start_requests(self):
        for i in range(1, 101):
            # 通过上面总结的网址格式构造要爬取的网址
            url = "https://sz.lianjia.com/ershoufang/pg" + str(i) + "/"
            print(url)
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AutopjtItem()
        # 通过各Xpath表达式分别提取商品的名称、价格、链接、评论数等信息
        li_box = response.xpath("//ul[@class='sellListContent']//li")
        #print(response.xpath("//ul[@class='sellListContent']//li//div[@class='tag']/span[@class='subway']/text()").extract())
        i = 0
        item["title"] = []
        item["house_code"] = []
        item["village"] = []
        item["region"] = []
        item["desc"] = []
        item["flood"] = []
        item["follow_info"] = []
        item["sub_way"] = []
        item["tax_free"] = []
        item["total_price"] = []
        item["price"] = []
        for li in li_box:
            title = li.xpath(".//div[@class='title']/a/text()").extract()
            if not len(title):
                continue;

            item["title"].append(title[0])

            house_code = li.xpath(".//div[@class='title']/a/@data-housecode").extract()
            item["house_code"].append(house_code[0] if len(house_code) else '')

            village = li.xpath(".//div[@class='address']/div[@class='houseInfo']/a/text()").extract()
            item["village"].append(village[0] if len(village) else '')

            region = li.xpath(".//div[@class='flood']/div[@class='positionInfo']/a/text()").extract()
            item["region"].append(region[0] if len(region) else '')

            desc = li.xpath(".//div[@class='address']/div[@class='houseInfo']/text()").extract()
            item["desc"].append(desc[0] if len(desc) else '')

            flood = li.xpath(".//div[@class='flood']/div[@class='positionInfo']/text()").extract()
            item["flood"].append(flood[0] if len(flood) else '')

            follow_info = li.xpath(".//div[@class='followInfo']/text()").extract()
            item["follow_info"].append(follow_info[0] if len(follow_info) else '')

            sub_way = li.xpath(".//div[@class='tag']/span[@class='subway']/text()").extract()
            item["sub_way"].append(sub_way[0] if len(sub_way) else '')

            tax_free = li.xpath(".//div[@class='tag']/span[@class='taxfree']/text()").extract()
            item["tax_free"].append(tax_free[0] if len(tax_free) else '')

            total_price = li.xpath(".//div[@class='priceInfo']/div[@class='totalPrice']/span/text()").extract()
            item["total_price"].append(total_price[0] if len(total_price) else '')

            price = li.xpath(".//div[@class='priceInfo']/div[@class='unitPrice']/@data-price").extract()
            item["price"].append(price[0] if len(price) else '')
            # 提取完后返回item

        yield item
        # 接下来很关键，通过循环自动爬取100页的数据
        for i in range(1, 101):
            # 通过上面总结的网址格式构造要爬取的网址
            url = "https://sz.lianjia.com/ershoufang/pg" + str(i) + "/"
            print(url)
            # 通过yield返回Request，并指定要爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)        

