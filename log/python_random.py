#!/usr/bin/env python
# coding:utf-8


import logging
import getpass
import sys

class MyLog(object):
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)