#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/26'
'''

import onethr
import thread
from time import ctime,sleep

loops = [4,2]

def loop(nloop,nsec,lock):
    '''

    :param nloop: 循环对象
    :param nsec: sleep 时间
    :param lock: 锁对象
    :return:
    '''
    print 'start loop',nloop,'at :',ctime()
    sleep(nsec)

    print 'loop',nloop,'done at:',ctime()
    lock.release()      #release() 释放锁


def main():
    print 'starting at:',ctime()

    locks=[]
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()  #allocate_lock 分配锁
        lock.acquire()                  #获取锁对象
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    #实现子进程同步
    for i in nloops:
        while locks[i].locked(): #如果获取了锁对象返回true，否则返回false
            pass

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()