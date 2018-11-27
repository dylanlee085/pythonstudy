#!/usr/bin/env python
# coding:utf-8


import threading 
import time

class send_message(threading.Thread):
    def __init__(self,content):
        super(send_message, self).__init__()
        self.content=content
        
    def run(self):
        time.sleep(1)
        print 'the content is:%s\r' % self.content

for i in xrange(4):
    t = send_message(i)
    t.start()

print 'main thread end!'
