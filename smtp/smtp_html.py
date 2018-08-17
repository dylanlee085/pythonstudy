#!/usr/bin/env 
#coding:utf-8

import smtplib
from email.mime.text import MIMEText

username = "lianjop@163.com"
password = "*******"
host="smtp.163.com"

def sendmail(sender,receiver,content):
    subject = "运维测试"
    msg = MIMEText(content,'html','utf-8')     #需要指明类型为html
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(receiver)

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
    content = """"<p>Python 邮件发送测试...</p><p><a href="http://www.cnblogs.com/freely/">戳它</a></p>"""   #html内容 
    receiver = ["782820303@qq.com","ljp_20131201@163.com"]
    sendmail(sender,receiver,content)
