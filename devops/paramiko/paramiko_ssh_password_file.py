#!/usr/bin/env python
# coding:utf-8


import paramiko

def deal_file(host,username,password,port=22):
    #建立一个trans对象
    transport = paramiko.Transport((host, port))
    #建立连接
    transport.connect(username=username,password=password)
    #创建sftp对象
    sftp =paramiko.SFTPClient.from_transport(transport)
    #上传文件
    sftp.put('/data/test.sh', '/tmp/test.sh')
    sftp.get('/tmp/test.sh', '/data/test_new.sh')
    #关闭连接
    transport.close()

if __name__ == '__main__':
    with open('list', 'r') as f:
        for line in f.readlines():
            host = line.split(',')[0]
            username = line.split(',')[1]
            password = line.split(',')[2]
            deal_file(host,username,password)