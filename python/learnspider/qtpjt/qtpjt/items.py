# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QtpjtItem(scrapy.Item):
    # 建立picurl存储图片的网址
    picurl = scrapy.Field()
    # 建立picid存储图片网址中的图片名，以方便构造本地文件名
    picid = scrapy.Field()
