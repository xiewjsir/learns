#!/usr/bin/py

from time import sleep
from datetime import datetime
import tushare as c
import urllib.request as w
import os,stat
import pandas as Pd

# ----------------------- 转换股票代码
def _tcode(s):
    l = len(str(s))
    v = str(s)
    if(l>6):
        return v[:6]
    elif l==6:
        return v
    else:
        return ('0'*(6-l))+v


# -------------------------------------

c_sbf = 'data/stocks_b.csv' # 本文件存储股票基本信息

if not os.path.exists(c_sbf):
    c.get_stock_basics().to_csv(c_sbf)

stocks_b = Pd.read_csv(c_sbf) # 加载基本股票信息

codes = stocks_b['code']
names = stocks_b['name']
i_total=len(codes)*3
i_error=0
i_new=0
i_update=0

bs_url = 'http://quotes.money.163.com/service/zcfzb_{code}.html?type=year'
to_file_template = 'data/bs{code}.csv'

for v in range(len(codes)):
    to_file = to_file_template.format(code=_tcode(codes[v]))
    print(''.join(['[',str(v+1),'/',str(len(codes)),']',str(datetime.now())]),'正在下载',names[v],'资产负债表')
    if not os.path.exists(to_file): # 文件不存在则下载文件
        try:
            w.urlretrieve(bs_url.format(code=_tcode(codes[v])),to_file)
            i_new=i_new+1
            sleep(3)
        except Exception as e:
            i_error = i_error + 1
    else: # 文件过期重新下载
        if (datetime.now()-datetime.fromtimestamp(os.stat(to_file)[stat.ST_CTIME])).days>=90:
            try:
                w.urlretrieve(bs_url.format(code=_tcode(codes[v])),to_file)
                i_update=i_update+1
                sleep(3)
            except Exception as e:
                i_error=i_error+1

  # 文件正常则跳过 no-op

#-------------------下载利润表-----------------------------------------------

is_url = 'http://quotes.money.163.com/service/lrb_{code}.html?type=year'
to_file_template = 'data/is{code}.csv'

for v in range(len(codes)):
    to_file = to_file_template.format(code=_tcode(codes[v]))
    print(''.join(['[',str(v+1),'/',str(len(codes)),']',str(datetime.now())]),'正在下载',names[v],'利润表')
    if not os.path.exists(to_file): # 文件不存在则下载文件
        try:
            w.urlretrieve(is_url.format(code=_tcode(codes[v])),to_file)
            i_new=i_new+1
            sleep(3)
        except Exception as e:
            i_error = i_error + 1
    else: # 文件过期重新下载
        if (datetime.now()-datetime.fromtimestamp(os.stat(to_file)[stat.ST_CTIME])).days>=90:
            try:
                w.urlretrieve(is_url.format(code=_tcode(codes[v])),to_file)
                i_update=i_update+1
                sleep(3)
            except Exception as e:
                i_error=i_error+1

  # 文件正常则跳过 no-op

#-------------------下载现金流量表-----------------------------------------------
cf_url = 'http://quotes.money.163.com/service/xjllb_{code}.html?type=year'
to_file_template = 'data/cf{code}.csv'

for v in range(len(codes)):
    to_file = to_file_template.format(code=_tcode(codes[v]))
    print(''.join(['[',str(v+1),'/',str(len(codes)),']',str(datetime.now())]),'正在下载',names[v],'现金流量表')
    if not os.path.exists(to_file): # 文件不存在则下载文件
        try:
            w.urlretrieve(cf_url.format(code=_tcode(codes[v])),to_file)
            i_new=i_new+1
            sleep(3)
        except Exception as e:
            i_error = i_error + 1
    else: # 文件过期重新下载
        if (datetime.now()-datetime.fromtimestamp(os.stat(to_file)[stat.ST_CTIME])).days>=90:
            try:
                w.urlretrieve(cf_url.format(code=_tcode(codes[v])),to_file)
                i_update=i_update+1
                sleep(3)
            except Exception as e:
                i_error=i_error+1

  # 文件正常则跳过 no-op


print("总共数量:"+ str(i_total) + "\n本次新下载:"+str(i_new)+"\n更新:"+str(i_update)+"\n失败:"+str(i_error))
