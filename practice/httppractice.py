#encoding:utf-8
import urllib
import urllib2
url = 'http://push.hao123.com/apis/test_send_msg.php'
values = {'g_id':'1027019902',
          'm_time_to_send':'1386049369',
          'm_display':'1',
          'm_push_type':'2'
          ,'m_by_timezone':'0'
          ,'m_msg':'中华人民共和国万岁'
          ,'mt_id':'0',
          'm_iggid_file':'33600458'
         }
data = urllib.urlencode(values)
print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page