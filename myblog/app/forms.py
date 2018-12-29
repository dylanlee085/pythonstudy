#!/usr/bin/env python
# coding: utf-8

#从flask_wtf导入FlaskForm的基类
from flask_wtf import FlaskForm
#由于flask_wtf插件本身提供字段类型,所以从wtf从wtforms导入四个表示表单字段的类
from wtforms import StringField, PasswordField, BooleanField, SubmitField
#用于验证输入的字段是否符合预期
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#导入user模块
from app.models import User

##文本输入
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


#从WTForms包中导入了四个表示表单字段的类。每个字段类都接受一个描述或别名作为第一个参数，并生成一个实例来作为LoginForm的类属性
class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')
   

#注册类
class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired()])
   password2 = PasswordField(
      'Repeat Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Register')

   def validate_username(self, username):
      user = User.query.filter_by(username=username.data).first()
      if user is not None:
         raise ValidationError('Please use a different username.')

   def validate_email(self, email):
      user = User.query.filter_by(email=email.data).first()
      if user is not None:
         raise ValidationError('Please use a different email address.')


#editprofile
class EditProfileForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
   submit = SubmitField('Submit')

   def __init__(self, original_username, *args, **kwargs):
      super(EditProfileForm, self).__init__(*args, **kwargs)
      self.original_username = original_username

   def validate_username(self, username):
      if username.data != self.original_username:
         user = User.query.filter_by(username=self.username.data).first()
         if user is not None:
            raise ValidationError('Please use a different username.')



#Post类
class PostForm(FlaskForm):
   post = TextAreaField('Say something', validators=[
      DataRequired(), Length(min=1, max=140)])
   submit = SubmitField('Submit')


#resetpassword
class ResetPasswordRequestForm(FlaskForm):
   email = StringField('Email', validators=[DataRequired(), Email()])
   submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
   password = PasswordField('Password', validators=[DataRequired()])
   password2 = PasswordField(
      'Repeat Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Request Password Reset')


class MessageForm(FlaskForm):
   message = TextAreaField('Message', validators=[
      DataRequired(), Length(min=0, max=140)])
   submit = SubmitField('Submit')






