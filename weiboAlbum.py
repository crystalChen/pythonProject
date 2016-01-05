#coding=utf-8
# 功能：下载刘亦菲微博原创相册
# 没有实现用户名密码登录，直接copy了浏览器cookie字符串，暴力。
# 并没有从网页浏览器直接爬取，因为那样要分析它前端JS，有些操作比较难实现。
# 一般思路是从手机端入手，因为手机端没有做那么多的限制，从而找到规律，然后在抓取PC端的数据。
# 脚本写于2015年七月末，爬取刘亦菲的所有原创相册后，发现了一个秘密，只为宋XX这一个男性单独配过图，处女座有洁癖，何况我女神，写文字配图必然精简干练，暗不爽。
# 八月几号就传来了他们正在交往的消息，噩耗。
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

