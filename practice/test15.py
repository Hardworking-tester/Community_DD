# encoding:utf-8
import urllib2
import urllib
import cookielib
import re
filename="D:\\wwg.txt"
# cookie=cookielib.MozillaCookieJar(filename)
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata=urllib.urlencode({'account':'wwg','password':'123abc'})
# loginurl="http://192.168.1.159:8080/zentao/user-login-L3plbnRhby8=.html"
# result=opener.open(loginurl,postdata)
# cookie.save(ignore_expires=True,ignore_discard=True)
# gradeurl="http://192.168.1.159:8080/zentao/company-browse.html"
# result2=opener.open(gradeurl)
# print result2.read()
content = response.read().decode('utf-8')
pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                     '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]