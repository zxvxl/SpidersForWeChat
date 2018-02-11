# SpidersForWeChat
SpidersForWeChat

抓取搜狗微信公众号文章

此爬虫用来抓取搜狗微信公众号文章，搜狗微信只能显示公众号10篇文章，
所以此爬虫也是为了抓取公众号的最新文章。

1.抓取公众号的最新文章
2.可绕过验证码，绕过IP封禁。
3.可设置定时任务。begin.py中配置爬虫间隔时间

Python 2.7.14

因本人是新手，不熟Python，里面有很多不足之处，通过各种查资料，填坑，用时两周才完成功能，望见谅！

需要用到plantoms.js ，bin文件下的js，查看相关文件

test.py 中

start_urls 中填写搜狗微信中搜索相关公众号的链接

cmd = 'phantomjs E:\phantomjs\/bin\getBody.js "%s"' % history_page_url

请根据本地路径配置

setting.py 中，填写自己要保存的数据库连接信息

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'zl'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_PORT = 3306

表结构如db.sql


来之不易，如有转载请注明出处！


