#!/usr/bin/env python
#coding=utf-8

import multiprocessing

def do(n) :
#获取当前线程的名字
    name = multiprocessing.current_process().name
    print(name,'starting')
    print("worker ", n)
    with open('test.txt', 'a') as f:
        f.write('hello world!\n')

if __name__ == '__main__' :
    numList = []
    for i in xrange(8) :
        p = multiprocessing.Process(target=do, args=(i,))
        p.start()
        p.join()
        print("Process end.")
