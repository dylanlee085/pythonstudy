#!/usr/bin/env 
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

username = "lianjop@163.com"
password = "*******"
host="smtp.163.com"

def sendmail(sender,receiver,content):
    subject = "运维测试"
    msg = MIMEMultipart()   #指定内容为混合类型
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(receiver)   #多个收件人时使用join方法连接
    contents = MIMEText(content,'plain', _charset='utf-8')
    msg.attach(contents)
    filename='美图.jpg'
    jpgpart = MIMEApplication(open(filename, 'rb').read())     #打开附件时类型
    jpgpart.add_header('Content-Disposition', 'attachment', filename=filename.decode('utf-8').encode('gb2312'))   #使用中文文件名时需要转码
    msg.attach(jpgpart)
    try:
        server = smtplib.SMTP()
        server.connect(host)
        server.login(username,password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print "邮件发送成功"
    except smtplib.SMTPRecipientsRefused:
        print 'Recipient refused'
    except smtplib.SMTPAuthenticationError:
        print 'Auth error'
    except smtplib.SMTPSenderRefused:
        print 'Sender refused'
    except smtplib.SMTPException,e:
        print e.message

if __name__ == "__main__":
    sender = "运维测试" + "<" + username +">"
    content = "请查收每日入驻数据"
    receiver = ["782820303@qq.com","ljp_20131201@163.com"]
    sendmail(sender,receiver,content)
