#!/usr/bin/env python
# coding: utf-8

import threading 
import time


class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg=arg
    def run(self):
        time.sleep(1)
        print 'the arg is:%s\r' % self.arg

for i in xrange(4):
    t = MyThread(i)
    t.start()

print 'main thread end!'
