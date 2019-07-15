#!/usr/bin/env python

import cgi

reshtml = '''Content-type:text/html\n
    <HTML><HEAD><TITLE>Friends CGI DEMO
    </TITLE></HEAD>
    <body><H3>Friends list for:<I>%s</I></H3>
    <p>
        Your name is:<B>%s</B>
        You have <B>%s</B> frineds.
    </p>
    </BODY></HTML>
'''

form = cgi.FieldStorage()
who = form['person'].value
howmany =form['howmany'].value

print reshtml % (who,howmany)