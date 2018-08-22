#!/usr/bin/env python
# coding:utf-8

'''
1. 爬取线路
2. 爬取对应线路的站点
3. 爬取站点的经纬度信息
'''


import requests
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
from warnings import filterwarnings

def get_url(city):
    urls = []
    for type1 in range(1,10):
        url = 'http://%s.8684.cn/list%d' % (city, type1)
        urls.append(url)
    for type2 in range(65,91):
        url = 'http://%s.8684.cn/list%s' % (city, chr(type2))
        urls.append(url)
    return urls

def get_line(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('div', class_='stie_list')
        for i in content:
            for i in i.find_all('a'):
                yield i.get('href')

def get_position(url,prefix):
    fullurl = url + prefix
    response = requests.get(fullurl)
    soup = BeautifulSoup(response.text, 'lxml')
    ways = soup.find_all('strong')
    forwards = []
    for forward in ways[0]:
        forwards.append(forward)
    positions = soup.find_all('div', class_='bus_site_layer')
    count1 = len(positions[0].find_all('a'))
    global count2
    f_positions = []
    for f_position in positions[0].find_all('a'):
        f_positions.append(f_position.string)
    backs = []
    b_positions = []
    if len(ways) > 1:
        for back in ways[1]:
            backs.append(back)
        count2 = len(positions[1].find_all('a'))
        for b_position in positions[1].find_all('a'):
            b_positions.append(b_position.string)
        values = forwards, f_positions, count1,  backs,  b_positions, count2
    else:
        values = forwards, f_positions, count1
    return values

def insert_mysql(values):
    host = 'localhost'
    user = 'root'
    passwd = 'yunwei'
    db = 'mysql'
    port = 3306
    filterwarnings('ignore', category = MySQLdb.Warning)
    conn = MySQLdb.connect(host, user, passwd, db, port, charset='utf8')
    cur = conn.cursor()
    cur.execute('create database if not exists bus default charset=utf8')
    conn.select_db('bus')
    cur.execute('create table if not exists bus_info(id int(6) auto_increment primary key, forwards varchar(80) NOT NULL unique, f_positions varchar(200), count int(6), backs varchar(80), b_positions varchar(200), count2 int(6)) default charset=utf8')
    forward = values[0][0]
    f_position = ','.join(values[1])
    count1 = values[2]
    global backs
    global b_positions
    global count2
    if len(values) < 6:
        backs = 'NULL'
        b_positions = 'NULL'
        count2 = 'NULL'
    else:
        backs = values[3][0]
        b_positions = ','.join(values[4])
        count2 = values[5]
    try:
        cur.execute('insert into bus_info (forwards,f_positions,count,backs,b_positions,count2) values (%s,%s,%s,%s,%s,%s)',(forward,f_position,count1,backs,b_positions,count2))
    except:
        print "记录已存在"
        
    #try:
    #    cur.execute('insert into bus_info (forwards,f_positions,count,backs,b_positions,count2,) values (%s,%s,%s,%s,%s,%s)',values)
    #except:
    #    print "记录已存在"
    conn.commit()
    cur.close()
    conn.close()



           
if __name__ == '__main__':
    city = 'shaoguan'
    url = 'http://%s.8684.cn' % city
    urls = get_url(city)
    for prefix in get_line(urls):
        values = get_position(url,prefix)
        insert_mysql(values)
      
        
        
