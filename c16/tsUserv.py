#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from socket import *
from time import ctime

dash = '-' * 50

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM) #创建实例
udpSerSock.bind(ADDR)                   #绑定服务端套接字
#udpSerSock.listen(5)                   #udp 是面向非连接的，因此不需要监听端口

try:
    while True:
        print 'waiting for message...'
        data,addr = udpSerSock.recvfrom(BUFSIZ)

        print dash

        print '[%s] > %s' % (addr,data)

        udpSerSock.sendto('[%s] %s ' %(ctime(),data),addr)

        print '...received from and returned to :' ,addr

except (EOFError,KeyboardInterrupt) as e:
    print 'Error : ',e.message
    udpSerSock.close()
