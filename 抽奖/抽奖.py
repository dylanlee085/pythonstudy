#! /usr/bin/env python
# coding: utf-8


import random

# 输入一个抽奖池~~~~
peopledict = {}
with open('list.txt', 'r') as f:
    for i in f.readlines():
        num = i.split()[0]
        name = i.split()[1]
        peopledict[num] = name

# 抽奖结果
resultdict = {}
# 请输入抽奖次数
try:
    num = int(raw_input("please input num:"))
except:
    print "input error"

# 进行抽奖啦啦啦
while num > 0:
    result = random.choice(peopledict.keys())
    resultdict[result] = peopledict[result]
    print resultdict[result]
    # 防止一个恶心的人被连续中奖两次！！！
    del peopledict[result]
    num -= 1
