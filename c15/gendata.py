#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/23'
'''

from random import randint,choice
from string import lowercase  #lowercase 即26位小结字母a-z
from sys import maxint  #根据系统位数，生成最大数据，32、64
from time import ctime

def getRangeStr():
    doms = ('com','edu','gov','org')

    for i in range(randint(5,10)):
        dtint = randint(0,2**32)  #生成一个[0,maxin-1]之间的随机数.
        dtstr = ctime(dtint)      #ctime格式时间的范围限定在0~2^32

    shorter = randint(4,7)
    em = ''

    #随机选出几个字母，拼成字符串
    for j in range(shorter):
        em += choice(lowercase) #random.choice([req]),在列表中随机选择一个元素

    #随机选出几个字母，拼成字符串
    longer = randint(shorter,12)
    dn = ''

    for j in range(longer):
        dn += choice(lowercase)

    return '%s::%s@%s.%s::%d-%d-%d' % \
          (dtstr,em,dn,choice(doms),dtint,shorter,longer)

    #例子：Sun Oct 17 15:12:55 1993::umrpjsn@rlscnzfgnye.org::750841975-7-11

f = open('gendata.txt' , 'w+')
for i in range(1,10):
    if i == 9:
        f.writelines('%s' % getRangeStr())
    else:
        f.writelines('%s\n' % getRangeStr())

f.close()
