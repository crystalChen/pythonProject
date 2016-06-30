# pythonProject

weiboAlbum.py:
微博相册爬虫。
1.爬取新浪微博需要登录，这里没有破解用户名密码登录，而是直接copy通过浏览器登录后的cookie字符串，作为token登录；
2.爬虫一般从移动端入手更加容易。web微博拉取feed用了JS，而手机端直接返回所有数据，更容易分析数据。