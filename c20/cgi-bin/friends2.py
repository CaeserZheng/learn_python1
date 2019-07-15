#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   friends2.py
@Time    :   2019/07/02 20:58:47
@Author  :   Caeser Zheng 
@Contact :   zgl3010@qq,cin
'''

import cgi

header = 'Content-Type:text/html\n\n'

formhtml = '''
    <HTML><HEAD><TITLE>Friends CGI DEMO
    </TITLE></HEAD>
    <body>
        <H3>Friends list for:
            <I>NEW USER</I>
        </H3>
    <form action="/cgi-bin/friends2.py">
        <B>Enter You Name:</B>
        <input type=hidden name=action value=edit>
        <input type=text name=person value="NEW USER" size=15>
        <p><b>how many friends do you have?</b></p>
        %s
        <p><input type=submit>
    </from>
    </BODY>
    </HTML>
'''

fradio = '<input type=radio name=hownamy value="%s" %s> %s\n'
def showFrom():
    frineds = ''
    for i in [0,10,25,50,100]:
        checked = ''
        if i == 0:
            checked = 'CHECKED'
        frineds = frineds+fradio % (str(i),checked,str(i))

    print header + formhtml % (frineds)

reshtml = '''<HTML><HEAD><TITLE>Friends CGI DEMO
    </TITLE></HEAD>
    <body><H3>Friends list for:<I>%s</I></H3>
    <p>
        Your name is:<B>%s</B>
        You have <B>%s</B> frineds.
    </p>
    </BODY>
    </HTML>
'''

def doResults(who,howmany):
    print header + reshtml %(who,who,howmany)

def process():
    form = cgi.FieldStorage()
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        howmany =0

    if form.has_key('action'):
        doResults(who,howmany)
    else:
        showFrom()

if __name__ == '__main__':
    process()
    
