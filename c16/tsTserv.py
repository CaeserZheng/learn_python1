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
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM) #创建实例
tcpSerSock.bind(ADDR)                   #绑定服务端套接字
tcpSerSock.listen(5)                    #监听请求链接并发数

try:
    while True:
        print 'waiting for connection...'
        tcpCliSock,addr = tcpSerSock.accept()
        print dash
        print '...connected from:',addr


        while True:
            try:
                data = tcpCliSock.recv(BUFSIZ)
                if not data:
                    break
                print '%s > %s' % (addr[0],data)

                tcpCliSock.send('[%s] %s' % (ctime(),data))
                print 'server > [%s] %s' % (ctime(),data)
                #tcpCliSock.close()
            except error as e:
                print "Socket ERROR：",e.message
                tcpCliSock.close()
                tcpSerSock.close()
                break
        tcpCliSock.close()
except (EOFError,KeyboardInterrupt) as e:
    print 'Error : ',e.message
    tcpSerSock.close()




