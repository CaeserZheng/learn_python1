#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/21'
'''

import os
import pickle   #将数据进行序列化读写到硬盘

class FileDescr(object):
    saved = [] #用来记录描述符所访问的所有属性

    def __init__(self,name = None):
        self.name = name

    def __get__(self, obj, typ = None):
        if self.name not in FileDescr.saved:  #在获取描述符的属性之前，必须确保用户给他们的赋值（name）
            raise AttributeError,\
                "%r used before assignment" % self.name

        try:
            f = open(self.name,'r')
            val = pickle.load(f)    #将file中的对象序列化读出
            f.close()
            return val

        except (pickle.PickleError,IOError,
                EOFError,AttributeError,
                ImportError,IndexError),e:
            raise AttributeError,"could nt read %r:%s" % self.name

    def __set__(self, obj, val):
        f = open(self.name,'w')
        try:
            try:
                pickle.dump(val,f)  #将val数据序列化写入文件中
                FileDescr.saved.append(self.name)
            except (TypeError,pickle.PicklingError),e:
                raise AttributeError, \
                    "could not pickle %r" % self.name
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)    #删除文件
            FileDescr.saved.remove(self.name)
        except (OSError,ValueError),e:
            pass

