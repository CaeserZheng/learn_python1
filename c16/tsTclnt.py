#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSocket = socket(AF_INET,SOCK_STREAM) #创建实例

tcpCliSocket.connect(ADDR)   #建连套接字

while True:
    data = raw_input('> ')
    if not data:
        break

    tcpCliSocket.send(data)
    data = tcpCliSocket.recv(BUFSIZ)

    if not data:
        break
    print data

tcpCliSocket.close()