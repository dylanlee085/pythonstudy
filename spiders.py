#!/usr/bin/env python
#coding:utf-8

import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    if hasattr(e, "code"):
        print e.code
except urllib2.URLError,e:
    if hasattr(e,"reason"):
        print e.reason
else:
    print "ok"