#! /usr/bin/env python
# coding: utf-8



import requests
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')
from bs4 import BeautifulSoup


def get_html():
    url = 'https://www.smzdm.com/fenlei/zhinengshouji/p2/#feed-main'
    headers = {
        "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        "Cookie": '__ckguid=5lF6GloqpCs1fA5ckToWcs; __jsluid=d2b40c2751639a30708231a17b5d5ff9; smzdm_user_view=B4812825100C5AE46FCF6C1D97EAB901; smzdm_user_source=E8AD62FCBB9DE83FC62B8B584FBB7427; wt3_eid=%3B999768690672041%7C2153916130900627391%232153916130900389064; device_id=19029390581539161311243383221202a9ecfec6916e0593bbb9a0f94c; _ga=GA1.2.1714720527.1539161312; PHPSESSID=817530eb99e8f75aaf69234b5007b3f9; ad_date=22; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%22J_feed_ad3%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%22J_feed_ad4%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%7D; _gid=GA1.2.1060770298.1540174336; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1539161311,1540174333,1540174448,1540177478; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DdmHngXT9TPZ3buR5C-z4UW4WvyMevBY8c4t-14d2QBWcqWg2UX4ZJhMk4XWqwTAFrxrieLR0K0ODrsQpb28Fdq%26wd%3D%26eqid%3De9d38f7c00018a04000000065bcd4364%22%7D; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1540179520'}
    response = requests.get(url, headers)
    html = response.text
    print html
    return html


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.findAll('ul', id='feed-main-list')
    print content


def main():
    html = get_html()
    parse_html(html)


if __name__ == '__main__':
    main()
