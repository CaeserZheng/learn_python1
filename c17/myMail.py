#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/25'
'''

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

origHdrs = [
    'From:zgl3010@qq.com',
    'To:zhengguoliang@qiniu.com',
    'Subject:test msg'
            ]

origBody = ['xxx','yyy','zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('zgl3010@qq.com',('zhengguoliang@qiniu.com',),origMsg)
sendSvr.quit()

assert len(errs) == 0,errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('xxx')
recvSvr.pass_('xxxx')

rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
sep =msg.index('')
recvBody = msg[sep+1:]

assert origBody == recvBody



