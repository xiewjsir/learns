#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column,Numeric,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义对象:
class Store(Base):
    # 表的名字:
    __tablename__ = 'mall_store'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    classify = Column(String(64))
    area = Column(String(64))
    address = Column(String(256))
    phone = Column(String(16))
    business_hours = Column(String(64))
    per_capita = Column(Numeric(10,2))
    comment_num = Column(Integer)
    score = Column(Integer)
    add_time = Column(Integer)
    update_time = Column(Integer)

    def __init__(self, row_dict):
        for key in row_dict:
            setattr(self, key, row_dict[key])

    def update(self, row_dict):
        for key in row_dict:
            setattr(self, key, row_dict[key])

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, '门店对象')