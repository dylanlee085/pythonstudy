#!/usr/bin/env python
# coding:utf-8

#导入flask模块
from flask import Flask
#导入配置模块
from config import Config

#导入flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#导入flask_migrate
from flask_migrate import Migrate

#导入LoginManager
from flask_login import LoginManager

#导入mail模块
from flask_mail import Mail

#bootstrap
from flask_bootstrap import Bootstrap

#moment
from flask_moment import Moment

app = Flask(__name__)
#加载配置模块
app.config.from_object(Config)

#数据库实例
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#login实例
login = LoginManager(app)
login.login_view = 'login'

#mail实例
mail = Mail(app)

#bootstrap
bootstrap = Bootstrap(app)

#moment
moment = Moment(app)

#导入视图模块
from app import views, models, errors


#邮件配置
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_SSL']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

#记录日志到文件
if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')