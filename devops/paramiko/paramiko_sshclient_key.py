#!/usr/bin/env python
# coding: utf-8



import paramiko


def exec_commands(host, username, command, port=22):
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,port=port,username=username, pkey=private_key)
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
            host = line.split(',')[0]
            username = line.split(',')[1]
            command = line.split(',')[4]
            exec_commands(host, username,command)
