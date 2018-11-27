#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup


def get_url(url):
    response = requests.get(url)
    response.encoding = 'gb2312'
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    contents = soup.find_all(attrs={"id" : "menu"})
    urls = []
    for content in contents:
        content = content.find_all('div', class_='contain')
        for i in content:
            for i in i.find_all('a'):
                url = i.get('href')
                if 'http://www.dytt8.net' in url:
                    urls.append(url)
                if url.startswith('/html'):
                    url = 'http://www.ygdy8.net' + url
                    urls.append(url)
    return urls

def get_detail_url(urls):
    for url in urls:
        response = requests.get(url)
        response.encoding = 'gb2312'
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        contents = soup.find_all('div', class_='co_content8')
        for div in contents:
            for td in div.find_all(attrs={"height":"26"}):
                for a in td.find_all('a'):
                    url = a.get('href')
                    name = a.string
                    if 'index.html' not in url:
                        url = 'http://www.ygdy8.net' + url
                        yield url 


def get_html(url):
    response = requests.get(url)
    response.encoding = 'gb2312'
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find_all('div',class_="co_content8")
    for i in content:
        for p in i.find_all('p'):
            print p



if __name__ == "__main__":
    url = 'https://www.dytt8.net/'
    urls = get_url(url)
    for url in get_detail_url(urls):
        print get_html(url)
