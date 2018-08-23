#!/usr/bin/env python
# coding: utf-8

import paramiko

def exec_commands(host,username,password,command,port=22):
    #建立一个trans对象
    trans = paramiko.Transport((host, port))
    #建立连接
    trans.connect(username=username,password=password)
    #将sshclient 对象的transport指定为前面建立的trans对象
    ssh = paramiko.SSHClient()
    ssh._transport=trans
    #执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    #打印输出
    result = stdout.read().decode()
    err_result = stderr.read().decode()
    if len(err_result) == 0:
        print "******** %s the command is successful!********" % host
        print result
    else:
        print "******** %s the command is failed!********" % host
        print err_result
    #关闭连接
    trans.close()

if __name__ == '__main__':
    with open('list', 'r') as f:
        for line in f.readlines():
            host = line.split(',')[0]
            username = line.split(',')[1]
            password = line.split(',')[2]
            command = line.split(',')[4]
            exec_commands(host,username,password,command)