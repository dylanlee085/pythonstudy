#!/usr/bin/env python
# coding: utf-8

import paramiko


def exec_commands(host, username, password,command, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=host,port=port,username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    err_result = stderr.read()
    if len(err_result) == 0:
        print "******** %s the command is successful!********" % host
        print result
    else:
        print "******** %s the command is failed!********" % host
        print err_result
    ssh.close()

if __name__ == '__main__':
    with open('list', 'r') as f:
        for line in f.readlines():
            print line
            host = line.split(',')[0]
            username = line.split(',')[1]
            password = line.split(',')[2]
            command = line.split(',')[4]
            exec_commands(host, username, password,command)



