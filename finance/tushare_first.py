#! /usr/bin/env python
# coding: utf-8

import tushare as ts
from sqlalchemy import create_engine

ts.set_token('32e8ce3111dedfce4968ddde754c8b9240463075d077b8243a7668a0')
pro = ts.pro_api()

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,market,exchange,area,industry,list_date')
engine = create_engine('mysql://root:yunwei@localhost/stock?charset=utf8')

#存入数据库
data.to_sql('stock_name',engine, if_exists='append')

df = pro.daily(ts_code='000001.SZ', start_date='20190124', end_date='20190124')
df.to_sql('stock_daily',engine, if_exists='append')