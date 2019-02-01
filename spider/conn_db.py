#! /usr/bin/env python
# coding: utf-8



import pymysql as pm

class Mysqlpython:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.db = "song_db"
        self.user = "root"
        self.passwd = "yunwei"
        self.charset = "utf8"
        #上面是数据库的基本参数
        self.conn = pm.connect(host=self.host, port=self.port, db=self.db, user=self.user,
                            passwd=self.passwd,
                            charset=self.charset)
        self.cur = self.conn.cursor()
    #这里初始化的创建连接数据库，不会再使用时重复调用

    def get_art(self, art_name,art_id):
        sql1 =" CREATE TABLE art_id(id int PRIMARY KEY AUTO_INCREMENT,art_name varchar(50) NOT NULL,art_id varchar(50) NOT NULL);"
        sql2 ="CREATE UNIQUE INDEX art_id_art_id_uindex ON art_id (art_id);"
        #创建歌手表，生成唯一索引，在后续的歌曲下载过程中加快搜索速度
        sql3  = "INSERT INTO `song_db`.`art_id` (`art_name`, `art_id`) VALUES ('{}', '{}');".format(art_name,art_id)
        try:
            self.cur.execute(sql1)
            self.cur.execute(sql2)
            self.conn.commit()
         #使用try语句创建数据库，判断如果数据库已经创建过的，就生成异常，跳过创建
        except:
            pass
        try:
            self.cur.execute(sql3)
            self.conn.commit()
            #将爬取的歌手信息存储到数据库中
        except:
            pass
        return None

    def get_song(self,song_name,song_src,art_id):
        sql1 = "CREATE TABLE song_id(id int PRIMARY KEY AUTO_INCREMENT,song_name varchar(50),song_id varchar(50),song_art_id varchar(50));"
        sql2 = "INSERT INTO `song_db`.`song_id` (`song_name`, `song_id`, `song_art_id`) VALUES ('{}', '{}', '{}');".format(song_name,song_src,art_id)
        try:
            self.cur.execute(sql1)
            self.conn.commit()
        except:
            pass
        try:
            self.cur.execute(sql2)
            self.conn.commit()
        except:
            pass
        return None
    #上面同样是创建歌曲表，将爬取的歌曲信息存放如数据库中

    def select_song(self,name,song):
        sql = "SELECT art_name,song_name,song_id from art_id join(select song_name,song_id,song_art_id from song_id)t on song_art_id =art_id and song_name='{}' and art_name = '{}';".format(song,name)
        self.cur.execute(sql)
        songs = self.cur.fetchall()
        self.conn.commit()
        return songs
    #上面部分对应的是，在下载歌曲中查找的操作

art_db = Mysqlpython()
