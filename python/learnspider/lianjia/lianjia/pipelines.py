# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.chengjiao import Chengjiao

class MysqlPipeline(object):
    def __init__(self):
        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/spider')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        self.session = DBSession()

    def process_item(self,item,spider):
        item['add_time'] = time.time()
        row = Chengjiao(item)
        # 添加到session:
        self.session.add(row)
        # 提交即保存到数据库:
        self.session.commit()
        return item

    def close_spider(self,spider):
        # 关闭session:
        self.session.close()


"""
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="spider", port=3306, charset="utf8")

    def process_item(self, item, spider):
        print(item)
        print(item['area'])
        add_time = time.time()
        sql = "insert into lj_chengjiao(area,build_year,decoration,elevator,floor,href,name,orientation,region,sign_time,style,total_price,unit_price,add_time)values('" + str(item['area']) + "','" + str(item['build_year']) + "','" + str(item['decoration']) + "','" + str(item['elevator']) + "','" + str(item['floor']) + "','" + str(item['href']) + "','" + str(item['name']) + "','" + str(item['orientation']) + "','" + str(item['region']) + "','" + str(item['sign_time']) + "','" + str(item['style']) + "','" + str(item['total_price']) + "','" + str(item['unit_price']) + "','" + str(add_time) + "')";
        print(sql)
        self.conn.query(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
"""

"""
import pymongo
class MongoPipeline(object):
 
    collection = 'lianjia_test'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        data = dict(item)
        table.insert_one(data)
        return item
"""
