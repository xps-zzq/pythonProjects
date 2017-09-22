# _*_ coding:UTF-8 _*_
import cookielib
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
req = urllib2.Request('http://msg.csdn.net/')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
response = urllib2.urlopen(req)
print response.read()
