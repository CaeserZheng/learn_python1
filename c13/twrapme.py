#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/21'
'''

from time import time,ctime

class TimedWrapme(object):
    def __init__(self,obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()  #返回当前的时间戳 1970纪元后经过的浮点秒数

    def get(self):
        '获取时间戳'
        self.__atime = time()

    def gettimeval(self,t_type):
        '返回属性值'
        if not isinstance(t_type,str) or t_type[0] not in 'cma':
            raise TypeError,"argument of 'c' , 'm' or 'a',req d "
        return getattr(self,'_%s__%stime' % (self.__class__.__name__,t_type[0]))

    def gettimestr(self,t_type):
        '通过ctime 转化为asctime Tue Feb 17 10:00:18 2013'
        return ctime(self.gettimeval(t_type))

    def set(self,obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):        #实现repr(),说明—__data的来源
        self.__atime =time()
        return 'self.__data'

    def __str__(self):          #被print 调用表示对象
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data,attr)



timeWrapperObj = TimedWrapme(800)
print timeWrapperObj.gettimestr('c')
print timeWrapperObj.gettimestr('a')
print timeWrapperObj.gettimestr('m')


timeWrapperObj
print repr(timeWrapperObj)
print timeWrapperObj.gettimestr('c')

print timeWrapperObj.gettimestr('a')
print timeWrapperObj.gettimestr('m')


