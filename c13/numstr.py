#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/21'
'''

class NumStr(object):
    def __init__(self,num = 0,string=''):
        self.__num=num
        self.__string=string

    def __str__(self):
        return '[%d::%r]' % (self.__num,self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other,NumStr):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise TypeError,\
                'Illegal argument type for built-in opration'

    def __mul__(self, num):
        if isinstance(num,int):
            return self.__class__(self.__num * num,
                                  self.__string * num)
        else:
            raise TypeError , \
                'Illegal argument type for built-in opration'

    def __nonzero__(self):
        return  self.__num or len(self.__string)

    def __norm_caval(self,cmpres):
        return cmp(cmpres,0)

    def __cmp__(self, other):
        return self.__norm_caval(cmp(self.__num,other.__num)) +\
               self.__norm_caval(cmp(self.__string,other.__string))


a = NumStr(3,'foo')
b = NumStr(3,'goo')
c = NumStr(2,'foo')
d = NumStr()
e = NumStr(string='boo')
f = NumStr(1)

print a,b,c,d,e,f
print a < b
print a + b
print a * 3
print cmp(a,b)

i=1
j=2

print i+j