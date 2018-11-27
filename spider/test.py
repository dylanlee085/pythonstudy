#!/usr/bin/env python
# coding: utf-8



import requests



with open('list2', 'r') as f:
    for i in f.readlines():
        i = i.rstrip('\n')
        url = 'http://whois.chinaz.com/' + i
        response = requests.get(url)
        print response, url
