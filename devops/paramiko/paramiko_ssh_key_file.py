#!/usr/bin/env python
# coding:utf-8

import paramiko

def deal_file(host,username,port=22):
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport((host,port))
    transport.connect(username=username, pkey=private_key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('/data/test.sh', '/tmp/test.sh')
    sftp.get('/tmp/test.sh', '/data/test_new.sh')
    transport.close()

if __name__ == '__main__':
    with open('list', 'r') as f:
        for line in f.readlines():
            host = line.split(',')[0]
            username = line.split(',')[1]
            deal_file(host,username)

