#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

dash = '-' * 50

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        port = self.port = self.transport.getPeer().port
        print '...connection from : [%s] %s ' % (clnt,port)

    def dataReceived(self, data):
        print '...receive data : ' ,data
        self.transport.write('[%s] %s' % (ctime(),data))



try:
    factory = protocol.Factory()          #创建一个工厂，每次有连接进来时，就会产生一个protocal对象。来监听请求。
    factory.protocol = TSServProtocol       #请求进来是，创建一个TSSserProtocol进行处理
    print 'waiting for connection...'
    print dash

    reactor.listenTCP(PORT,factory)
    reactor.run()
except (EOFError,KeyboardInterrupt) as e:
    print 'Error:' ,e.message
    reactor.stop()

