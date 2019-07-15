#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/27'
'''

import urllib2
import urlparse

LOGIN = 'aa'
PASSWD = 'mypass'

URL = urlparse.urlunparse(
    ('http','baidu.com','','','',''))

def handler_version(url):
    '''使用handler 模式'''
    from urlparse import urlparse as up
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password('Archives',up(url)[1],LOGIN,PASSWD)

    opener = urllib2.build_opener(hdlr) #创建一个opener，当获取一个URL时，可以使用一 个opener（一个urllib2.OpenerDirector实例对象，可以由build_opener实例化生成）

    urllib2.install_opener(opener) #install_opener如上所述也能用于创建一个opener对象，但是这个对象是（全局）默认的opener。

    return url

def request_version(url):
    '''使用Request模式'''
    from base64 import encodestring
    req = urllib2.Request(url) # 创建一个url请求对象
    b64str = encodestring('%s:%s' % (LOGIN,PASSWD))[:-1]

    req.add_header('Authorization','Basic %s' % b64str) #add_header,生成请求头

    return req

for funcType in ('handler','request'):
    print '*** Using %s:' % funcType.upper()

    url = eval('%s_version' % funcType)(URL)
    try:
        f = urllib2.urlopen(url)
        print  f.readline()
        for i in f.readlines():
            print i
        f.close
    except urllib2.URLError as e:
        print e


