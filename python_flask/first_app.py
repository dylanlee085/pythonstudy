#! /usr/bin/env python
# coding: utf-8


from flask import Flask
from flask import redirect



#创建一个flask实例
app = Flask(__name__)

#使用程序实例提供的app.route装饰器，把修饰的函数注册为路由
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


#带有变量的url
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name


#跳转
@app.route('/baidu')
def baidu():
    return redirect('https://www.baidu.com')




#启动程序
if __name__ == '__main__':
    app.run(debug=True,port = 8888, host = '0.0.0.0')





1*（1 + 0.2)*（1 + 0.2)*（1 + 0.2)*(1+0.2)

1.44