#!/usr/bin/env python
#coding: utf-8


import urllib2
import bs4
import chardet

class SpiderDouban:
    def __init__(self):
        self.__headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64)')

    def openUrl(self,url):
        opener = urllib2.build_opener()
        opener.addheaders = [self.__headers]
        fileLikeObj = opener.open(url)
        contentString = fileLikeObj.read()
        fileLikeObj.close()
        encodingDictonary = chardet.detect(contentString)
        encoding = encodingDictonary['encoding']
        contentString = contentString.decode(encoding=encoding)
        return contentString

    def getFilmsDictionary(self,content):
        filmsDictionary = {}
        soup = bs4.BeautifulSoup(content, "html.parser")
        div = soup.find('div', class_= 'screening-bd')
        filmList = div.findAll('li', class_="ui-slide-item")

        for film in filmList:
            if ('data-rate' in film.attrs):
                if film['data-rate']:
                    filmsDictionary[film['data-title']] = float(film['data-rate'])
        return filmsDictionary

    def sortFilms(self,filmsDictionary):
        sortedFilms = sorted(filmsDictionary.items(), key=lambda x: x[1], reverse=True)
        return sortedFilms

