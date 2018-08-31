#!/usr/bin/env
#coding:utf-8

import os
from flask import Flask, request,redirect,url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/data/uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])   #设置允许上传的文件类型
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024     #限制上传文件大小
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER     #设置上传到的目录

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':                            #判定是否为post请求
        file = request.files['file']                        #通过request的files字典访问文件
        if file and allowed_file(file.filename):             #判断文件类型是否在被允许的上传的文件类型中
            filename = secure_filename(file.filename)        #设置文件安全属性
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))   #保存文件
            return redirect(url_for('uploaded_file',filename=filename))     #文件保存后重定向到指定链接
    return '''<!doctype html>
    <title>上传新文件</title>
    <h1>上传新文件</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>'''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=1)
