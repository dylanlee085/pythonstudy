#!/usr/bin/env python
#coding:utf-8


import urllib
import urllib2
from collections import OrderedDict
import time

values = OrderedDict() #用于固定字典顺序
values['formhash'] = 'c84d4c38'
values['referer'] = 'http://www.sgsg.cn/home.php'
values['loginfield'] = 'username'
values['username'] = 'sgsg_085'
values['password'] = 'UNIh8BNblckfSDwS'
values['questionid'] = 0
values['answer'] = ''
data = urllib.urlencode(values)
print data
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
headers = { 'User-Agent' : user_agent }

url = "http://www.sgsg.cn/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LztST&inajax=1"
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request,timeout=10)
print response.read()  






