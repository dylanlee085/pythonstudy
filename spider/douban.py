#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
from collections import OrderedDict

url = 'https://accounts.douban.com/login'

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
Referer = "https://www.douban.com/"
# values = { 'ck' : 'xE5h', 'source' : 'None', 'form_email' : 'r782820303@sina.com' , 'form_password' : 'o7rgUdnV483D31vd' , 'captcha-solution' : 'society', 'captcha-id' : '39lyN6FnPBTejpta0zeCnVnj%3Aen', 'login' : '%E7%99%BB%E5%BD%95' }
# values = { 'source':'index_nav', 'form_email': 'r782820303@sina.com', 'form_password': 'o7rgUdnV483D31vd', 'captcha-solution': 'cause', 'captcha-id': 'FDYAj4zWbljtdAavhXgU44oG:en', 'user_login': '登录' }
values = OrderedDict()
values['source'] = 'index_nav'
values['form_email'] = 'r782820303@sina.com'
values['form_password'] = 'o7rgUdnV483D31vd'
values['captcha-solution'] = 'cause'
values['captcha-id'] = 'FDYAj4zWbljtdAavhXgU44oG:en'
values['user_login'] = '登录'
headers = { 'User-Agent' : user_agent, 'Referer': Referer }
data = urllib.urlencode(values)
print data
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
print page
