#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/26'
'''

from time import sleep,ctime
dash = '-' * 50
def loop0():
    print 'start loop 0 at:',ctime()
    sleep(4)

    print 'loop 0 done at:',ctime()
    print dash


def loop1():
    print 'start loop 1 at:' , ctime()
    sleep(2)

    print 'loop 1 done at:' , ctime()
    print dash

def main():
    print 'Starting at :' ,ctime()
    loop0()
    loop1()
    print  'All loop DONE  at:',ctime()

if __name__ == '__main__':
    main()