#! /usr/bin/env python
# coding: utf-8


'''
1.获取淘宝联盟数据
2.将联盟数据插入数据库
3.分析数据库中高佣金率的品类
'''


import requests
import xproxy
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


def get_html(url):
    cookie = 't=6306762e8a7a7ed91272114e445de42e; cookie2=12d59564dd393fc66b9eecb2ad60e6b7; v=0; _tb_token_=e8fe3e03a53e3; cna=RHEmFMCbGkcCAXFsi7KGby/s; JSESSIONID=A979FB39DE0797A3CBC0C4A97C3F1CE9; rurl=aHR0cDovL3B1Yi5hbGltYW1hLmNvbS9teXVuaW9uLmh0bT9zcG09YTIxOXQuNzkwMDIyMS8xLjE5OTg5MTA0MTkuZGQ0MDNiMGNhLjJhOGY3NWE1NVlHRWs1IyEvcHJvbW8vc2VsZi9hY3Rpdml0eQ%3D%3D; isg=BG1tOgNNygnJt65lT9I8F_tPfA8nYoWVSs03C69yrYRyJo3YdxsxbKbwFLplprlU'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Cookie': cookie}
    proxy = xproxy.get_random_ip()
    response = requests.get(url, headers, proxies=proxy)
    content = response.json()
    print content


if __name__ == '__main__':
    url = 'https://pub.alimama.com/items/channel/qqhd.json?spm=a219t.7900221%2F1.1998910419.d435ff811.2a8f75a55YGEk5&channel=qqhd&perPageSize=50&shopTag=&t=1539658265946&_tb_token_=e8fe3e03a53e3&pvid=19_113.108.139.178_6369_1539658265443'
    get_html(url)
