#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column,Numeric,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义chengjiao对象:
class Chengjiao(Base):
    # 表的名字:
    __tablename__ = 'lj_chengjiao2'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    area = Column(String(64))
    build_year = Column(String(64))
    decoration = Column(String(64))
    elevator = Column(String(32))
    floor = Column(String(32))
    href = Column(String(64))
    orientation = Column(String(16))
    region = Column(String(16))
    sign_time = Column(String(16))
    style = Column(String(16))
    total_price = Column(Numeric(15,6))
    unit_price = Column(Numeric(15,6))
    add_time = Column(Integer)

    def __init__(self, row_dict):
        for key in row_dict:
            setattr(self, key, row_dict[key])

    def update(self, row_dict):
        for key in row_dict:
            setattr(self, key, row_dict[key])

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)