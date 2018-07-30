#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import bs4

raw_cookies = 'll="118281"; bid=ZNBeCmhjDYw; __utmc=30149280; __utmz=30149280.1522634243.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1481375625.1522634243; _gid=GA1.2.121743734.1522635881; ps=y; ue="r782820303@sina.com"; push_doumail_num=0; __utmv=30149280.4643; ap=1; push_noty_num=0; _pk_ses.100001.8cb4=*; __utma=30149280.1481375625.1522634243.1522659518.1522661545.4; __utmt=1; dbcl2="46431658:QamcTB+Dj+Q"; ck=qVQZ; _pk_id.100001.8cb4=be200258b0dd1ce8.1522634241.4.1522661929.1522659521.; __utmb=30149280.8.10.1522661545'
cookies={}  
for line in raw_cookies.split(';'):  
  key,value=line.split('=',1)#1代表只分一次，得到两个数据  
  cookies[key]=value  
testurl='https://www.douban.com/people/dylan085/'  
s=requests.get(testurl,cookies=cookies)  
soup = bs4.BeautifulSoup(s.text, 'html.parser')
div = soup.find('div', id= 'friend')
dd = div.findAll('dd')
for i in dd:
    url = str(i.findAll('a')[0]).split('=',1)[1].split('<',1)[0].split('>',1)[0]
    name = str(i.findAll('a')[0]).split('=',1)[1].split('<',1)[0].split('>',1)[1]
    print url,name

