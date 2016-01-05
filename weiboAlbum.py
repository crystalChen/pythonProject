#coding=utf-8
import urllib2
import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
'cookie': 'copy浏览器的cooke字符串'}
req = urllib2.Request('http://weibo.cn/album/albummblog/?rl=11&fuid=1558100377&page=12', headers=headers) 
r = urllib2.urlopen(req)
data = r.read()
p = re.compile(r'src="http://ww(.).sinaimg.cn/square/(.{32}).jpg" alt=')
uuids = p.findall(data)
urls = []
for uuid in uuids:
   url = 'http://ww' + uuid[0] + '.sinaimg.cn/mw1024/' + uuid[1] + '.jpg'
   urls.append(url)

i = 0
for url in urls:
	response = requests.get(url)
	if response.status_code == 200:
		i += 1
		f = open("/Users/chen/Downloads/weibo/"+ str(i) +".jpg", 'wb')
		f.write(response.content)
		f.close()

