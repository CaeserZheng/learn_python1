#!/usr/bin/env python
#-.- coding=utf-8 -.-
'''
__author__ = 'caeser'
__mtime__ = '2019/6/27'
'''


from sys import argv
from os import makedirs,unlink,sep,rmdir
from os.path import  dirname,exists,isdir,splitext
from string import replace,find,lower

from htmllib import  HTMLParser
from urllib import urlretrieve
from urlparse import urlparse,urljoin

from formatter import  DumbWriter,AbstractFormatter
from  cStringIO import StringIO
from time import sleep
import re
import shutil

def callbackInfo(down , block , size):
    '''
        回调函数：
        down：已经下载的数据块
        block：数据块的大小
        size：远程文件的大小
    '''
    if not (size > 0):
        print '...Warnning Size : [%s]' % size
        per = 100
    else:
        print 'down=%s;block=%s;size=%s' % (down , block , size)
        per = 100.0 * (down * block) / size
        if per > 100:
            per = 100
    print '%.2f%%' % per

    sleep(1)
def urlMatch(url):
    urlReg = '[a-zA-z]+://[^\s]*'
    httpUrlReg = '^https?://[^\s]*'

    return re.match(httpUrlReg,url)

class Retriever(object):
    '''检索并解析每一个下载下来的web网页'''
    def __init__(self,url):
        self.url = url
        self.file = self.filename(url)

    def filename(self,url,deffile='index.html'):
        parsedurl = urlparse(url)
        #返回一个包含6个字符串项目的元组：协议、位置、路径、参数、查询、片段

        path = parsedurl.netloc + parsedurl.path
        ext = splitext(path)   #splitext搜索文件路径（path）和文件的扩展名
        # （ext)，如a.png,ext=('a','png')

        if ext[1] == '':
            #no file ,use default
            #例如www.baidu.com -->www.baidu.com/index.html
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile

        ldir = dirname(path) #dirname 去掉文件名，返回目录
        if sep !='/': #os.sep 主要用于系统路径中的分隔符
            ldir = replace(ldir,'/',sep)

        if isdir(ldir):
            #使用isdir辨别文件类型是不是目录。
            if exists(ldir):
                #unlink(ldir) #unlink 方法用于删除文件,如果文件是一个目录则返回一个错误。
                shutil.rmtree(ldir)
                print '目录 [%s] 已存在，删除目录....' % (ldir)

        print '创建目录 --> [%s]' % ldir
        makedirs(ldir)      #生成目录
        return path


    def download(self): #下载网页
        try:
            retval = urlretrieve(self.url,self.file,callbackInfo)
            '''
            参数url：下载链接地址
            参数filename：指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
            参数reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
            参数data：指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头
            :return filename, headers
            '''
        except IOError:
            retval = ('*** ERROR: invald URL "%s"' % (self.url))

        return retval

    def parseAndGetLinks(self):
        '''解析html页面，获取页面中的链接，并保存链接'''

        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        #使用HTMLParser的方法进行处理 , StringIO是从内存中读取数据，DumbWriter将事件流转换为存文本文档。
        self.parser.feed(open(self.file).read())
        #将self.file文件打开，并一次性读入上面定的文件中

        self.parser.close()
        print 'self.parser.anchorlist --> ' ,self.parser.anchorlist
        return self.parser.anchorlist  #anchorlist 记录href 地址


class Crawler(object):
    '''
    管理爬虫进程
    '''
    count = 0

    def  __init__(self,url):
        self.q = [url]
        #第一个数据是q,这是一个有下载连接组成的队列，
        #这个清单在执行过程中是会变化的，每处理一个主页它就缩短一次，
        #而在各下载主页中发现一个新的连接就会被加长。

        self.seen = []
        #Crawler的另外两个数据项包括seen-这是我们已经下载过的全体连接所组成的一个列表；

        self.dom = urlparse(url)[1]
        #把主连接的域名报存在dom中，用这个值核对后续连接是否属于这同一个区域。

    def getPage(self,url):
        #getPage()方法用第一个连接实例化出一个Retriever对象，从她开始进行后续的处理。
        r = Retriever(url)
        retval = r.download()

        if retval[0] == '*': #如果首字符未*,说明出错
            print retval
            return

        Crawler.count += 1 #记录
        print '\n(' , Crawler.count ,')'
        print 'URL: ', url
        print 'FILE: ',retval[0]

        self.seen.append(url)   #记录已经处理的链接

        links = r.parseAndGetLinks()
        #获取url中的url列表
        linkcount =0
        for eachLink in links:
            #确认是否是http请求
            linkcount+=1
            print '[%d] link --> [%s]' % (linkcount,eachLink)
            if (eachLink[:4] != 'http' or eachLink[:5] != 'https') and find(eachLink,'://') == -1:
                #str.find(str, beg=0, end=len(string)),存在返回-1
                eachLink = urljoin(url,eachLink)
                print '* ', eachLink

            if find(lower(eachLink),'mailto:') !=-1:
                print '...discarded,mailto link'
                continue

            if eachLink not in self.seen:
                if  find(eachLink,self.dom) == -1:
                    print '...discarded ,not in domain'
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print '...new, added to Q'
                    else:
                        print '...discarded, already in Q'
            else:
                print '...discarded ,already processed'

    def go(self):#循环进程
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    if len(argv) > 1:
        url = argv[1]

    else:
        try:
            while True:
                url = raw_input('Enter Starting URL: ').strip()
                if not url:
                    return
                if not urlMatch(url):
                    print '...invalid url [%s]' , url
                else:
                    break
        except (KeyboardInterrupt,EOFError):
            url = ''

    if url[-1] != '/':
        url += '/'
    print '...Root Url: ',url

    robot = Crawler(url)

    robot.go()

if __name__ == '__main__':
    main()
