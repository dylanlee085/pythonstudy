#!/usr/bin/env python
# coding: utf-8



import requests
import json

url = "https://app.finchina.com/finchinaAPP/getTheSameTradeData.action"

querystring = {"token":"2032323A32373A303820435354203230313931373139","user":"20190123090107_13682217185","accountingcode":"10150009","type":"co","child_type":"profitTable"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "fb2f2cd5-38bf-47ae-9429-246f5bb3c128"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

content = json.loads(response.text)
for i in content['data']:
    for  ii in i.values():
        print ii
