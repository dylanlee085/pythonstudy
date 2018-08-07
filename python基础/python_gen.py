#!/usr/bin/env python
# coding: utf-8



def countdown(n):
    print "Counting down!"
    while n > 0:
        yield n
        n -= 1


for i in countdown(5):
    print i
