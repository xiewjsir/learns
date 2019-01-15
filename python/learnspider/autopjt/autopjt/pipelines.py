# -*- coding: utf-8 -*-
import codecs
import json
import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopjtPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="hexun", port=3306, charset="utf8")

    def process_item(self, item, spider):
        for j in range(0, len(item['title'])):
            title = item['title'][j]
            house_code = item['house_code'][j]
            region = item['region'][j]
            village = item['village'][j]
            desc = item['desc'][j]
            flood = item['flood'][j]
            follow_info = item['follow_info'][j]
            sub_way = item['sub_way'][j]
            tax_free = item['tax_free'][j]
            total_price = item['total_price'][j]
            price = item['price'][j]
            add_time = ''
            sql = "insert into lianjia2(title,house_code,region,village,`desc`,flood,follow_info,sub_way,tax_free,total_price,price,add_time)values('" + title + "','" + house_code + "','" + region + "','" + village + "','" + desc + "','" + flood + "','" + follow_info + "','" + sub_way + "','" + tax_free + "','" + total_price + "','" + price + "','" + add_time + "')";
            #print(sql)
            self.conn.query(sql)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
