#! /usr/bin/env python
# coding: utf-8


# 导入可能要用到的模块
import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError


# 获得索引页的信息
def get_index(offset):
    base_url = 'http://www.guokr.com/apis/minisite/article.json?'
    data = {
        'retrieve_type': "by_subject",
        'limit': "20",
        'offset': offset
    }
    params = urlencode(data)
    url = base_url + params

    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        print('Error.')
        return None