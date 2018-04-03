#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import bs4

testurl='http://ishibk.com/jbyf'  
s=requests.get(testurl)  
soup = bs4.BeautifulSoup(s.text, 'html.parser')
div = soup.find('div', class_= 'content')
li = div.findAll('li')
for i in li:
#    print i.find('a')['title']
#    print i.find('a')['href']
#    print i.find('a').find('img')['src']
    ss=requests.get(i.find('a')['href'])  
    soups = bs4.BeautifulSoup(ss.text, 'html.parser')
    div = soups.find('div', class_= 'entry')
    #if div.find('p') == None:
    #    continue
    #else:
    #    print str(div.find('p')).split('>',1)[1].split('<',1)[0]
    for sections in div.findAll('section',class_=''):
        print str(sections)
        
