#!/usr/bin/env python
#coding:utf-8


import requests

session = requests.Session()
url = "http://www.sgsg.cn/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LztST&inajax=1"
data = {'fastloginfield':'username','username':'sgsg_1946','password':'UNIh8BNblckfSDwS','quickforward':'yes','handlekey':'ls'}
session.post(url, data)
res = session.get('http://sgsg.cn/home.php?mod=space&do=home')
html = res.content.decode('gb2312')
print html
f = open('discuz.txt','w')
f.write(res.content)
f.flush()
f.close()





