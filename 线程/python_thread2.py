#!/usr/bin/env python
# coding:utf-8


import threading
import time



'''
https://www.cnblogs.com/yeayee/p/4952022.html
https://www.cnblogs.com/tkqasn/p/5700281.html
'''

#方法二：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print 'the arg is:%s\r' % self.arg

for i in xrange(4):
    t =MyThread(i)
    t.start()
