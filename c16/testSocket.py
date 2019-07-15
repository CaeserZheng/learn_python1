#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/24'
'''

import socket

myFirstSocket = socket.socket()
myFirstSocket.bind('127.0.0.1')

myFirstSocket.listen('8888')

while True:
    cs = myFirstSocket.accept()
    csd = myFirstSocket.recv()
