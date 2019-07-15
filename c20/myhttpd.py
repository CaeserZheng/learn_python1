#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   myhttpd.py
@Time    :   2019/07/02 23:13:01
@Author  :   Caeser Zheng 
@Contact :   zgl3010@qq,cin
'''

from os import curdir,sep
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            uri = curdir+sep+self.path
            f=open(uri)
            #curdir 返回当前相对路径
            #sep系统目录分隔符  /
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.send_header('X-ser','myhttpd/1.1')
            self.end_headers()
            self.wfile.write(f.read())
        except IOError:
            self.send_error(404,'File Not Found :%s' %self.path)

def main():
    try:
        server = HTTPServer(('127.0.0.1',8081),MyHandler)
        print 'Welcome to the machine...'
        print 'Press ^C once or twice to quit...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C revievied,shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
    

