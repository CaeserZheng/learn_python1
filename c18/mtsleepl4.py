#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/26'
'''

import threading
from time import ctime,sleep

loops = [4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func,self.args)

def loop(nloop,nsec):
    '''

    :param nloop: 循环对象
    :param nsec: sleep 时间
    :param lock: 锁对象
    :return:
    '''
    print 'start loop',nloop,' at :',ctime()
    sleep(nsec)

    print 'loop',nloop,' done at:',ctime()


def main():
    print 'starting at:',ctime()

    threads = []
    nloops = range(len(loops))

    for i in nloops:   #分配进程
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops:    # 开始进程
        threads[i].start()

    for i in nloops:    #等待全部进程
        threads[i].join()

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()