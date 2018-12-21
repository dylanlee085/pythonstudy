#!/usr/bin/env python
# coding:utf-8

#导入flask模块
from flask import Flask
#导入配置模块
from config import Config



app = Flask(__name__)
#加载配置模块
app.config.from_object(Config)

#导入视图模块
from app import views


