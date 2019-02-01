#!/usr/bin/env python
# coding: utf-8


import MySQLdb
from warnings import filterwarnings
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
from xpinyin import Pinyin
import whois
import re

def query_mysql():
    host = 'localhost'
    user = 'root'
    passwd = 'yunwei'
    db = 'mysql'
    port = 3306
    filterwarnings('ignore', category = MySQLdb.Warning)
    conn = MySQLdb.connect(host, user, passwd, db, port, charset='utf8')
    cur = conn.cursor()
    conn.select_db('banhao')
    try:
            cur.execute('select gamename from banhao_info')
            list = cur.fetchall()
            
    except:
        print "记录已存在"
    conn.commit()
    cur.close()
    conn.close()
    for i in list:
        yield i[0]

def translate_pinyin(gamename):
    p = Pinyin() 
    if len(gamename) <= 4:
        zimu = p.get_initials(gamename,'')
        servicename = zimu + '.com'
        try:
            whois.whois(servicename)
#            print "%s, %s 该域名已被注册" % (gamename, servicename)
        except:
#            print "%s, %s 可以注册" % (gamename, servicename)
            print "%s, %s 域名无法访问" % (gamename, servicename)
   

    



if __name__ == "__main__":
    for gamename in query_mysql():
        translate_pinyin(gamename)
        continue
