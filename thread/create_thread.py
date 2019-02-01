#!/usr/bin/env python
# coding: utf-8

import threading
import time

def action():
    time.sleep(1)
    print 'the name\r'


for i in 'dylan','lee':
    t = threading.Thread(target=action, args=())
    t.start()
