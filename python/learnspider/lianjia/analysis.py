#!/usr/bin/env pythone3
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib

engine = create_engine("mysql+pymysql://root@127.0.0.1:3306/spider?charset=utf8")

ret = pd.read_sql_query("select id,name,area,total_price,unit_price,sign_time,sign_month from lj_chengjiao limit 20000",engine)

price_mean = ret[ret['sign_month']>'201412'][['sign_month','unit_price']].groupby('sign_month').mean()
print(price_mean)

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
price_mean.plot()
plt.title('走势图')
plt.xlabel('月份')
plt.ylabel('价格')
#plt.savefig('04csdn.png',dpi=400)
plt.show()



#print(ret)
#pd.io.sql.to_sql(thedataframe,'tablename', yconnect, schema='databasename', if_exists='append')