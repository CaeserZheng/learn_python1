#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

from twisted.internet import protocol,reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        '''发送数据'''
        data = raw_input('>')
        if data:
            print '...sending %s...' % data
            self.transport.write(data) #发送数据给服务端
        else:
            self.transport.loseConnection() #关闭套接字

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    '''创建一个客户端工厂'''
    protocol = TSClntProtocol
    #clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()
    def clientConnectionFailed(self, connector, reason):
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()

