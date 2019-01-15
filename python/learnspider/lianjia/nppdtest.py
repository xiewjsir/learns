#!/usr/bin/env python3
# -*- coding -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from sqlalchemy import create_engine

"""
arr1 = np.arange(10,20)
print(arr1)
sarr1 = pd.Series(arr1)
print(sarr1)

sarr2 = pd.Series({'a':1,'b':2,'c':6})
print(sarr2)

arr2 = np.arange(10,22).reshape(4,3)
print(arr2)

darr1 = pd.DataFrame(arr2)
print(darr1)

darr2 = pd.DataFrame({'a':[2,3,4,5],'b':[6,7,8,9],'c':[10,11,12,13]})
#print(darr2)

darr3 = pd.DataFrame({'one':{'a':2,'b':3,'c':4},'tow':{'a':5,'b':6,'c':7},'three':{'a':8,'b':9,'c':10}})
#darr3.index = ['c','d','e']
#darr3.columns = ['four','five']
print(darr3[0:2])

s5 = pd.Series(np.array([10,15,20,30,55,80]),
index = ['a','b','c','d','e','f'])
print(s5)
s6 = pd.Series(np.array([12,11,13,15,14,16]),
index = ['a','c','g','b','d','f'])
print(s6)
print(s5 + s6)
print(s5/s6)
"""

darr3 = pd.DataFrame({'one':{'a':2,'b':3,'c':4},'tow':{'a':5,'b':6,'c':7},'three':{'a':8,'b':9,'c':10}})
print(darr3.head())


#d1 = ret.ix[0:1,['id','name','area','total_price','sign_time']].head()
#d2 = ret.ix[2:3,['id','name','area','total_price','sign_time']].head()
#print(d1)
#print(d2)
#d3 = pd.concat([d1,d2])
#print(d3)
#d4 = pd.DataFrame(d3,columns=['id','name','area','total_price','sign_month'])
#print(d4)
#print(d3.drop([1]))
#print(d3.drop(['name'],axis=1))
#d3.ix[d3['id']==1,'sign_time'] = 201708
#print(d3)


