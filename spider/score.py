#!/usr/bin/env python

import time

from FilmScoreSpider import SpiderDouban

begin = time.time()

url="http://movie.douban.com/"

doubanSpider = SpiderDouban()
contentHTML = doubanSpider.openUrl(url)
print contentHTML
filmsDic = doubanSpider.getFilmsDictionary(contentHTML)
sortedFilms = doubanSpider.sortFilms(filmsDic)

for film in sortedFilms:
    print film[0], ":", film[1]

time_cons = "%.2f" % (time.time() - begin)
print "time consumed: " + time_cons + "s"