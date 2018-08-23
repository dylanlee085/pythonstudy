#!/usr/bin/env python
# coding: utf-8


#def way():
#    print "way 1"


#def way2():
#    print "way 2"




def decorator(func):
    def way():
        print "way 1"
        func()
    return way

@decorator
def way2():
    print "way 2"
    
way2()
