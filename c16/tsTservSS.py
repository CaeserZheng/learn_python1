#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from  SocketServer import (TCPServer as TCP,
                           StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

dash = '-' * 60

class MyRequestHandler(SRH):        #从StreamRequestHandle派生一个子类
    def handle(self):               #重写handle 方法
        print '...conneceted from : ',self.client_address

        msg = self.rfile.readline()
        print '...receive message : ',msg
        self.wfile.write('[%s] %s ' %
                         (ctime(),msg))

        print dash

try:
    tcpServ = TCP(ADDR,MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()
except (EOFError,KeyboardInterrupt) as e:
    print 'Error: ' , e.message
    tcpServ.server_close()
