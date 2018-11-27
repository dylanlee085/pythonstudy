#! /usr/bin/env python
# coding: utf-8



import requests
#这里使用的是第三方urllib库来请求url
import random
import lxml
from conn_db import art_db
#这里导入自定义的数据库连接、读写的库
from multiprocessing import Pool
#引用进程池，多进程的请求url

ua_list=[
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)"},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7"},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)"},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)"},
    {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0"}
    ]
#上面是user-agent池，存放多个不同的user-agent
header = {
        'User-Agent':random.choice(ua_list)["User-Agent"]
        }
#上面是动态的随机生成user—agent，减少被识别的风险

def url_request(url):
    requ = requests.get(url,headers=header)
    html = requ.read().decode("utf-8")
    return html
#请求目标url

def get_artist(url):
    html = url_request(url)
    html = lxml.etree.HTML(html)
    li_art = html.xpath('//*[@id="m-artist-box"]/li')
    for art in li_art:
        art_name=art.xpath(".//a[1]/text()")[0]
        art_id =art.xpath(".//a[1]/@href")[0]
        art_db.get_art(art_name,art_id)
        get_art_song(art_name,art_id)
#上面部分是得到所有的歌手信息：姓名，id
#调用自定义的db模块，信息存入到数据库中
#并且调用下面的函数，得到歌曲信息
#这里主要用到xpath方法对目标页面进行解析分离出自己想要的部分

def get_art_song(art_name,art_id):
      url = "https://music.163.com{}".format(art_id)
      html = url_request(url)
      html = lxml.etree.HTML(html)
      li_song = html.xpath('//ul[@class="f-hide"]/li')
      for song in li_song:
          song_name = song.xpath("./a/text()")[0]
          print("正在存储---{}--链接".format(song_name))
          song_src = song.xpath("./a/@href")[0]
          art_db.get_song(song_name,song_src,art_id)
#同样的将歌曲的信息，下载链接等存放如数据库中

if __name__ == "__main__":
#    华语歌手列表
    art_id_ch= [1001,1002,1003]
    #欧美歌手列表
    art_id_ou= [2001,2002,2003]
    #日本歌手列表
    art_id_jp= [6001,6002,6003]

    all_art_id = art_id_ch + art_id_ou + art_id_jp
    #所有分类歌手的id号
    pool = Pool()
    #创建进程池，将对应的分类id的url传入创建进程
    for x in all_art_id:
        url_artist = "https://music.163.com/discover/artist/cat?id={}".format(x)
        pool.apply_async(get_artist,(url_artist,))
        pool.close()
        pool.json()
