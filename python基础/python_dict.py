#!/usr/bin/env python
# coding: utf-8


#创建一个字典
prices = {
    "GOOG" : 490.10,
    "APPL" : 123.50,
    "IBM" : 91.50,
    "MSFT" : 52.13
}
print type(prices)


#创建空字典
prices = {}
prices = dict()


#判断对象是否是字典成员
#方法1
if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0

#方法2
p = prices.get("SCOX", 0.0)
print p

#获取字典关键字列表
syms = list(prices)

del prices['MSFT']
print prices
