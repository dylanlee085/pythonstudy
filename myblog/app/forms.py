#!/usr/bin/env python
# coding: utf-8

#从flask_wtf导入FlaskForm的基类
from flask_wtf import FlaskForm
#由于flask_wtf插件本身提供字段类型,所以从wtf从wtforms导入四个表示表单字段的类
from wtforms import StringField, PasswordField, BooleanField, SubmitField
#用于验证输入的字段是否符合预期
from wtforms.validators import DataRequired

#从WTForms包中导入了四个表示表单字段的类。每个字段类都接受一个描述或别名作为第一个参数，并生成一个实例来作为LoginForm的类属性
class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')
   







