#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/19'
'''

class AddrBookEntry():
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print "Created instance for:",self.name
    def updatePhone(self,newph):
        self.phone = newph
        print "Update phpne# for:", self.name

class EmpAddrBookEntry(AddrBookEntry):
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid = id
        self.empem = em

    def updateEmail(self,newem):
        self.empem = newem
        print "Update E-mail address for : ",self.name


eb = EmpAddrBookEntry("John","123",1,"zgl3010@qq.com")

print eb.name
print eb.phone
print eb.empid
print eb.empem
print "-----------"

eb.updatePhone("333")
eb.updateEmail("abc@qq.com")

print eb.name
print eb.phone
print eb.empid
print eb.empem
