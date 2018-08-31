#!/usr/bin/env python
# coding: utf-8



import paramiko


def exec_commands(host, username, command, port=22):
    # 指定私钥文件
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    #创建Transport连接对象
    transport = paramiko.Transport((host,port))
    #使用密钥连接主机
    transport.connect(username=username, pkey=private_key)
    #创一个SSHClient对象
    ssh = paramiko.SSHClient()
    #将ssh对象和Transport对象绑定
    ssh._transport = transport
    #执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    #接收返回
    result = stdout.read()
    err_result = stderr.read()
    if len(err_result) == 0:
        print "******** %s the command is successful!********" % host
        print result
    else:
        print "******** %s the command is failed!********" % host
        print err_result
    transport.close()

if __name__ == '__main__':
    with open('list', 'r') as f:
        for line in f.readlines():
            host = line.split(',')[0]
            username = line.split(',')[1]
            command = line.split(',')[4]
            exec_commands(host, username,command)
