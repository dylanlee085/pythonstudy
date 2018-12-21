#!/usr/bin/env python
# coding: utf-8

import requests

url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg"

querystring = {"g_tk":"146455691","jsonpCallback":"jsoncallback7783528157747723","loginUin":"782820303","hostUin":"0","format":"jsonp","inCharset":"utf8","outCharset":"GB2312","notice":"0","platform":"yqq","needNewCode":"0","cid":"205360772","reqtype":"2","biztype":"1","topid":"3595836","cmd":"8","needmusiccrit":"0","pagenum":"1","pagesize":"25","lasthotcommentid":"","callback":"jsoncallback7783528157747723","domain":"qq.com","ct":"24","cv":"101010"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "8872d240-541a-4a9f-8fe7-71c01d36d417"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
