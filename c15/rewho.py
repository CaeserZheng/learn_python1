#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/23'
'''
import re
import os

dashes = '\n' + '-' * 50

dfile = 'whodata.txt'
dfile = 'gendata.txt'

patt1 = '^Sun'
patt2 = '\.edu'
f= open(dfile,'r')
for eachLine in f.readlines():
    eachIndexs  = re.split('::',eachLine.strip())
    match_res = re.match(patt1,eachIndexs[0])
    if match_res:
        print eachIndexs

    search_res = re.search(patt2,eachIndexs[1])
    if search_res:
        print eachIndexs

f.close()

print dashes

def whoDataDeal():
    f = os.popen('who','r')
    for eachLine in f.readlines():
        print re.split('\s\s+|\t',eachLine.strip())
    f.close()
