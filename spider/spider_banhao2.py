#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import requests
import json
import sys
import MySQLdb
from warnings import filterwarnings
reload(sys) 
sys.setdefaultencoding('utf-8')


def getResponse(page_num):
    url = "http://www.cgigc.com.cn/cgigc-backend/api/mobileGame/getLatestGameISBNSearchList"
    querystring = {"callback":"","curPage":page_num,"pageCount":"20","gameNameKey":"","unitName":"","approvalNo":"","isbnNo":""}
    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "dc38e7d6-d000-43c7-a145-46662dec6985"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    response = response.text.lstrip('(').rstrip(')')
    data = json.loads(response)
    for i in range (len(data['data']['gameisbn'])):
         gamename = data['data']['gameisbn'][i]['gamename']
         unitname = data['data']['gameisbn'][i]['unitname']
         copyrightname = data['data']['gameisbn'][i]['copyrightname']
         gametype = data['data']['gameisbn'][i]['gametype']
         approvalno = data['data']['gameisbn'][i]['approvalno']
         isbnno = data['data']['gameisbn'][i]['isbnno']
         yield gamename,unitname,copyrightname,gametype,approvalno,isbnno

def insert_mysql(gamename,unitname,copyrightname,gametype,approvalno,isbnno):
    host = 'localhost'
    user = 'root'
    passwd = 'yunwei'
    db = 'mysql'
    port = 3306
    filterwarnings('ignore', category = MySQLdb.Warning)
    conn = MySQLdb.connect(host, user, passwd, db, port, charset='utf8')
    cur = conn.cursor()
    cur.execute('create database if not exists banhao default charset=utf8')
    conn.select_db('banhao')
    cur.execute('create table if not exists banhao_info(id int(6) auto_increment primary key, gamename varchar(80) NOT NULL uniq, unitname varchar(80),copyrightname varchar(80),gametype varchar(80),approvalno varchar(80),isbnno varchar(80)) default charset=utf8')
    try:
            cur.execute('insert into banhao_info (gamename,unitname,copyrightname,gametype,approvalno,isbnno) values (%s,%s,%s,%s,%s,%s)',(gamename,unitname,copyrightname,gametype,approvalno,isbnno))
    except:
        print "记录已存在"
    conn.commit()
    cur.close()
    conn.close()
 

def main():
    url = "http://www.cgigc.com.cn/cgigc-backend/api/mobileGame/getLatestGameISBNSearchList"
    querystring = {"callback":"","curPage":"1","pageCount":"20","gameNameKey":"","unitName":"","approvalNo":"","isbnNo":""}
    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "dc38e7d6-d000-43c7-a145-46662dec6985"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    response = response.text.lstrip('(').rstrip(')')
    data = json.loads(response)
    totalcount = int(data['data']['@totalcount'])
    return totalcount
    
if __name__ == '__main__':
    page_num = int(main() + 1) 
    for i in range(1,page_num):
        for gamename,unitname,copyrightname,gametype,approvalno,isbnno in getResponse(i):
            insert_mysql(gamename,unitname,copyrightname,gametype,approvalno,isbnno)
