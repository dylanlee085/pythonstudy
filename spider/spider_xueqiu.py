#! /usr/bin/env python
# coding: utf-8



'''
1.获取组合名字
2.获取组合股票组成
3.将股票名字存入mysql数据库
'''


import requests
import json
import sys
import MySQLdb
from warnings import filterwarnings
reload(sys)
sys.setdefaultencoding('utf-8')
import time

def get_symbol_name():
    url = "https://xueqiu.com/cubes/discover/rank/cube/list.json"

    querystring = {"category": "12", "count": "400", "market": "cn", "profit": "monthly_gain"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "bf73aa42-b70a-402e-b24d-5957bdfdeed9",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Cookie': '_ga=GA1.2.2114160061.1542957935; device_id=b1a75b5e65f063a698e3bcd20ed84f42; s=f312y796sw; aliyungf_tc=AQAAAMhFHA82tggAsotscf6gwrB8v2/6; __utmc=1; __utmz=1.1546052848.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _gid=GA1.2.1421482253.1546052872; Hm_lvt_1db88642e346389874251b5a1eded6e3=1546052848,1546052860,1546052871,1546052930; xq_a_token=f5f63e5386ac62a766832d42006c34e3bb9c262c; xqat=f5f63e5386ac62a766832d42006c34e3bb9c262c; xq_r_token=d586c6bbb68c5bc1c6c4e57abdde0feecd5a370b; xq_token_expire=Wed%20Jan%2023%202019%2011%3A13%3A30%20GMT%2B0800%20(CST); xq_is_login=1; u=3615725511; bid=275c540b18c399d811752e1bec2b53c2_jq8w65tz; __utma=1.2114160061.1542957935.1546060066.1546064167.4; __utmt=1; __utmb=1.15.10.1546064167; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1546066187'
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    html = (response.text)
    return html


def para_symbol_html(html):
    data = json.loads(html)
    symbols = []
    for i in data['list']:
        # print i['id'],
        # print i['name'],
        # print i['symbol'],
        # print i['daily_gain'],
        # print i['monthly_gain'],
        # print i['total_gain']
        symbols.append(i['symbol'])
    return symbols


def get_stock_name(symbols):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Cookie':'_ga=GA1.2.2114160061.1542957935; device_id=b1a75b5e65f063a698e3bcd20ed84f42; s=f312y796sw; aliyungf_tc=AQAAAMhFHA82tggAsotscf6gwrB8v2/6; __utmc=1; __utmz=1.1546052848.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _gid=GA1.2.1421482253.1546052872; Hm_lvt_1db88642e346389874251b5a1eded6e3=1546052848,1546052860,1546052871,1546052930; xq_a_token=f5f63e5386ac62a766832d42006c34e3bb9c262c; xqat=f5f63e5386ac62a766832d42006c34e3bb9c262c; xq_r_token=d586c6bbb68c5bc1c6c4e57abdde0feecd5a370b; xq_token_expire=Wed%20Jan%2023%202019%2011%3A13%3A30%20GMT%2B0800%20(CST); xq_is_login=1; u=3615725511; bid=275c540b18c399d811752e1bec2b53c2_jq8w65tz; __utma=1.2114160061.1542957935.1546060066.1546064167.4; __utmt=1; __utmb=1.15.10.1546064167; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1546066187'
    }
    for symbol in symbols:
        print "========%s=========" % symbol
        url = 'https://xueqiu.com/p/' + symbol +'?from=singlemessage&isappinstalled=0'
  #      url = 'https://xueqiu.com/p/' + symbol
        response = requests.get(url, headers=headers)
        html = response.text
        pos_start = html.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
        pos_end = html.find('SNB.cubePieData')
        data = html[pos_start:pos_end]
        data = json.loads(data.split(';')[0])
        for stock in  data['last_rebalancing']['holdings']:
            stock_symbol = stock['stock_symbol']
            stock_name = stock['stock_name']
            weight = stock['weight']
            yield symbol, stock_symbol ,stock_name, weight
        print "========%s=========" % symbol

def insert_mysql(symbol, stock_symbol ,stock_name, weight):
    host = 'localhost'
    user = 'root'
    passwd = 'yunwei'
    db = 'mysql'
    port = 3306
    filterwarnings('ignore', category = MySQLdb.Warning)
    conn = MySQLdb.connect(host, user, passwd, db, port, charset='utf8')
    cur = conn.cursor()
    cur.execute('create database if not exists xueqiu default charset=utf8')
    conn.select_db('xueqiu')
    cur.execute('create table if not exists zh_info(id int(6) auto_increment primary key, symbol varchar(80) NOT NULL, stock_symbol varchar(80),stock_name varchar(80), weight varchar(80)) default charset=utf8')
    try:
            cur.execute('insert into zh_info (symbol, stock_symbol ,stock_name, weight) values (%s,%s,%s,%s)',(symbol, stock_symbol ,stock_name, weight))
    except:
        print "记录已存在"
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    html = get_symbol_name()
    symbols = para_symbol_html(html)
    for symbol, stock_symbol ,stock_name, weight in get_stock_name(symbols):
        insert_mysql(symbol, stock_symbol, stock_name, weight)
        time.sleep(10)
