#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/26'
'''

import onethr
import thread
from time import ctime,sleep

def main():
    print 'starting at:',ctime()

    'thread.start_new_thread的第一个参数需要传函数名，而不是执行函数即function()'
    thread.start_new_thread(onethr.loop0,())
    thread.start_new_thread(onethr.loop1,())

    sleep(6)   #主进程通过sleep6 来等待子进程执行完成，可以引入锁来搞定这个同步的过程

    print 'All Done at:',ctime()

if __name__ == '__main__':
    main()