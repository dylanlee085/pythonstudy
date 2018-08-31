#!/usr/bin/env 
#coding:utf-8

import smtplib
from email.mime.text import MIMEText

username = "lianjop@163.com"
password = "*******"
host="smtp.163.com"
def sendmail(sender,receiver,content):
    subject = "运维测试"
    msg = MIMEText(content,'plain','utf-8')     #指定类型为文本
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(receiver)    #多个收件人时使用join方法连接
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
    content = "航拍东风水库 湖面孤岛像把琴"
    receiver = ["782820303@qq.com","ljp_20131201@163.com"]   
    sendmail(sender,receiver,content)
