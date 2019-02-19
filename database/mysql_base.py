#!/usr/bin/env python
# coding: utf-8

#导入SQLAlchemy

from sqlalchemy import Column, BIGINT, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建基类
Base = declarative_base()

#初始化数据库连接
engine = create_engine('mysql+pymysql://root:Lee@yunwei@2019@localhost:3306/test')

#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建session对象，后面的数据库操作都将基于session进行
session = DBSession()


#数据库操作方法
#初始化数据库
def init_db():
    Base.metadata.create_all(engine)

#删除数据库
def drop_db():
    Base.metadata.drop_all(engine)

#定义user类
class User(Base):
    __tablename__ = "user"


   #表结构
    id = Column(BIGINT, primary_key=True,  autoincrement=True)
    name = Column(String(20), unique=True)
    gender = Column(String(30))

#正式初始化数据库
init_db()


#增
#创建User对象
new_user = User(name='mrlizi', gender='man')
#添加session
session.add(new_user)
#批量添加
session.add_all([
    User(name='子非鱼', gender='M'),
    User(name='虞姬', gender='F'),
    User(name='花木兰', gender='F')
])

#提交即保存到数据库
session.commit()


result = session.query(User.name)
print (result)
