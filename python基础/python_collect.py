#!/usr/bin/env python
# coding: utf-8

#创建一个集合
s = set([3,5,910])

#创建一个唯一字符集合
t = set('Hello')

#t和s的并集
a = t | s

#t和s的交集
b = t & s

#求差集(项在t中，但不在s中)
c = t - s

#对称差集(项在t或者s中,但不会同时出现在二者中)
d = t ^ s

#向集合中添加一个新项目
t.add('x')

#向集合中添加多个新项目
s.update([10,37,42])

#将集合中某项删除
t.remove('H')
