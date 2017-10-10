# coding=utf-8
import re
import sys
import en
import urllib2
from bs4 import BeautifulSoup
import lxml

def to_mysql(word):         
    print ''

def crawler(url):
    #reload(sys)
    #sys.setdefaultencoding("utf-8")  
    res = urllib2.Request(url) #送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
    response = urllib2.urlopen(res)
    #print response.read()
    soup = BeautifulSoup(response.read(), 'html5lib')
    #with open('html.txt', 'w') as wr:
        #wr.write(response.read().encode('UTF-8'))
    #print soup.prettify('UTF-8')
    """
    with open('html.txt', 'w') as wr:
        wr.write(soup.prettify('UTF-8'))
    """
    with open('span.txt', 'w') as wr:
        for tag in soup.find_all(lang='EN-US'):
            if tag.string != None:
                #wr.write(tag.string.encode('UTF-8'))
                #line=re.sub('\*?\d{4}\.', '', tag.string.encode('UTF-8')).strip()
                line=re.sub(r'[^a-zA-z \n]', '', tag.string.encode('UTF-8')).strip()
                if '[' in line:
                    part=line.split(' ')
                    print part[0]

if __name__ == '__main__':
    print "Start crawler page."
    url="http://www.shute.kh.edu.tw/~t1248/voc7000-AB.htm" #url="來源網址"
    #url = "http://163.21.1.9/t234/Welcome%20to%20Ada%20Web/English/%E8%8B%B1%E6%96%87%E8%AB%BA%E8%AA%9E.htm"
    print url
    crawler(url)