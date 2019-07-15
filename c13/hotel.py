#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/19'
'''


class HotelRoomCalc(object):
    '旅馆租房费用计算器'

    def __init__(self,rt,sales=0.085,rm=0.1):
        '销售税8.5%，房间税10%'
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt
    def calcTotal(self,days=1):
        daily = round((self.roomRate * (1+self.salesTax + self.roomTax)),2)
        return float(days)*daily


sfo = HotelRoomCalc(299)
print sfo.calcTotal()