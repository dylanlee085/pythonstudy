#!/usr/bin/env python
# coding:utf-8


import requests
import time
import json
import sys

def get_one_page(url):
    try:
        headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            return response.text
    except RequestException:
        return None

def para_page(html):
    info = json.loads(html)
    print "country:",info["country"]
    print "region:" ,info["region"]
    print "city:",info["city"]
    print "isp:" ,info["isp"]
    print "lon,lat:" ,info["lon"],info["lat"]





if __name__ == '__main__':
    ip = sys.argv[1]
    url = 'http://ip-api.com/json/%s' % (ip)
    html = get_one_page(url)
    para_page(html)
