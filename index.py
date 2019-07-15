#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/20'
'''

class TestStaticMethod:
    @staticmethod
    def foo():
        print 'calling static method foo() :', TestStaticMethod.__name__


class TestClassMethod:
    @classmethod
    def foo(cls):
        print 'calling class method foo() :' , cls.__name__


tsm = TestStaticMethod()
tsm.foo()
tcm = TestClassMethod()
tcm.foo()


