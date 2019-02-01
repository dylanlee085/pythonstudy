#!/usr/bin/env python
# coding: utf-8


import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

try:
    resp = requests.get('http://httpbin.org/get', timeout=0.5)
    print(resp.status_code)
except ReadTimeout:  # 访问超时的错误
    print 'Timeout'
except ConnectionError:  # 网络中断连接错误
    print 'Connect error'
except RequestException:  # 父类错误
    print 'Error'