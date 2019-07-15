#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from twisted.internet import protocol,reactor,selectreactor

PORT = 21569
dash = '-' * 50

userList = ['Alice','Bob']

class HalfDuplexChatServProtocol(protocol.Protocol):
    '''半双工'''

    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        port = self.port = self.transport.getPeer().port
        print '...connection from : [%s] %s ' % (clnt , port)

    def dataReceived(self, data):
        print '...receive data : ' ,data
        responeData = raw_input(' > ')
        self.transport.write('[%s]' % (responeData))

class FullDuplexChatServProtocol(protocol.Protocol):
    '''全双工'''

    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        port = self.port = self.transport.getPeer().port
        print '...connection from : [%s] %s ' % (clnt , port)

    def dataReceived(self, data):
        print '...receive data : ' ,data
        responeData = raw_input(' > ')
        self.transport.write('[%s]' % (responeData))

try:
    factory = protocol.Factory()          #创建一个工厂，每次有连接进来时，就会产生一个protocal对象。来监听请求。
    factory.protocol = HalfDuplexChatServProtocol       #请求进来是，创建一个TSSserProtocol进行处理
    print 'waiting for connection...'
    print dash


    reactor.listenTCP(PORT,factory)
    reactor.run()
except (EOFError,KeyboardInterrupt) as e:
    print 'Error:' ,e.message
    reactor.stop()