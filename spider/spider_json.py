#!/usr/bin/env python
# coding: utf-8


'''
1.无须登录
2.使用requests库
3.直接返回html，不对网页进行处理
'''

import requests
import json
import xproxy
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')


def get_html(url):
    proxy = xproxy.get_random_ip()
    print proxy
    try:
        cookie = '_ga=GA1.2.740474103.1516937896; _lxsdk_cuid=1653c833a46c8-0e342a087163f-37664109-1fa400-1653c833a46c8; ci=20; rvct=20; client-id=8b4c5f07-2165-4da3-a91e-5c31998e9c7c; uuid=34ea6c482be74382a9c4.1534407762.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=213709739.1534318588278.1534388216039.1534407767661.5"; _lxsdk=1653c833a46c8-0e342a087163f-37664109-1fa400-1653c833a46c8; oc=4nq2dgra3JoVT2ZzFO97Hz_nYIwMhayoNkVlKbinTW5YJyQeg2ZWGx5y_D1w9ao7m8D7Xnlirerb3NxXjed6PG2sAgmiHaavFKr0HRIAy2ARt3NJj2a9RuG8St_IKo3jYRkDayDMGj3TtLV1ZeYAa7Xfuslr28bAKj5ZZO8aUvA; _lxsdk_s=16541d43d48-4e0-81d-a01%7C%7C8'
        headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', 'Cookie': cookie}
        response = requests.get(url, headers=headers, proxies=proxy)
        if response.status_code ==200:
            html = response.text
            return html
    except RequestException:
        return None

def para_html(html):
    data = json.loads(html)
    infos = []
    for i in data['data']['poiInfos']:
        info = ['店名: %s' % i['title'], '评分: %s' % i['avgScore'], '评论: %s' % i['allCommentNum'], '地址: %s\n' % i['address']]
#        socre = '评分: %s' % i['avgScore']
#        comment = '评论: %s' % i['allCommentNum']
#        address = '地址: %s\n' % i['address']
        infos.append(info)
    return infos
        
        

if __name__ == '__main__':
    for num in range(1,15):
        url = 'http://gz.meituan.com/meishi/api/poi/getPoiList?cityName=%%E5%%B9%%BF%%E5%%B7%%9E&cateId=393&areaId=0&sort=&dinnerCountAttrId=&page=%d&userId=&uuid=c630a135ff0544879740.1534318576.1.0.0&platform=1&partner=126&originUrl=http%%3A%%2F%%2Fgz.meituan.com%%2Fmeishi%%2Fc393%%2F&riskLevel=1&optimusCode=1&_token=eJxdjktvqkAYhv%%2FLbCHOjAwKJl1YLAqiUlC5NF1wuIOAhUGU5vz3Mybt5iRf8l6%%2BZ%%2FF%%2Bg1aLwAIjJCPEg1vcggXAEzSZAR7Qjn1EgQgymhJRfALhf92c8OBPe16BxQcWES8T4fNZWCx%%2FYHmKeIwk9Mn%%2FesL8lLB7UhqDQEbpdQFhOk6qOKd9UE%%2FCpoLMd1kOQ0EWIBsCGF4dGc60%%2FNHgR%%2Blv3rHljO3ytGYu1oeoONHDcnx7tw6cnfkJR8yytNVZ2urLPMoeqRhXvqMNMGjDYnDW5LUy1MDVzJXR1yfqtMv7SpG4LZJ2K2%%2FwZ52kbRL3oeS9AKFgSNzd0u33oq0vt1yv3Ksh7rSM1u1BGZti15zoVU0CwXdEU%%2FnCSZhrqdWVM3d%%2FquMOb%%2FfwYmdHDxaemhu3c%%2BVF%%2BuUVk9Gy5sftmnMTZR1zcZD7uFET6eYMvSGJ5tk7PEhbN2HW76UqDenopJuAzAvzrSxoZG9c%%2Baux18sX8Pcf0wCO4w%%3D%%3D' % num
        html = get_html(url)
        print para_html(html)
