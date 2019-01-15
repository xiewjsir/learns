# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    house_code = scrapy.Field()
    region = scrapy.Field()
    village = scrapy.Field()
    desc = scrapy.Field()
    flood = scrapy.Field()
    follow_info = scrapy.Field()
    sub_way = scrapy.Field()
    tax_free = scrapy.Field()
    total_price = scrapy.Field()
    price = scrapy.Field()
