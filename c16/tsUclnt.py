#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSocket = socket(AF_INET,SOCK_DGRAM) #创建实例

while True:
    data = raw_input('> ')
    if not data:
        break

    udpCliSocket.sendto(data,ADDR)
    data,addr = udpCliSocket.recvfrom(BUFSIZ)

    if not data:
        break
    print '[%s] > %s' % (addr,data)
    #udpCliSocket.close()

udpCliSocket.close()
